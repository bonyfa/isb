import logging

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


logging.basicConfig(level=logging.INFO)


def read_data(path: str) -> str:
    """
       Read data from file(in bytes)
       """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = file.read()
        return data
    except Exception as ex:
        logging.error(ex)


def write_data(path: str, text: str) -> None:
    """
       Write data in file(in bytes)
       """
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as ex:
        logging.error(ex)


def read_data_bytes(path: str) -> bytes:
    """
       Read data from file(in bytes)
       """
    try:
        with open(path, 'rb', encoding='utf-8') as file:
            data = file.read()
        return data
    except Exception as ex:
        logging.error(ex)


def write_data_bytes(path: str, text: bytes) -> None:
    """
       Write data in file(in bytes)
       """
    try:
        with open(path, 'wb', encoding='utf-8') as file:
            file.write(text)
    except Exception as ex:
        logging.error(ex)


def serialization_symmetric_key(key: bytes, path: str) -> None:
    """
        Serialization symmetric key in file
        """
    try:
        with open(path, 'wb') as key_file:
            key_file.write(key)
    except Exception as ex:
        logging.error(ex)


def deserialization_symmetric_key(key: bytes, path: str) -> bytes:
    """
        Serialization symmetric key in file
        """
    try:
        with open(path, 'rb', encoding='utf-8') as key_file:
            content = key_file.read()
        return content
    except Exception as ex:
        logging.error(ex)


def serialization_public_key(public_key: rsa.RSAPublicKey,
                             public_pem: str) -> None:
    """
        Serialization public key in file
        """
    try:
        with open(public_pem, 'wb') as public_out:
            public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                     format=serialization.PublicFormat.SubjectPublicKeyInfo))
    except Exception as ex:
        logging.error(ex)


def serialization_private_key(private_key: rsa.RSAPrivateKey,
                              private_pem: str,) -> None:
    """
        Serialization private key in file
        """
    try:
        with open(private_pem, 'wb') as private_out:
            private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                        encryption_algorithm=serialization.NoEncryption()))
    except Exception as ex:
        logging.error(ex)


def deserialization_public_key(public_pem: str) -> rsa.RSAPublicKey:
    """
        Deserialization public key from file
        """
    try:
        with open(public_pem, 'rb') as pem_in:
            public_bytes = pem_in.read()
        return load_pem_public_key(public_bytes)
    except Exception as ex:
        logging.error(ex)


def deserialization_private_key(private_pem: str) -> rsa.RSAPrivateKey:
    """
        Deserialization private key from file
        """
    try:
        with open(private_pem, 'rb') as pem_in:
            private_bytes = pem_in.read()
        return load_pem_private_key(private_bytes, password=None, )
    except Exception as ex:
        logging.error(ex)