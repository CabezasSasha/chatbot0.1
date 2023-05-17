from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from docx import Document
from bs4 import BeautifulSoup
from flask import Flask, render_template, request



# Creamos el bot y lo entrenamos con los datos de corpus
bot = ChatBot('myBot')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.spanish")



# Cargamos el archivo de Word y extraemos el contenido
document = Document('puebla.docx')
text = '\n'.join([paragraph.text for paragraph in document.paragraphs])



# Parseamos el contenido como HTML y lo pasamos a la plantilla HTML
soup = BeautifulSoup(text, 'html.parser')
html_content = str(soup)



# Creamos la aplicación Flask y definimos las rutas
app = Flask(__name__)



@app.route("/")
def home():
 return render_template("Chatbot.html")



@app.route('/get_response', methods=['POST'])
def get_bot_response():
 user_text = request.args.get('msg')
 bot_response = str(bot.get_response(user_text))
 return bot_response


@app.route("/document")
def get_document():
 return html_content


if __name__ == "__main__":
 app.run(debug=True)