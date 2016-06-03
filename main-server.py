# coding=utf-8
#!/usr/bin/env python
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = '192123489:AAFzhC6qzSzbii-FVaDxxzWuKENIANzzH7U'

def main():
    updater = Updater(token = TOKEN)
    dispatcher = updater.dispatcher

    print 'Server Begin...'
    print 'Bot:'+TOKEN
    print '\n\n================================\n\n'

    #Add commands and filters
    start_cmd_handler = CommandHandler('start', echoMsgCB)
    dispatcher.add_handler(start_cmd_handler)

    qa_cmd_handler = CommandHandler('qa', qaCommandCB)
    dispatcher.add_handler(qa_cmd_handler)

    echo_handler = MessageHandler([Filters.text], echoMsgCB)
    dispatcher.add_handler(echo_handler)

    caps_cmd_handler = CommandHandler('caps', capsCommandCB, pass_args=True)
    dispatcher.add_handler(caps_cmd_handler)

    updater.start_polling()

def unknownCommand(bot, update):
    return ''

def qaCommandCB(bot, update):
    print '------ receive raw data:'
    print update
    print '----------------begin qa--------------------'
    uid = update.message.chat.id
    txt = 'ni cai a'

    bot.sendMessage(chat_id=uid, text=txt)
    print '----------------end qa----------------------'

def capsCommandCB(bot, update, args):
    print '/caps'
    text_args = ' '.join(args).upper()
    bot.sendMessage(chat_id=update.chat.id, text=text_args)

def echoMsgCB(bot, update):
    print '------ receive raw data:'
    print update
    print '----------------begin echo--------------------'

    uid = update.message.chat.id

    # bot.sendChatAction(chat_id=uid,action=telegram.ChatAction.TYPING)
    bot.sendMessage(chat_id=uid,text="已收到消息，echo")
    bot.sendMessage(chat_id=uid,text="echo:\n"+update.message.text)
    if len(update.message.entities) > 0:
        txt = update.message.text
        for e in update.message.entities:
            print 'entities: '
            print e
            if e.type == u'bot_command' and e.offset == 0:
                txt = txt[e.length:]
                print 'new txt=|'+txt+'|'
                bot.sendMessage(chat_id=uid,text="echo:\n"+txt)

    print '----------------echo success------------------'


if __name__ == '__main__':
    main()
