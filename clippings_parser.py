from collections import namedtuple

import regex


title_line_re = regex.compile(r"(.*) (?|\((.*)\)|\- (.*))")

noises = [
    "\xef\xbb\xbf",
    "\xe2\x80\x94",
    "\xc2\xa0",
]

Clip = namedtuple("Clip", ["author", "title", "content"])


def fetch_clippings_from_file(clippings_file):
    yield fetch_clip_from_file(clippings_file)
    while True:
        _ = next(clippings_file)
        yield fetch_clip_from_file(clippings_file)


def fetch_clip_from_file(clippings_file):
    title_line = clean(next(clippings_file))
    title_search = regex.search(title_line_re, title_line)
    title = title_search.group(1)
    author = title_search.group(2)

    highlight_description_line = clean(next(clippings_file))
    empty_line = next(clippings_file)
    content = clean(next(clippings_file))

    return Clip(author, title, content)


def clean(string):
    utf_string = unicode(string).encode("utf-8")
    clean_string = utf_string
    for noise in noises:
        clean_string = clean_string.replace(noise, "")

    return clean_string


