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
            link_list = html.find_all('a')
            for link in link_list:
                new_req = requests.get(str(url) + str(link.get('href')))
                new_html = bs4.BeautifulSoup(new_req.text, features="html.parser")
                if session.query(Info).filter_by(url=new_req.url).first():
                    return
                else:
                    current_info = Info(url=new_req.url, title=new_html.title.string)
                    session.add(current_info)
                    session.commit()
                new_link_list = new_html.find_all('a')
                for new_link in new_link_list:
                    try:
                        new_req_2 = requests.get(str(new_link.get('href')))
                        new_html_2 = bs4.BeautifulSoup(new_req_2.text, features="html.parser")
                    except MissingSchema:
                        new_req_2 = requests.get(str(url) + str(new_link.get('href')))
                        new_html_2 = bs4.BeautifulSoup(new_req_2.text, features="html.parser")
                    current_info = Info(url=new_req_2.url, title=new_html_2.title.string)
                    session.add(current_info)
                    session.commit()
        except IndexError:
            raise Exception("site not available")
        n += 1


Base.metadata.create_all(engine)

if __name__ == '__main__':
    url = 'http://gazeta.ru'
    pars(url)
