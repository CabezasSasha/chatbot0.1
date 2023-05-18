from bs4 import BeautifulSoup
from docx import Document
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
import pytz
from datetime import datetime

app = Flask(__name__)
# Obtener la fecha y hora actual en la zona horaria de Argentina
timezone = pytz.timezone('America/Argentina/Buenos_Aires')
current_time = datetime.now(timezone)

# Imprimir la fecha y hora actual
print(current_time)

def train_chatbot():
    bot = ChatBot('myBot')
    trainer = ChatterBotCorpusTrainer(bot)
    trainer.train("chatterbot.corpus.spanish")
    return bot

def get_bot_response(bot, user_text):
    return str(bot.get_response(user_text))

def convertir_docx_a_html(ruta_archivo):
    # Abrir el archivo .docx
    documento = Document(ruta_archivo)

    # Obtener el contenido del documento como texto
    contenido_documento = ""
    for parrafo in documento.paragraphs:
        contenido_documento += parrafo.text + "\n"

    # Crear un objeto BeautifulSoup para el contenido HTML
    soup = BeautifulSoup('', 'html.parser')

    # Agregar el contenido del documento al objeto BeautifulSoup
    for linea in contenido_documento.split('\n'):
        soup.append(soup.new_string(linea))

    # Obtener el HTML generado
    contenido_html = str(soup)

    return contenido_html

@app.route("/")
def home():
    start_time = time.perf_counter()  # Inicio del tiempo de ejecución
    # Resto del código para renderizar el template "Chatbot.html"
    end_time = time.perf_counter()  # Fin del tiempo de ejecución
    execution_time = end_time - start_time
    print(f"Tiempo de ejecución: {execution_time} segundos")
    return render_template("Chatbot.html")

@app.route('/get_response', methods=['POST'])
def get_response():
    user_text = request.form['msg']
    bot_response = get_bot_response(bot, user_text)
    return bot_response

@app.route("/document")
def get_document():
    # Ruta del archivo .docx
    ruta_archivo = 'nuevo.docx'
    contenido_html = convertir_docx_a_html(ruta_archivo)
    return contenido_html

if __name__ == "__main__":
    bot = train_chatbot()
    app.run(debug=True)

