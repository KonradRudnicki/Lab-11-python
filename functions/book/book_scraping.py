import requests
from bs4 import BeautifulSoup
from classes.Book import Book


# part 1
def download_book(book_id):
    url = f"https://www.gutenberg.org/cache/epub/{book_id}/pg{book_id}-images.html"
    response = requests.get(url)
    return response.text


# part 2
def parse_book(book_id) -> Book:
    html = download_book(book_id)
    soup = BeautifulSoup(html, 'html.parser')

    p_tags_container = soup.select("div.container p")
    title = p_tags_container[0].text.split(": ")[1]
    author = p_tags_container[1].text.split(": ")[1]

    class_chapters = soup.select(".chapter")
    first_chapter = class_chapters[5].text

    return Book(book_id, soup, title, author, class_chapters, first_chapter)