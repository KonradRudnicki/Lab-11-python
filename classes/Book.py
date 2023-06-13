from dataclasses import dataclass
from bs4 import BeautifulSoup

@dataclass
class Book:
    id: str
    content: BeautifulSoup
    title: str
    author: str
    chapters: list
    first_chapter: str