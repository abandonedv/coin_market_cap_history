import os
from my_rename import time_data

NAME_OF_DIR = "saved_json_per_hour"

files = os.listdir(NAME_OF_DIR)

for old_name in files:
    print(len(files))
    old_name = os.path.join(NAME_OF_DIR, f"{old_name}")
    name_of_coin = ""
    time_of_file = []
    for i, x in enumerate(old_name.split("-")):
        if not x.isdigit():
            name_of_coin += x + "-"
        else:
            time_of_file = old_name.split("-")[i:]
            time_of_file[-1] = time_of_file[-1].split(".")[0]
            my_time = time_data(time_of_file)
            new_name = name_of_coin[:-1] + "_" + my_time + ".json"
            os.rename(old_name,
                      new_name)
            print(new_name)
            break
