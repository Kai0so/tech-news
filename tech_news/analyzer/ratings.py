from ..database import get_collection


# Requisito 10
def top_5_news():
    search_result = []
    news_result = (
        get_collection()
        .find()
        .sort([("comments_count", -1), ("title", 1)])
        .limit(5)
    )
    for news in news_result:
        news_data = (news["title"], news["url"])
        search_result.append(news_data)
    return search_result


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
