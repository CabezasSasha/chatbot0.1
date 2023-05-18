from docx import Document
from bs4 import BeautifulSoup

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