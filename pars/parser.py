import requests
import bs4
from requests.exceptions import MissingSchema
from sqlalchemy.orm import Session

from conf import engine
from models import Info, Base

session = Session(bind=engine)


def pars(url):
    req = requests.get(url)
    html = bs4.BeautifulSoup(req.text, features="html.parser")
    n = 1
    while n < 5:
        try:
            link_list = html.find_all('a')[n]
            link = link_list.get('href')
            try:
                new_req = requests.get(str(link))
                new_html = bs4.BeautifulSoup(new_req.text, features="html.parser")
            except MissingSchema:
                new_req = requests.get(str(url) + str(link))
                new_html = bs4.BeautifulSoup(new_req.text, features="html.parser")
            if session.query(Info).filter_by(url=new_req.url).first():
                return
            else:
                current_info = Info(url=new_req.url, title=new_html.title.string)
                session.add(current_info)
                session.commit()
        except IndexError:
            raise Exception("site not available")
        n += 1


Base.metadata.create_all(engine)

if __name__ == '__main__':
    url = 'http://lenta.ru'
    pars(url)
