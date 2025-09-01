import os
import requests

API_BASE = "https://www.googleapis.com/books/v1/volumes"


class GoogleBooksError(Exception):
    pass

def fetch_books_for_title(query: str, max_results: int = 5, lang: str = "en"):
    """Search Google Books for a title and return raw items list.
    Uses API key from env if available.
    """
    if not query:
        return []

    params = {
    "q": f"intitle:{query}",
    "maxResults": max_results,
    "printType": "books",
    "langRestrict": lang,
    }

    api_key = os.getenv("GOOGLE_BOOKS_API_KEY")
    if api_key:
        params["key"] = api_key
        
    try:
        resp = requests.get(API_BASE, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json() or {}
        return data.get("items", [])
        
    except requests.RequestException as e:
        raise GoogleBooksError(str(e)) from e