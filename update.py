import pprint
import time
import my_dbase
import math
import requests
from coin_market_cap_parser import URL_HIST_PER_HOUR, IDS
from coin_market_cap_API import get_id_of_coin


def find_new(item):
    current_time = math.floor(time.time())
    t_s = item.coin_time_in_sec
    print(t_s)
    t_e = t_s + 3700
    if t_e <= current_time:
        my_range = str(t_s) + "~" + str(t_e)
        id = get_id_of_coin(item.coin_parse, "USD")
        print(item.coin_parse)
        parameters = {
            "id": id,
            "range": my_range
        }
        my_json = requests.get(URL_HIST_PER_HOUR, params=parameters).json()
        new_row_time = (list(my_json["data"]["points"].items()))[-1][0]
        new_row = my_json["data"]["points"][new_row_time]
        print(new_row)
        # print(my_json["data"]["points"][f"{t_e}"])
        # t_s = t_e
        # t_e = t_e + 3600


def main():
    current_time = time.time()
    crypt_list = my_dbase.get_all_coin_names()
    for item in crypt_list:
        find_new(item)
        break


if __name__ == "__main__":
    main()
