import json
import logging

logging.basicConfig(level=logging.INFO)


def read_text_from_file(path:str)->str:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            txt = f.read()
        return txt
    except FileNotFoundError as ex:
        logging.error(f"Incorrect path - {ex}")

def save_text_to_file(text:str,dict:str)->None