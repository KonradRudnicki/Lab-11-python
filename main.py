import re
import urllib

import content as content
# from turtle import pd
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
from collections import Counter
import matplotlib.pyplot as plt
import os
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from exceptions.PictureNotFoundError import PictureNotFoundError


# part 1
def download_book(book_id):
    url = f"https://www.gutenberg.org/cache/epub/{book_id}/pg{book_id}-images.html"
    response = requests.get(url)

    return response.text


# part 2
def parse_book(html):
    soup = BeautifulSoup(html, 'html.parser')

    p_tags_container = soup.select("div.container p")
    title = p_tags_container[0].text.split(": ")[1]
    author = p_tags_container[1].text.split(": ")[1]

    class_chapters = soup.select(".chapter")
    first_chapter = class_chapters[5].text
    print(type(first_chapter))
    return title, author, class_chapters


def round_to_ten(n):
    return int(round(n // 10.0) * 10)


def count_words(chapter_no):
    words_count = []
    paragraphs = chapter_no.find_all('p')
    paragraphs_text = [p.get_text() for p in paragraphs]

    for paragraph in paragraphs_text:
        words_count.append(round_to_ten(len(paragraph.split())))

    words_count = sorted(words_count)
    counter = Counter(words_count)

    for count, num_paragraphs in counter.items():
        if num_paragraphs > 1:
            print(f"There are {num_paragraphs} paragraphs with {count} words.")

    x_values = list(counter.keys())
    y_values = list(counter.values())

    plt.bar(x_values, y_values)
    plt.xlabel('Word Counts (rounded to nearest 10)')
    plt.ylabel('Number of Paragraphs')
    plt.title('Distribution of Paragraph Lengths in Chapter')
    plt.show()

    return words_count


# part 4

def get_picture_source(content, book_id):

    soup = BeautifulSoup(content, 'html.parser')

    images = soup.select("img")

    if images:
        try:
            source = images[0]["src"]
        except TypeError:
            raise PictureNotFoundError()
        source_url = f"https://www.gutenberg.org/cache/epub/{book_id}/{source}"
    else:
        # Original picture not found, return None
        return None

    return source_url


def download_picture(url, image_path):
    if url is None:
        # Original picture not found, create a white image
        black_image = Image.new("RGB", (1000, 1000), color="white")
        black_image.save(image_path)
    else:
        urllib.request.urlretrieve(url, image_path)

def edit_image(input_filename, output_filename):
    # Open the image file
    img = Image.open(input_filename)

    # Define the area for cropping (left, upper, right, lower)
    crop_area = (50, 50, 300, 300)  # Replace these values as needed

    # Crop the image
    cropped_img = img.crop(crop_area)

    # Define the size for resizing
    resize_size = (500, 500)  # Replace these values as needed

    # Resize the image
    resized_img = cropped_img.resize(resize_size)

    # Load a font (provide the full path to the .ttf file)
    font = ImageFont.truetype('arial.ttf', 15)

    # Get an image drawing interface
    d = ImageDraw.Draw(resized_img)

    # Define the position for the watermark (x, y from the bottom left corner)
    watermark_position = (10, resized_img.height - 20)  # The second value might need adjustment based on the font size

    # Add the watermark
    d.text(watermark_position, "Downloaded from Project Gutenberg", fill=(255, 255, 255), font=font)

    # Save the image
    resized_img.save(output_filename)

if __name__ == '__main__':
    book_id = input('Enter a book id: ')
    html = download_book(book_id)
    # print(html)
    title, author, class_chapters = parse_book(html)
    count_words(class_chapters[5])


    picture_url = get_picture_source(html, book_id)
    image_path = 'resources/first_photo.jpg'
    download_picture(picture_url, image_path)

    edit_image('resources/first_photo.jpg', 'resources/first_photo_edited.jpg')