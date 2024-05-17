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

def test_identical_consecutive_bits(str: str) -> float:
    try:
        str1 = list(str)
        l = 1/len(str1) * sum(str1)
        if ((fabs(l - 0.5)) >=(2 / sqrt(len(str1)))):
            return 0.0
        Vn = 0
        for i in range (len(str1)-1):
            Vn += 0 if str1[i] == str[i+1] else 1
        p = erfc((fabs(Vn - 2*len(str1)*l*(1-l)))/(2 * sqrt(2 * len(str1)) * l * (1-l)))
        return p
    except Exception as ex:
        logging.error(f"Wrong str - {ex}")




if __name__ == "__main__":
    with open(SETTINGS, 'r', encoding='utf-8') as f:
        sequence = json.load(f)




