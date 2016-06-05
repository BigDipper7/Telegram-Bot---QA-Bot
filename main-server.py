# coding=utf-8
#!/usr/bin/env python
from telegram import Bot, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import urllib
import time
import thread
import json

TOKEN = '192123489:AAFzhC6qzSzbii-FVaDxxzWuKENIANzzH7U'
HOST = 'http://localhost:8080'
URL = '/json/query'

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
                # bot.sendMessage(chat_id=uid,text="echo:\n"+txt)
                # res = queryTomcat(uid, txt)
                bot.sendMessage(chat_id=uid,text='小水管，正在查询中，请稍后...')
                thread.start_new_thread(worker,(bot, uid, txt,1))
                # bot.sendMessage(chat_id=uid,text=res)

    print '----------------echo success------------------'

def queryTomcat(uid, text):
    print 'begin doing querying...'
    params = urllib.urlencode({'uid':uid, 'qatxt':text.encode('utf-8')})
    f = urllib.urlopen(HOST+URL, params)
    result = f.read()
    print result
    test = json.loads(result)
    print test
    qus = test['question']
    aut = test['answers'][0]['author']
    con = test['answers'][0]['content']
    print qus, aut, con
    return result, qus, aut, con

def worker(bot, uid, text, interval):
    cnt = 0
    while cnt<1:
        print 'Thread:(%d) Time:%s\n'%(uid, time.ctime())
        time.sleep(interval)
        cnt+=1
    res, qus, aut, con = queryTomcat(uid, text)
    print 'before process:'+con
    con = con.replace('<p>','')
    con = con.replace('</p>','\n')
    print 'after process:'+con
    bot.sendMessage(chat_id=uid,text=res)
    bot.sendMessage(chat_id=uid,text=qus)
    # bot.sendMessage(chat_id=uid,text=qus.encode('utf-8'))#same result like upper one
    bot.sendMessage(chat_id=uid,text=aut,parse_mode=ParseMode.HTML)
    bot.sendMessage(chat_id=uid,text=con,parse_mode=ParseMode.HTML)
    # bot.sendMessage(chat_id=uid,text=aut.decode('ISO-8859-1'))#bad using
    # bot.sendMessage(chat_id=uid,text=aut.encode('utf-8'))#bad using
    # bot.sendMessage(chat_id=uid,text='<b>'+aut+'</b>',parse_mode=ParseMode.HTML)#bad using
    thread.exit_thread()


if __name__ == '__main__':
    main()
