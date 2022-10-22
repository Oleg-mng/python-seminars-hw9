from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_comands import *
from spy import *

# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

app = ApplicationBuilder().token("5669734316:AAEIJmjS96UI5r6JuNKSjhg3Hg6QT-NxGpQ").build()

app.add_handler(CommandHandler("hi", hi_comand))
app.add_handler(CommandHandler("time", time_comand))
app.add_handler(CommandHandler("help", help_comand))
app.add_handler(CommandHandler("sum", sum_comand))

print('server start')
app.run_polling()

# import matplotlib.pyplot as plt
# import numpy as np

# list=[1,2,3,8,5,15, 3, 89]
# plt.plot(list)
# plt.show()


# Fixing random state for reproducibility
# np.random.seed(19680801)


# plt.rcdefaults()
# fig, ax = plt.subplots()

# Example data
# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))

# ax.barh(y_pos, performance, xerr=error, align='center')
# ax.set_yticks(y_pos, labels=people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')

# plt.show()


# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))
# # Python is 👍
# print(emoji.emojize('Python is :thumbsup:', language='alias'))
# # Python is 👍
# print(emoji.demojize('Python is 👍'))
# # Python is :thumbs_up:
# print(emoji.emojize("Python is fun :red_heart:"))
# # Python is fun ❤
# print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
# # Python is fun ❤️ #red heart, not black heart
# print(emoji.is_emoji("👍"))
# # True



# from progress.bar import Bar
# import time
# bar = Bar('Processing', max=20)
# for i in range(20):
#     # Do some work
#     time.sleep(0.5)
#     bar.next()
# bar.finish()



# from isOdd import isOdd

# print(isOdd(1))
# print(isOdd(54)) 

