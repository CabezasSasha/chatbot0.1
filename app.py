from flask import Flask, render_template, request
from bot import train_chatbot, get_bot_response
from document_parser import parse_document, convert_to_html

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
    file_path = 'nuevo.docx'
    document_text = parse_document(file_path)
    html_content = convert_to_html(document_text)
    return html_content

# Obtener la respuesta del chatbot
user_input = input("Usuario: ")
bot_response = bot.get_response(user_input)
print("Bot: ", bot_response)

if __name__ == "__main__":
    app.run(debug=True)
