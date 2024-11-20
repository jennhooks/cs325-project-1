import pytest
from bs4 import BeautifulSoup
from scraper import EbayScraper

# Test the parsing code on a local copy of a webpage.
def test_ebay_mock_get_page_urls():
    expected = [
        'https://www.ebay.com/urw/Available-Titles-CengageNOW-Ser-Calculus-Early-Transcendentals-by-James-Stewart-2002-Hardcover-/product-reviews/2408624?_itm=266964871059&pgn=1',
        'https://www.ebay.com/urw/Available-Titles-CengageNOW-Ser-Calculus-Early-Transcendentals-by-James-Stewart-2002-Hardcover-/product-reviews/2408624?_itm=266964871059&pgn=2',
        'https://www.ebay.com/urw/Available-Titles-CengageNOW-Ser-Calculus-Early-Transcendentals-by-James-Stewart-2002-Hardcover-/product-reviews/2408624?_itm=266964871059&pgn=3',
        'https://www.ebay.com/urw/Available-Titles-CengageNOW-Ser-Calculus-Early-Transcendentals-by-James-Stewart-2002-Hardcover-/product-reviews/2408624?_itm=266964871059&pgn=4',
        ]
    scraper = EbayScraper('tests/ebay_mock.html')
    with open('tests/ebay_mock.html', 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        result = scraper.get_page_urls(soup)
        assert result == expected

def test_ebay_mock_get_reviews_from_page():
    expected = []
    with open('tests/ebay_mock_reviews.txt', 'r') as file:
        for line in file:
            expected.append(line.rstrip())
    scraper = EbayScraper('tests/ebay_mock.html')
    with open('tests/ebay_mock.html', 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        result = scraper.get_reviews_from_page(soup)
        assert result == expected

# Test the module on real data.
def test_ebay_real_get_reviews():
    expected = []
    with open('tests/ebay_real_reviews.txt', 'r') as file:
        for line in file:
            expected.append(line.rstrip())

    scraper = EbayScraper('https://www.ebay.com/urw/Available-Titles-CengageNOW-Ser-Calculus-Early-Transcendentals-by-James-Stewart-2002-Hardcover-/product-reviews/2408624?_itm=266964871059&pgn=1')
    result = scraper.get_reviews()
    assert result == expected
