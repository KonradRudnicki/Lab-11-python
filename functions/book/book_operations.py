import re
from collections import Counter
import matplotlib.pyplot as plt


def round_to_ten(n):
    return int(round(n // 10.0) * 10)


def count_words(chapter_no):

    words_count = []
    paragraphs = chapter_no.find_all('p')
    paragraphs_text = [p.get_text() for p in paragraphs]

    for paragraph in paragraphs_text:
        if round_to_ten(len(paragraph.split())) != 0:
            words_count.append(round_to_ten(len(paragraph.split())))

    words_count = sorted(words_count)


    # for count, num_paragraphs in counter.items():
    #     if num_paragraphs > 1:
    #         print(f"There are {num_paragraphs} paragraphs with {count} words.")

    # x_values = list(counter.keys())
    # y_values = list(counter.values())
    #  counter = Counter(words_count)
    #
    #
    # plt.bar(x_values, y_values)
    # plt.xlabel('Word Counts (rounded to nearest 10)')
    # plt.ylabel('Number of Paragraphs')
    # plt.title('Distribution of Paragraph Lengths in Chapter')
    #plt.show()

    return words_count