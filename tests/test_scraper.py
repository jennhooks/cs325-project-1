import pytest
import os
from bs4 import BeautifulSoup
from scraper import EbayScraper, scrape_reviews_ebay

# Test the parsing code on a local copy of a webpage.
def test_ebay_mock_get_page_urls():
    expected = [
        'https://www.ebay.com/urw/Available-Titles-CengageNOW-Ser-Calculus-Early-Transcendentals-by-James-Stewart-2002-Hardcover-/product-reviews/2408624?_itm=266964871059&pgn=1',
        'https://www.ebay.com/urw/Available-Titles-CengageNOW-Ser-Calculus-Early-Transcendentals-by-James-Stewart-2002-Hardcover-/product-reviews/2408624?_itm=266964871059&pgn=2',
        'https://www.ebay.com/urw/Available-Titles-CengageNOW-Ser-Calculus-Early-Transcendentals-by-James-Stewart-2002-Hardcover-/product-reviews/2408624?_itm=266964871059&pgn=3',
        'https://www.ebay.com/urw/Available-Titles-CengageNOW-Ser-Calculus-Early-Transcendentals-by-James-Stewart-2002-Hardcover-/product-reviews/2408624?_itm=266964871059&pgn=4',
        ]
    mock_path = os.path.join('tests', 'ebay_mock.html')
    scraper = EbayScraper(mock_path)
    with open(mock_path, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        result = scraper.get_page_urls(soup)
        assert result == expected

def test_ebay_mock_get_reviews_from_page():
    expected = []
    mock_reviews = os.path.join('tests', 'ebay_mock_reviews.txt')
    with open(mock_reviews, 'r') as file:
        for line in file:
            expected.append(line.rstrip())
    mock_path = os.path.join('tests', 'ebay_mock.html')
    scraper = EbayScraper(mock_path)
    with open(mock_path, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        result = scraper.get_reviews_from_page(soup)
        assert result == expected

# Test the module on real data.
def test_ebay_real_get_reviews():
    expected = []
    real_reviews = os.path.join('tests', 'ebay_real_reviews.txt')
    with open(real_reviews, 'r') as file:
        for line in file:
            expected.append(line.rstrip())

    scraper = EbayScraper('https://www.ebay.com/urw/Available-Titles-CengageNOW-Ser-Calculus-Early-Transcendentals-by-James-Stewart-2002-Hardcover-/product-reviews/2408624?_itm=266964871059&pgn=1')
    result = scraper.get_reviews()
    assert result == expected

def test_real_scrape_reviews_ebay(tmp_path):
    expected = []
    real_reviews = os.path.join('tests', 'ebay_real_reviews.txt')
    with open(real_reviews, 'r') as file:
        for line in file:
            expected.append(line.rstrip())

    input_file = tmp_path / 'input.txt'
    with open(input_file, 'w') as file:
        file.write('https://www.ebay.com/urw/Available-Titles-CengageNOW-Ser-Calculus-Early-Transcendentals-by-James-Stewart-2002-Hardcover-/product-reviews/2408624?_itm=266964871059&pgn=1')
        file.write('\n')
    versions = ['5th edition']

    results = scrape_reviews_ebay(input_file, versions)
