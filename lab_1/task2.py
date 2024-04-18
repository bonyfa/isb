import json
import logging
import os.path

from read_save_makedict import read_text_from_file, save_text_to_file, json_to_dict, dict_to_json

logging.basicConfig(level=logging.INFO)

SETTINGS = os.path.join("2", "settings2.json")


def count_the_frequency(text_path: str) -> dict:
    """We count the frequency of occurrence of our symbols and form a dictionary"""
    try:
        text = read_text_from_file(text_path)
        freq = dict()
        length = len(text)
        for letter in text:
            letter = letter.upper()
            if letter not in freq:
                freq[letter] = text.count(letter) / length
        freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        return freq
    except Exception as ex:
        logging.error(f"Incorrect path - {ex}")


def decryption_text(text_path: str, key_path: str) -> str:
    """The function receives a directory with text and a key and encrypts the text"""
    """The function receives a directory with text and a key and encrypts the text"""
    try:
        text = read_text_from_file(text_path)
        encr_text = text.upper()
        key = json_to_dict(key_path)
        keys = key.keys()
        for k in keys:
            if key[k] != " ":
                encr_text = encr_text.replace(k, key[k].lower())
            else:
                l = k
        encr_text = encr_text.replace(l, key[l].lower())
        return encr_text
    except Exception as ex:
        logging.error(f"Wrong dictionary - {ex}")


if __name__ == "__main__":
    settings = json_to_dict(SETTINGS)
    txt_path = os.path.join(
                            settings["fold_task"],
                            settings["original_txt"])
    key_path = os.path.join(
                            settings["fold_task"],
                            settings["key"])
    result_path = os.path.join(
                               settings["fold_task"],
                               settings["result_txt"])
    frequency_path = os.path.join(
                               settings["fold_task"],
                               settings["frequency"])
    freq = count_the_frequency(txt_path)
    dict_to_json(key_path, dict(zip(settings["new alphabet"], settings["alphabet"])))
    save_text_to_file(decryption_text(txt_path, key_path), result_path)

