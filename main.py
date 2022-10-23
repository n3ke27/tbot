import telebot
import sqlite3

bot = telebot.TeleBot('5569374220:AAEoyEM5zkZBNa7QjB-rIiP-Hfs5lideIWo')
conn = sqlite3.connect('stats.db', check_same_thread=False)
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   nickname TEXT,
   class INT);
""")
conn.commit()


@bot.message_handler(commands=['start'])
def greetings(message):
    user = message.from_user.username
    user_info = (message.from_user.id, user, '10')
    bot.reply_to(message, "Hi! " + user)
    cur.execute("INSERT INTO users VALUES(?, ?, ?)", user_info)
    conn.commit()
    stri = "SELECT * FROM users WHERE userid="+str(message.from_user.id)
    cur.execute(stri)
    bot.send_message(message.chat.id, str(cur.fetchone()))


@bot.message_handler(content_types=['text'])
def reacquisition(message):
    bot.send_message(message.chat.id, "Stay. " + message.from_user.first_name + ", did you said:" + message.text + "?")


bot.infinity_polling()
