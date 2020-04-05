import telebot
import pymongo
import os

mm = os.environ.get("Mongo")
tt = os.environ.get("TOKEN")
my_client = pymongo.MongoClient(mm)
bot = telebot.TeleBot(tt)

my_database = my_client.Inf
my_collection = my_database.Inf

@bot.message_handler(commands=["streamcraft"])
def streamcraft_message(message):
    if message.from_user.id == 522487188:
        my_collection.update_one({"streamcraft":"false"},{"$set":{"streamcraft":"true"}})
        
@bot.message_handler(commands=["gmail"])
def gmail_message(message):
    if message.from_user.id == 522487188:
        my_collection.update_one({"gmail":"false"},{"$set":{"gmail":"true"}})

bot.polling()
