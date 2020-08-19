
from app import app
from flask import jsonify, request
# from app.wor.py import contar
# from .wor.py import contar

# Text datasets
from bs4 import BeautifulSoup
import nltk
import sklearn
import re
import string
# For downloading and importing data
import os
import urllib
import itertools
import tarfile


@app.route('/')
@app.route('/index')
def index():
    # return "Hello, World!"
    return jsonify({"message": "Hello World!"})


#Servicio para contar las palabras en un archivo 
@app.route("/contpalabras")
def contpalabras():

    nombArch = ''
    estado = 'OK'
    conteo = 0
    try:
        nombArc = request.args.get('archivo')      
    except:
        estado = 'ER'
    # print(contar())
    if estado != 'ER':
        conteo = contar(nombArc)

    return jsonify(nombArc = nombArc,
                    estado = estado,
                    conteo = conteo)


@app.route("/archivo")
def selarchivo():
    # try:
    try:
        nombArc = request.args.get('archivo')      
    except:
        return 'ER'
    # print(contar())
    return jsonify(contar())


def contar(nomb):
    if not nomb:
        return 'ER ingrese nombre archivo'
    # Load in each data file (zfill pads out integers with leading zeros)
    text_data = []
    filename = 'dataset/'+nomb.format(str(index).zfill(3))
    try:
        with open(filename, 'r', encoding = 'utf-8', errors = 'ignore') as infile:
            text_data.append(infile.read())
    except:
        return 'ER nomb archivo no existe'
    
    articles = []
    # Parse text as html using beautiful soup
    parsed_text = BeautifulSoup(text_data[0], 'html.parser')
    # Extract article between <BODY> and </BODY> and convert to standard text. Add to list of articles
    articles += [article.get_text() for article in parsed_text.find_all('body')]
    
    # This uses str.translate to map all punctuation to the empty string
    table = str.maketrans('', '', string.punctuation)
    articles = [article.translate(table) for article in articles]

    # Convert all numbers in the article to the word 'num' using regular expressions
    articles = [re.sub(r'\d+', '', article) for article in articles]

    # Separar el texto en lineas 
    lines = articles[0].splitlines()
    num_lines = len(articles[0].splitlines())
    
    num_words = 0
    for line in lines:
        num_words += len(line.split())

    return num_words

# reut2-000.sgm
def loadArc(nomb):
    if not nomb:
        return 'ER ingrese nombre archivo'
    # Load in each data file (zfill pads out integers with leading zeros)
    text_data = []
    filename = 'dataset/'+nomb.format(str(index).zfill(3))
    try:
        with open(filename, 'r', encoding = 'utf-8', errors = 'ignore') as infile:
            text_data.append(infile.read())
    except:
        return 'ER nomb archivo no existe'
    return text_data[0][:200]
# Print first 300 characters of first file
# print(text_data[0][:300])


# if __name__ == '__main__':
#      # Iniciamos la apicación en modo debug
#  app.run(debug=True)

#Funciones del worker
