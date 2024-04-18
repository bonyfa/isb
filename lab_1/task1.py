import json
import logging
import os.path

from read_save_makedict import read_text_from_file, save_text_to_file, json_to_dict

logging.basicConfig(level=logging.INFO)

SETTINGS = os.path.join("1", "settings1.json")


def encryption_text(text_path: str, key_path: str) -> str:
    """The function receives a directory with text and a key and encrypts the text"""
    try:
        text = read_text_from_file(text_path)
        encr_text = text.upper()
        key = json_to_dict(key_path)
        keys = key.keys()
        for k in keys:
            encr_text = encr_text.replace(k, key[k].lower())
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

    save_text_to_file(encryption_text(txt_path, key_path), result_path)
