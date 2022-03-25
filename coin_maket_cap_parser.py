import requests
from bs4 import BeautifulSoup
from time import sleep
import lxml
from save_html import save_html

URL = "https://coinmarketcap.com"
HEADERS = {
    "accept": "application/json, text/plain, */*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
}

def get_html(url):
    """Получаем html страницу"""
    r = requests.get(url, headers=HEADERS)
    return r.text


def get_all_links(html):
    """Получаем ссылки на все криптовалюты с главной страницы и собираем в список"""
    soup = BeautifulSoup(html, "lxml")

    table = soup.find("table", class_="czTsgW")
    trs = table.find("tbody").find_all("tr", limit=20)
    links = []
    for tr in trs:
        a = tr.find("a").get("href")
        a = URL + a + "historical-data/"
        links.append(a)
    return links


def get_hist_values(html):
    """Собираем данные о конретной криповалюте в разделе history data"""
    pass


def main():
    """Главная функция вызывающая все остальные"""
    all_links = get_all_links(get_html(URL))
    for url in all_links:
        my_html = get_html(url)
        get_hist_values(my_html)
        # save_html(my_html, url)


if __name__ == "__main__":
    print(main())