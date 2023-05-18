from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def train_chatbot():
    bot = ChatBot('myBot')
    trainer = ChatterBotCorpusTrainer(bot)
    trainer.train("chatterbot.corpus.spanish")
    return bot

def get_bot_response(bot, user_text):
    return str(bot.get_response(user_text))




