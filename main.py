import telebot

bot = telebot.TeleBot('5569374220:AAEoyEM5zkZBNa7QjB-rIiP-Hfs5lideIWo')


@bot.message_handler( commands=['start'] )
def greetings(message):
    user = message.from_user.username
    bot.reply_to(message, "Hey! " + str(user))


@bot.message_handler( content_types=['text'] )
def reaquestion(message):
    bot.send_message(message.chat.id, "Stay. " + message.from_user.first_name + ", did you said:" + message.text + "?")


bot.infinity_polling()
