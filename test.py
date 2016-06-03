# coding=utf-8
#!/usr/bin/env python
from telegram import Bot
from telegram.ext import Updater, CommandHandler

TOKEN = '192123489:AAFzhC6qzSzbii-FVaDxxzWuKENIANzzH7U'

def originBot():
    bot = Bot(token = TOKEN)
    print bot.getMe()
    updates = bot.getUpdates()
    print updates
    print [u.message.text for u in updates]
    print '------ echo --------'
    for u in updates:
        echoMsg(bot, u)

def anotherUpdaterDemo():
    updater = Updater(token = TOKEN)
    dispatcher = updater.dispatcher

    start_cmd_handler = CommandHandler('start', echoMsg)
    dispatcher.add_handler(start_cmd_handler)

    updater.start_polling()

def main():
    # originBot()
    anotherUpdaterDemo()

def echoMsg(bot, update):
    print 'receive command /start'
    # print 'receive update content: '+update
    print update
    print '----------------begin echo--------------------'
    bot.sendMessage(chat_id=update.message.chat.id,text="echo....")
    bot.sendMessage(chat_id=update.message.chat.id,text="echo:"+update.message.text)
    print '----------------echo success------------------'

if __name__ == '__main__':
    main()
