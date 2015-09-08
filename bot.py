import telegram
from settings import *

from plugins.echo import EchoPlugin
from plugins.ip import IpPlugin
from plugins.ww import WuxiWeatherPlugin

LAST_UPDATE_ID = None

plugins = [EchoPlugin, IpPlugin, WuxiWeatherPlugin]

def get_plugin(command):
    return dict([(t.command, t) for t in plugins])[command]


def main():
    global LAST_UPDATE_ID
    bot = telegram.Bot(token=TOKEN)
    try:
        LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
    except IndexError:
        LAST_UPDATE_ID = None
    while True:
        dispatch(bot)


def dispatch(bot):
    global LAST_UPDATE_ID
    for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=10):
        message = update.message.text.encode('utf-8')
        if message:
            command = message.split(" ")[0]
            try:
                get_plugin(command)(bot).run(update)
            except KeyError:
                pass
            LAST_UPDATE_ID = update.update_id + 1


if __name__ == "__main__":
    main()
