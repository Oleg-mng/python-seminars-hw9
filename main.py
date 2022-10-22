from pytube import YouTube
from telebot import *

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

yt = YouTube('https://youtu.be/HJv4L3Adnq8')
yt.title
print (yt.title)

bot=telebot.Telebot("5704098294:AAH55qwRk3jiWwbRedBpuorImDl9PUqFqJ4")

@bot.message_handler(commands=['start'])
def start(message):
    mess=f'Привет{message.from_user.first_name} {message.from_user.last_name}'
    bot.send.message(message.chat.id, mess, parse_mode='html')

print('server start')
bot.polling(none_stop=True)

# app = ApplicationBuilder().token("5669734316:AAEIJmjS96UI5r6JuNKSjhg3Hg6QT-NxGpQ").build()

# app.add_handler(CommandHandler("hi", hi_comand))
# app.add_handler(CommandHandler("link", link_comand))
# app.add_handler(CommandHandler("quality video", quality_comand))
# app.add_handler(CommandHandler("download video", download_comand))


# app.run_polling()

# qua = input('Выберите качество видео для скачивания 360/720/1080: ')
# if qua == '360':
#     stream = yt.streams.get_by_itag(18)
#     stream.download()
# elif qua == '720':
#     stream = yt.streams.get_by_itag(22)
#     stream.download()
# elif qua == '1080':
#     stream = yt.streams.get_by_itag(137)
#     stream.download()


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hi {update.effective_user.first_name}!')


# stream = yt.streams.get_by_itag(22)
# stream.download()