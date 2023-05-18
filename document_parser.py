from docx import Document
from bs4 import BeautifulSoup

def parse_document(file_path):
    #Abrir el archivo .docx
    document = Document(file_path)
    # Extraer el texto del archivo .docx
    text = ""
    for paragraph in document.paragraphs:
        text+=paragraph.text + "\n"
   

def convert_to_html(text):
    soup = BeautifulSoup(text, 'html.parser')
    html_content = str(soup)
    return html_content
