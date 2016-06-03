# coding=utf-8
#!/usr/bin/env python
from telegram import Bot

bot = Bot(token = '192123489:AAFzhC6qzSzbii-FVaDxxzWuKENIANzzH7U')
def main():
    print bot.getMe()
    updates = bot.getUpdates()
    print updates
    print [u.message.text for u in updates]
    print '------ echo --------'
    for u in updates:
        echoMsg(bot, u)

def echoMsg(bot, update):
    bot.sendMessage(chat_id=update.message.chat.id,text="echo....")
    bot.sendMessage(chat_id=update.message.chat.id,text="echo:"+update.message.text)

if __name__ == '__main__':
    main()
