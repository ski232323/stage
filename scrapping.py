import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from spellchecker import SpellChecker
from textblob import TextBlob
import csv
import time

BASE_URL = "https://staging-www2.quantilia.com/"
OUTPUT_CSV = "rapport_orthographe.csv"
visited = set()
errors = set()
spell_fr = SpellChecker(language='fr')

def extract_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup(["script", "style", "noscript"]):
        tag.extract()
    return " ".join(soup.get_text(" ").split())

def check_french(text, url):
    words = text.split()
    misspelled = spell_fr.unknown(words)
    for word in misspelled:
        suggestion = spell_fr.candidates(word)
        errors.add((url, "FR", word, ", ".join(list(suggestion)[:5])))

def check_english(text, url):
    blob = TextBlob(text)
    corrected = blob.correct()
    for orig, corr in zip(blob.words, c
