import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
def scrape_novidades(fetch_response):
    selector = Selector(fetch_response)
    titles = selector.css("h2.entry-title a::attr(href)").getall()
    if titles:
        return titles
    return []


# Requisito 3
def scrape_next_page_link(fetch_response):
    selector = Selector(fetch_response)
    next_page = selector.css("div.nav-links a.next::attr(href)").get()
    if next_page:
        return next_page
    return None


# Requisito 4
def scrape_noticia(fetch_response):
    selector = Selector(fetch_response)
    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get().strip()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("span.author a::text").get()
    comments_count = selector.css("div.post-comments h5::text").get(default=0)
    summary_selector = selector.css(
        "div.entry-content > p:first-of-type *::text"
    ).getall()
    summary = "".join(summary_selector).strip()
    tags = selector.css("section.post-tags a::text").getall()
    category = selector.css("span.label::text").get()
    dictionary = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }
    return dictionary


# Requisito 5
def get_tech_news(amount):
    URL_BASE = "https://blog.betrybe.com/"
    news_data = []
    while len(news_data) < amount:
        base_url_response = fetch(URL_BASE)
        news_url = scrape_novidades(base_url_response)
        for news in news_url:
            if len(news_data) < amount:
                news_url_response = fetch(news)
                data = scrape_noticia(news_url_response)
                news_data.append(data)
        URL_BASE = scrape_next_page_link(base_url_response)
    create_news(news_data)
    return news_data
