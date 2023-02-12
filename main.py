
#Імпотруємо потрібні бібліотеки

import openai
import telebot

#Токени від OpenAI API та BotFather
openai.api_key = "YOUR TOKEN"
bot = telebot.TeleBot('YOUR TOKEN')

#Запит до ChatGPT
def get_answer(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

#Скрипт
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hi, it's ChatGPT-bot")

@bot.message_handler(content_types=['text'])
def ans(message):
    user_input = message.text
    response = get_answer(user_input)
    bot.reply_to(message, response)



bot.infinity_polling()



