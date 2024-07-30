import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def extract_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()
