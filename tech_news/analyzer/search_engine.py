from ..database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    search_result = []
    try:
        news_result = search_news(query)
    except FileNotFoundError:
        return []
    else:
        for news in news_result:
            news_data = (news["title"], news["url"])
            search_result.append(news_data)
        return search_result


# Requisito 7
def search_by_date(date):
    try:
        formated_date = datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )
        query = {"timestamp": formated_date}
        search_result = []
        news_result = search_news(query)
    except Exception:
        raise ValueError("Data inválida")
    else:
        for news in news_result:
            news_data = (news["title"], news["url"])
            search_result.append(news_data)
        return search_result


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
