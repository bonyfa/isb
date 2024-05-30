import logging

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


logging.basicConfig(level=logging.INFO)


def read_data(path: str) -> str:
    try:
        with open(path, 'w', encoding='utf-8') as file:
            data = file.read()
        return data
    except Exception as ex:
        logging.error(ex)


def write_data(path: str, text: str) -> None:
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as ex:
        logging.error(ex)