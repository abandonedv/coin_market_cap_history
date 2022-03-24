import requests
from bs4 import BeautifulSoup
from time import sleep
import lxml

URL = "https://coinmarketcap.com"


def get_html(url):
    """Получаем html страницу"""
    r = requests.get(url)
    return r.text


def get_all_links(html):
    """Получаем ссылки на все криптовалюты с главной страницы и собираем в список"""
    soup = BeautifulSoup(html, "lxml")

    table = soup.find("table", class_="czTsgW")
    divs = table.find_all("div", class_="sc-16r8icm-0 escjiH")
    links = []
    for d in divs:
        a = d.find("a").get("href")
        a = URL + a + "historical-data/"
        links.append(a)
    return links


def get_hist_values(html, url):
    """Собираем данные о конретной криповалюте в разделе history data"""
    soup = BeautifulSoup(html, "lxml")
    div = soup.find("div", class_="sc-16r8icm-0 jKrmxw container")
    print(div.prettify())


def main():
    """Главная функция вызывающая все остальные"""
    all_links = get_all_links(get_html(URL))
    for l in all_links:
        get_hist_values(get_html(l), l)


if __name__ == "__main__":
    print(main())
