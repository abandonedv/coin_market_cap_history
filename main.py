import pprint
import json
import requests


def price_of_crypt():
    try:

        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/historical'
        parameters = {
            'start': "20210101",
            'end': "20220101"
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '881ca7de-a5a6-4971-885a-3d800be10159',
        }

        session = requests.Session()
        session.headers.update(headers)

        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        pprint.pprint(data)
    except Exception as e:
        print(e)


price_of_crypt()
