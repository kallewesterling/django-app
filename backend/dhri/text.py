# General text tools
import re
from django.utils.text import slugify
from backend.dhri.constants import get_regex


def get_urls(markdown: str) -> list:
    """ Returns a list of URLs in a given string """
    g = re.findall(get_regex('COMPLEX_SEARCH_FOR_URLS'),
                   markdown)  # used to be MARKDOWN_HREF (but that's included in COMPLEX_SEARCH_FOR_URLS now)
    return(list(set([x[0] for x in g if x[0]])))


def get_markdown_hrefs(markdown: str) -> list:
    """ Returns a list of URLs in a given string """
    g = re.findall(
        get_regex('MARKDOWN_HREF'), markdown)  # used to be  (but that's included in COMPLEX_SEARCH_FOR_URLS now)
    return(list(set([x for x in g if x])))  # returns unique


def get_number(markdown: str) -> int:
    """ Finds the first number that occurs in a markdown string and
    returns it as integer (removes any decimals for doubles) """
    g = re.search(get_regex('NUMBERS'), markdown)
    if g:
        if '.' in g.groups()[0]:
            return g.groups()[0].split('.')[0]
        else:
            return g.groups()[0]
    return 0


def dhri_slugify(string: str) -> str:
    # first replace any non-OK characters [/] with space
    string = re.sub(r'[\/\-\–\—\_]', ' ', string)

    # then replace too many spaces with one space
    string = re.sub(r'\s+', ' ', string)

    # then replace space with -
    string = re.sub(r'\s', '-', string)


    # then replace any characters that are not in ALLOWED charset with nothing
    string = re.sub(r'[^a-zA-Z\-\s]', '', string)

    # finally, use Django's slugify
    string = slugify(string)

    return string
