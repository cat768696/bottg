import os
import telebot

bot = telebot.TeleBot(os.environ["BOT_TOKEN"])

@bot.message_handler(commands=["start"])
def start(m):
    bot.reply_to(m, "Привет! Я твой первый бот 🤖")

@bot.message_handler(func=lambda m: True)
def echo(m):
    bot.reply_to(m, "Ты написал: " + m.text)

bot.infinity_polling()

