import json
import logging

logging.basicConfig(level=logging.INFO)


def read_text_from_file(path: str) -> str:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            txt = f.read()
        return txt
    except Exception as ex:
        logging.error(f"Incorrect path - {ex}")


def save_text_to_file(text: str, path: str) -> None:
    try:
        with open(path, 'w', encoding='utf-8') as f:
            txt = f.write(text)
    except Exception as ex:
        logging.error(f"Incorrect path - {ex}")


def json_to_dict(path: str) -> dict:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            key = json.load(f)
        return key
    except Exception as ex:
        logging.error(f"Incorrect path - {ex}")


def dict_to_json(path: str, dict: dict) -> None:
    try:
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(dict, file)
    except Exception as ex:
        logging.error(f"Incorrect dict - {ex}")