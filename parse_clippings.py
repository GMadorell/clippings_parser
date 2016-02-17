import codecs
from clippings_parser import fetch_clippings_from_file


FILE_PATH = "My Clippings.txt"
BOOK_TITLE = "YourBookTitle"


def main():
    # print fetch_distinct_book_titles()
    for clip in fetch_interesting_clips():
        print clip.content


def fetch_distinct_book_titles():
    book_titles = set()
    for clip in fetch_all_clippings():
        book_titles.add(clip.title)
    return book_titles


def fetch_interesting_clips():
    for clip in fetch_all_clippings():
        if clip.title.lower() == BOOK_TITLE.lower():
            yield clip


def fetch_all_clippings():
    with codecs.open(FILE_PATH, 'r', 'utf-8') as clippings_file:
        for clip in fetch_clippings_from_file(clippings_file):
            yield clip


if __name__ == "__main__":
    main()

