import json
import logging
import os.path
from math import erfc, fabs, sqrt, pow

logging.basicConfig(level=logging.INFO)

SETTINGS =("sequence.json")

def bit_test(str: str)-> float:
    try:
        summa = 0
        str1 = str.replace("0","-1")
        str1 = list(str1)
        sn = 1 / sqrt(len(str1)) * sum(str1)
        p = erfc(sn / sqrt(2))
        return p
    except Exception as ex:
        logging.error(f"Wrong str - {ex}")





if __name__ == "__main__":
    with open(SETTINGS, 'r', encoding='utf-8') as f:
        sequence = json.load(f)




