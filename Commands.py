import telebot
import pymongo

bot = telebot.TeleBot("1111776586:AAEf9T0hPAcHM7If0vGdnYDAQA9PuebCxs4")
my_client = pymongo.MongoClient("mongodb+srv://Kuptuk:str38171str@cluster0-qxkw1.gcp.mongodb.net/test?retryWrites=true&w=majority")

my_database = my_client.Inf
my_collection = my_database.Inf

@bot.message_handler(commands=["streamcraft"])
def streamcraft_message(message):
    if message.from_user.id == 522487188:
        my_collection.update_one({"streamcraft":"false"},{"$set":{"streamcraft":"true"}})

bot.polling()