from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hi_comand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

async def link_comand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

async def quality_comand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Выберите качество видео для скачивания 360/720/1080: ')
    qua = input('Выберите качество видео для скачивания 360/720/1080: ')
   
async def download_comand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Выберите качество видео для скачивания 360/720/1080: ')
    qua = input('Выберите качество видео для скачивания 360/720/1080: ')
    if qua == '360':
        stream = yt.streams.get_by_itag(18)
        stream.download()
    elif qua == '720':
        stream = yt.streams.get_by_itag(22)
        stream.download()
    elif qua == '1080':
        stream = yt.streams.get_by_itag(137)
        stream.download()


@bot.message_handler(commands=['some_command'])
def send_message(message):
        bot.send_message(message.chat.id, 'Выберите качество видео для скачивания 360/720/1080: ')
        text = message.text

from uuid import uuid4
from telegram.ext import Application, CommandHandler

async def put(update, context): # асинхронная функция
    key = str(uuid4())
    value = update.message.text.partition(' ')[2]
    # операция не связана с сетевым подключением
    context.user_data[key] = value
    # операция связана с сетевым подключением
    # добавляем оператор `await`
    await update.message.reply_text(key)

async def get(update, context): # асинхронная функция
    key = context.args[0]
    value = context.user_data.get(key, 'Not found')
    # операция связана с сетевым подключением
    # добавляем оператор `await`
    await update.message.reply_text(value)

if __name__ == '__main__':
    # экземпляр приложения создается по новому
    application = Application.builder().token('TOKEN').build()
    application.add_handler(CommandHandler('put', put))
    application.add_handler(CommandHandler('get', get))
    application.run_polling()