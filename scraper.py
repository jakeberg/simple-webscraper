#!/usr/bin/env python2

import re
import sys
import requests
import argparse
from bs4 import BeautifulSoup


def find_urls(webpage_text):
    """Finds all urls"""
    u = []
    soup = BeautifulSoup(webpage_text.text, 'html.parser')
    for link in soup.find_all('a'):
        address = link.get('href')
        url = re.search(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", str(address))
        if url:
            u.append(url.group())
    return u


def find_imgs(webpage_text):
    """Finds all urls"""
    s = []
    soup = BeautifulSoup(webpage_text.text, 'html.parser')
    for img in soup.find_all('img'):
        src = img.get('src')
        s.append(src)
    return s


def find_emails(webpage_text):
    """Finds all emails"""
    e = []
    text = webpage_text.text
    emails = re.findall(r"([a-zA-Z]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.][a-zA-Z]+)", text)
    for email in emails:
        e.append(email)
    return e


def find_phones(webpage_text):
    """Finds all phone numbers"""
    p = []
    text = webpage_text.text
    phones = re.findall(r"1?\W*([2-9][0-8][0-9])\W*([2-9][0-9]{2})\W*([0-9]{4})(\se?x?t?(\d*))?", text)
    for phone in phones:
        p.append(phone)
    return p


def create_parser():
    """Creates an argument parser object"""
    parser = argparse.ArgumentParser()
    parser.add_argument('webpage',
                        help='webpage that will be passed through scraper')
    return parser


def main(args):
    """Parse args, scrape webpage, scan with regex"""
    parser = create_parser()

    if not args:
        parser.print_usage()
        sys.exit(1)

    parsed_args = parser.parse_args(args)

    webpage_text = requests.get(parsed_args.webpage)

    # PRINTS OUT URLS
    print"""
    URLs:

    """
    found_urls = find_urls(webpage_text)
    for url in found_urls:
        print(url)

    # PRINTS OUT IMGS
    print"""
    IMGs:

    """
    found_imgs = find_imgs(webpage_text)
    for img in found_imgs:
        print(img)

    # PRINTS OUT EMAILS
    print"""
    Emails:

    """
    found_emails = find_emails(webpage_text)
    for email in found_emails:
        print(email)

    # PRINTS OUT PHONE NUMBERS
    print"""
    Phone Numbers:

    """
    found_phones = find_phones(webpage_text)
    for phone in found_phones:
        print phone[0] + "-" + phone[1] + "-" + phone[2]


if __name__ == '__main__':
    main(sys.argv[1:])
