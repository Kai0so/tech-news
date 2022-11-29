from ..database import search_news


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
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
