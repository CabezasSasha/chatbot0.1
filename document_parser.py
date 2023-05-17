from docx import Document
from bs4 import BeautifulSoup

def parse_document(file_path):
    document = Document(file_path)
    text = '\n'.join([paragraph.text for paragraph in document.paragraphs])
    return text

def convert_to_html(text):
    soup = BeautifulSoup(text, 'html.parser')
    html_content = str(soup)
    return html_content
