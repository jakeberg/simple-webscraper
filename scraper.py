#!/usr/bin/env python2

import re
import sys
import requests
import argparse
import urllib2
from bs4 import BeautifulSoup


def web_scraper(webpage):
    r = requests.get(webpage)
    soup = BeautifulSoup(r.text, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))
    # return soup.prettify()


def find_urls(webpage_text):
    """Finds all urls"""
    u = []
    urls = re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", webpage_text)
    for url in urls:
        u.append(url)
    return u


def find_emails(webpage_text):
    """Finds all emails"""
    e = []
    emails = re.findall(r"([a-zA-Z]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.][a-zA-Z]+)", webpage_text)
    for email in emails:
        e.append(email)
    return e


def find_phones(webpage_text):
    """Finds all phone numbers"""
    p = []

    phones = re.findall(r"1?\W*([2-9][0-8][0-9])\W*([2-9][0-9]{2})\W*([0-9]{4})(\se?x?t?(\d*))?", webpage_text)
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

    webpage_text = web_scraper(parsed_args.webpage)
    # print web_scraper

    # print"""
    # URLs:

    # """
    # found_urls = find_urls(webpage_text)
    # for url in found_urls:
    #     print(url)

    # print"""
    # Emails:

    # """
    # found_emails = find_emails(webpage_text)
    # for email in found_emails:
    #     print(email)

    # print"""
    # Phone Numbers:

    # """
    # found_phones = find_phones(webpage_text)
    # for phone in found_phones:
    #     print phone[0] + "-" + phone[1] + "-" + phone[2]


if __name__ == '__main__':
    main(sys.argv[1:])
