from bs4 import BeautifulSoup
from docx import Document
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from bot import train_chatbot, get_bot_response
from document_parser import parse_document, convert_to_html

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

# Ruta del archivo .docx
ruta_archivo = 'nuevo.docx'

# Convertir el archivo .docx a HTML
contenido_html = convertir_docx_a_html(ruta_archivo)

# Imprimir el contenido HTML resultante
print(contenido_html)

        
  # Obtener el HTML generado
def convert_to_html(text):
    soup = BeautifulSoup(text, 'html.parser')
    html_content = str(soup)
    return html_content


app = Flask(__name__)

bot = train_chatbot()

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
  # Ruta del archivo .docx
    ruta_archivo = 'nuevo.docx'
    document_text = parse_document(ruta_archivo)
    html_content = convert_to_html(document_text)
    return html_content



if __name__ == "__main__":
     app.run(debug=True)
