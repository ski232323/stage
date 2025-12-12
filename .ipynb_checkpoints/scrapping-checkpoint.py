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
    for orig, corr in zip(blob.words, corrected.words):
        if orig != corr:
            errors.add((url, "EN", orig, corr))

def process_page(url):
    print(f"[🔎] Analyse : {url}")
    visited.add(url)
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        print(f"[⚠️ ERROR] {url}: {e}")
        return set()

    if "text/html" not in resp.headers.get("Content-Type", ""):
        return set()

    html = resp.text
    text = extract_text(html)
    check_french(text, url)
    check_english(text, url)

    soup = BeautifulSoup(html, "html.parser")
    links = set()
    for a in soup.find_all("a", href=True):
        href = a['href']
        if href.startswith("#"):
            continue
        full_url = urljoin(url, href)
        parsed = urlparse(full_url)
        if parsed.netloc == urlparse(BASE_URL).netloc and full_url not in visited:
            links.add(full_url)
    return links

def crawl_site(start_url):
    to_visit = set([start_url])
    while to_visit:
        current = to_visit.pop()
        new_links = process_page(current)
        to_visit.update(new_links)
        time.sleep(1)
        export_csv()

def export_csv():
    if not errors:
        return
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["url", "lang", "mot_incorrect", "suggestions"])
        for row in errors:
            writer.writerow(row)
    print(f"✔ CSV mis à jour : {OUTPUT_CSV}")

if __name__ == "__main__":
    crawl_site(BASE_URL)
    print("✔ Analyse terminée")
