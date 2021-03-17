from telegram.ext import Updater, CommandHandler

def start (update, context):
	update.message.reply_text('hola walter clavo')

if __name__=='__main__':

	updater = Updater(token='1655048016:AAFkysh83LjUHD47yEDclBupy0TXpcZ4r1s', use_context='True')

	dp = updater.dispatcher
	dp.add_handler(CommandHandler ('start', start))

	updater.start_polling()
	updater.idle()
