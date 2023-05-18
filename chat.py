import time
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from bs4 import BeautifulSoup
from docx import Document

app = Flask(__name__)

def train_chatbot():
    bot = ChatBot('myBot')
    trainer = ChatterBotCorpusTrainer(bot)
    trainer.train("chatterbot.corpus.spanish")
    return bot

def get_bot_response(bot, user_text):
    return str(bot.get_response(user_text))

def convertir_docx_a_html(ruta_archivo):
    documento = Document(ruta_archivo)
    contenido_documento = ""
    for parrafo in documento.paragraphs:
        contenido_documento += parrafo.text + "\n"
    soup = BeautifulSoup('', 'html.parser')
    for linea in contenido_documento.split('\n'):
        soup.append(soup.new_string(linea))
    contenido_html = str(soup)
    return contenido_html

@app.before_request
def medir_tiempo():
    # Código para medir el tiempo de ejecución
    start_time = time.perf_counter()
    request.start_time = start_time

@app.after_request
def imprimir_tiempo_de_ejecucion(response):
    end_time = time.perf_counter()
    execution_time = end_time - request.start_time
    print(f"Tiempo de ejecución: {execution_time} segundos")
    return response

@app.route("/")
def home():
    return render_template("Chatbot.html")

@app.route('/get_response', methods=['POST'])
def get_response():
    user_text = request.form['msg']
    bot_response = get_bot_response(bot, user_text)
    return bot_response

@app.route("/document")
def get_document():
    ruta_archivo = 'nuevo.docx'
    contenido_html = convertir_docx_a_html(ruta_archivo)
    return contenido_html

if __name__ == "__main__":
    bot = train_chatbot()
    app.run(debug=True)
