#import pandas as pd

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


def contar():
    return 4

# Load in each data file (zfill pads out integers with leading zeros)
text_data = []
for index in range(22):
    filename = 'dataset/reut2-{0}.sgm'.format(str(index).zfill(3))
    with open(filename, 'r', encoding = 'utf-8', errors = 'ignore') as infile:
        text_data.append(infile.read())
# Print first 300 characters of first file
# print(text_data[0][:300])
print('/////////////////////////////////////////')


# Separate each text file into articles
articles = []
for textfile in text_data:
    # Parse text as html using beautiful soup
    parsed_text = BeautifulSoup(textfile, 'html.parser')
    # Extract article between <BODY> and </BODY> and convert to standard text. Add to list of articles
    articles += [article.get_text() for article in parsed_text.find_all('body')]
# print the first article as an example
print(articles[0])
print('/////////////////////////////////////////')

# Convert each article to all lower case
articles = [article.lower() for article in articles]
# Strip all punctuation from each article
# This uses str.translate to map all punctuation to the empty string
table = str.maketrans('', '', string.punctuation)
articles = [article.translate(table) for article in articles]
# Convert all numbers in the article to the word 'num' using regular expressions
# articles = [re.sub(r'\d+', 'num', article) for article in articles]
articles = [re.sub(r'\d+', '', article) for article in articles]

# Print the first article as a running example
print(articles[0])

print(len(articles[0].splitlines()))

# Separar el texto en lineas 

lines = articles[0].splitlines()

num_lines = len(articles[0].splitlines())
num_words = 0

for line in lines:
    num_words += len(line.split())

print('palabras: ', num_words)