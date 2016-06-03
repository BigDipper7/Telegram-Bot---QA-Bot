# coding=utf-8
#!/usr/bin/env python
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

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

def finalTest():
    updater = Updater(token = TOKEN)
    dispatcher = updater.dispatcher

    qa_cmd_handler = CommandHandler('/qa',)
    dispatcher.add_handler(qa_cmd_handler)

def qa(bot, update):
    uid = update.chat.id
    txt = 'ni cai a'

    bot.sendMessage(chat_id=uid, text=txt)

def anotherUpdaterDemo():
    updater = Updater(token = TOKEN)
    dispatcher = updater.dispatcher

    start_cmd_handler = CommandHandler('start', echoMsg)
    dispatcher.add_handler(start_cmd_handler)

    echo_handler = MessageHandler([Filters.text], echoMsg)
    dispatcher.add_handler(echo_handler)

    caps_cmd_handler = CommandHandler('caps', capsCommand, pass_args=True)
    dispatcher.add_handler(caps_cmd_handler)

    updater.start_polling()

def capsCommand(bot, update, args):
    print '/caps'
    text_args = ' '.join(args).upper()
    bot.sendMessage(chat_id=update.chat.id, text=text_args)

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
    bot.sendMessage(chat_id=update.message.chat.id,text="echo:"+update.message.text[7:])
    print '----------------echo success------------------'

if __name__ == '__main__':
    main()
