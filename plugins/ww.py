from plugins.base import BasePlugin


class WuxiWeatherPlugin(BasePlugin):
    command = "/ww"

    def __init__(self, bot):
        self.bot = bot

    def run(self, update):
        chat_id = update.message.chat_id
        text = update.message.text.encode('utf-8')
        self.bot.sendMessage(chat_id=chat_id,
                             text="asdfasf")
