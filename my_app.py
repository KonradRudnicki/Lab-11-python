from hydra import compose, initialize

from functions.book.book_operations import count_words
from functions.book.book_scraping import parse_book
from functions.book.photo_download import *
from functions.report.docx_generator import create_report


def run():

    with initialize(version_base=None, config_path="config"):
        cfg = compose(config_name="config.yaml")

    book = parse_book(cfg.params.book_id)
    count_words(book.chapters[5])

    picture_url = get_picture_source(book.content, cfg.params.book_id)
    download_picture(picture_url, cfg.picture.path)
    edit_image(cfg.picture.path, cfg.picture.path_edited)

    create_report(book,cfg)

if __name__ == '__main__':
    run()