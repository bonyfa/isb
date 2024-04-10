import json
import logging
import os.path

from read_save_makedict import read_text_from_file,save_text_to_file,json_to_dict , dict_to_json

logging.basicConfig(level=logging.INFO)

SETTINGS = os.path.join("2", "settings2.json")
ALPHABET = " оиеантсрвмлдякпзыьучжгхфйюбцщэъ"


def count_the_frequency(text_path: str) -> dict:
    """We count the frequency of occurrence of our symbols and form a dictionary"""
    try:
        text = read_text_from_file(text_path)
        freq = dict()
        length = len(text)
        for letter in text:
            if letter not in freq:
                freq[letter] = text.count(letter) / length
        freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        return freq
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
    dict_to_json(frequency_path, count_the_frequency(txt_path))