import unittest

import bs4
import requests

from pars.parser import get_url_and_html


class TestInfo(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'https://www.gazeta.ru/'
        self.bad_url = 'https://www.gazeta.ru/414214/'
        self.req = requests.get(self.url)
        self.bad_req = requests.get(self.bad_url)
        self.html = bs4.BeautifulSoup(self.req.text, features='html.parser')

    def test_get_url_and_html(self):
        url, html = get_url_and_html(self.url, self.html.find('a'))
        self.assertEqual(url, self.url)
        self.assertEqual(html, self.html)


if __name__ == '__main__':
    unittest.main()
