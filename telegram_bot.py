from telegram.ext import Updater,CommandHandler,MessageHandler,Filters   
from Adafruit_IO import Client,Data


ADAFRUIT_IO_USERNAME = 'nik12345'   

ADAFRUIT_IO_KEY = 'aio_zXnS03LQ4NLOQh6iQxSVpbRBC3P4'
TOKEN = '1470039508:AAEVehZG4wQFcm0JtA2uExdr6pSf0nKI-fI'
aio = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)

def turnoff(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Light turned off")
  context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://www.pepperfry.com/black-steel-picture-light-by-cocovey-1791427.html?type=rel&from=vip3&type1=similar&from1=1791433')
  send_value(0)
def turnon(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Light turned on")
  context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://www.pepperfry.com/black-steel-picture-light-by-cocovey-1791427.html?type=rel&from=vip3&type1=similar&from1=1791433&pos=1:1&total_result=4')
  send_value(1)

def send_value(value):
  feed = aio.feeds('light')
  aio.send_data(feed.key,value)

def input_message(update, context):
  text=update.message.text
  if text == 'turn on':
   turnon(update, context)

  elif text == 'turn off':
    turnoff(update, context)


def start(update,context):
  start_message='''
/turnoff :To turn OFF the Light
/turnon :To turn ON the Light
'''
  context.bot.send_message(chat_id=update.effective_chat.id, text=start_message)


updater=Updater(TOKEN,use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('turnoff',turnoff))
dispatcher.add_handler(CommandHandler('turnon',turnon))
dispatcher.add_handler(CommandHandler('start',start))
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command),input_message))
updater.start_polling()
updater.idle()
