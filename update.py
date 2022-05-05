import pprint
import time
import my_dbase
import math
import requests
import asyncio
from time_data import time_data
from coin_market_cap_parser import URL_HIST_PER_HOUR, IDS
from coin_market_cap_API import get_id_of_coin
from my_classes import DateData


async def get_json(id, t_s, t_e):
    my_range = str(t_s) + "~" + str(t_e)
    parameters = {
        "id": id,
        "range": my_range
    }
    return requests.get(URL_HIST_PER_HOUR, params=parameters).json()


async def find_new(item):
    current_time = math.floor(time.time())
    t_s = my_dbase.get_time_of_last_update_of_coin(item)
    t_e = t_s + 3600
    id = get_id_of_coin(item, "USD")
    print(item)
    while t_e < current_time - 86400:
        my_json = await get_json(id, t_s, t_e)
        new_row_time = (list(my_json["data"]["points"].items()))[-1][0]
        new_row = my_json["data"]["points"][new_row_time]
        hour_date = DateData(item,
                             time_data(time.ctime(int(new_row_time)), time_need=True),
                             new_row_time,
                             new_row["v"][0])
        print(hour_date)
        await my_dbase.insert_one_coin(hour_date)
        t_s = t_e
        t_e = t_e + 3600


async def main():
    crypt_list = my_dbase.get_all_coin_names()
    for item in crypt_list:
        await find_new(item)


if __name__ == "__main__":
    asyncio.run(main(), debug=False)
