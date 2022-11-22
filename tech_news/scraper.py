import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
    except requests.ReadTimeout:
        return None
    else:
        if response.status_code == 200:
            return response.text
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    titles = selector.css("h2.entry-title a::attr(href)").getall()
    if titles:
        return titles
    return []


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css("div.nav-links a.next::attr(href)").get()
    if next_page:
        return next_page
    return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
