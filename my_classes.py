class NewsData:
    def __init__(self, news):
        self.news_parse = news[0]["slug"]
        self.news_time = time_data(time.ctime(news[0]["publishDate"]), time_need=True)
        self.news_time_in_sec = news[0]["publishDate"]
        self.news_title = news[0]["title"]
        self.__news_lead = "None"

    def get_news_lead(self):
        return self.__news_lead

    def set_news_lead(self, value):
        try:
            self.__news_lead = value["lead"]

        except:
            self.__news_lead = "None"

    news_lead_p = property(get_news_lead, set_news_lead)


class DateData:
    """Класc для удобного представления необходимых мне данных"""

    def __init__(self, name, coin_time, coin_time_in_sec, coin_value):
        self.coin_parse = name
        self.coin_time = coin_time
        self.coin_time_in_sec = coin_time_in_sec
        self.coin_value = coin_value

    def __repr__(self):
        return str(self.__dict__)
