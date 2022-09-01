import os

import requests
import bs4
from requests.exceptions import MissingSchema
from sqlalchemy.orm import Session

from conf import get_engine
from models import Info, Base

session = Session(bind=get_engine())


def get_url_and_html(url, link):
    try:
        new_req = requests.get(str(link.get('href')))
        new_html = bs4.BeautifulSoup(new_req.text, features="html.parser")
    except MissingSchema:
        new_req = requests.get(str(url) + str(link.get('href')))
        new_html = bs4.BeautifulSoup(new_req.text, features="html.parser")
    return new_req.url, new_html


def pars(url):
    req = requests.get(url)
    html = bs4.BeautifulSoup(req.text, features="html.parser")
    try:
        link_list = html.find_all('a')
        for link in link_list:
            new_req, new_html = get_url_and_html(url, link)
            if session.query(Info).filter_by(url=new_req).first():
                return
            else:
                current_info = Info(url=new_req, title=new_html.title.string)
                session.add(current_info)
                session.commit()
            new_link_list = new_html.find_all('a')
            for new_link in new_link_list:
                new_req, new_html = get_url_and_html(url, new_link)
                current_info = Info(url=new_req, title=new_html.title.string)
                session.add(current_info)
                session.commit()
    except IndexError:
        raise Exception("site not available")


Base.metadata.create_all(get_engine())

if __name__ == '__main__':
    url = os.environ.get('URL')
    pars(url)
