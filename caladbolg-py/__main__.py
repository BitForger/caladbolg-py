import discord
from dotenv import load_dotenv
import os
from nanoid import generate
import logging

_logger = logging.getLogger('caladbolg.main')
_logger.setLevel(level=logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
_logger.addHandler(ch)

_logger.warning("Warn")
_logger.info("Info")
_logger.debug("debug")

load_dotenv()


class CaladbolgClient(discord.Client):
    async def on_ready(self):
        _logger.info('Logged in', extra={"self": self})

    async def on_message(self, message):
        trace_id = generate()
        _logger.debug('Processing message', extra={"trace_id": trace_id, "content": message.content})
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')


def main():
    client = CaladbolgClient()
    client.run(os.getenv('DISCORD_TOKEN'))


if __name__ == '__main__':
    main()
