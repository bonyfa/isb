import json
import logging

from read_save_makedict import read_text_from_file,save_text_to_file,json_to_dict

logging.basicConfig(level=logging.INFO)

ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
SETTINGS = "settings.json"


def encryption_text(text_path : str, key_path : str) -> str:

    try:
        text = read_text_from_file(text_path)
        encr_text = text.upper()
        key = json_to_dict(key_path)
        keys = key.keys()
        for k in keys:
            encr_text = encr_text.replace(k, key[k].lower)
        return encr_text
    except Exception as ex:
        logging.error(f"Wrong dictionary - {ex}")

if __name__ == "__main__":
    print(encryption_text("text.txt","key.json"))
                


