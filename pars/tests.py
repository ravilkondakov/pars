import unittest

import bs4
import requests


class TestInfo(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'https://www.gazeta.ru/'
        self.bad_url = 'https://www.gazeta.ru/414214/'
        self.req = requests.get(self.url)
        self.bad_req = requests.get(self.bad_url)
        self.html = bs4.BeautifulSoup(self.req.text, features='html.parser')

    def test_status_code(self):
        self.assertEqual(200, self.req.status_code)

    def test_bad_status_code(self):
        self.assertEqual(404, self.bad_req.status_code)

    def test_body(self):
        self.assertEqual('Главные новости - Газета.Ru', self.html.title.string)

    def test_urls(self):
        link_body = self.html.find_all('a')[2]
        link = link_body.get('href')
        self.assertEqual('/news/', link)
        full_link = str(self.url) + str(link)
        self.assertEqual(full_link, 'https://www.gazeta.ru//news/')


if __name__ == '__main__':
    unittest.main()
