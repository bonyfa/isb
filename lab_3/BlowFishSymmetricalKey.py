import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from Workwithfile import read_data, deserialization_symmetric_key, write_data_bytes, read_data_bytes,  write_data


class BlowFishCipher:
    """
        Class providing methods for symmetric cryptography operations.
        """
    @staticmethod
    def generate_key(sym_key_length: int) -> bytes:
        """
            Generate a symmetric key
            """
        return os.urandom(sym_key_length//8)

    @staticmethod
    def encrypt_text(self,
                     path_text: str,
                     path_encr_text: str,
                     path_key: str) -> bytes:
        """
            Encrypt the text using a symmetric key and save result in file
            """
        text = bytes(read_data(path_text), 'UTF-8')
        key = deserialization_symmetric_key(path_key)

        padder = padding.PKCS7(128).padder()
        padded_text = padder.update(text) + padder.finalize()
        iv = os.urandom(16)
        cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        encryptor_text = encryptor.update(padded_text) + encryptor.finalize()

        write_data_bytes(encryptor_text, path_encr_text)
        return encryptor_text

    def decrypt_text(self,
                     path_encr_text: str,
                     path_decry_text: str,
                     path_key: str) -> str:
        """
            Decrypt the text using a symmetric key and save result in file
            """
        text = read_data_bytes(path_encr_text)
        key = deserialization_symmetric_key(path_key)
        iv = text[:16]
        text = text[16:]

        cipher = Cipher(algorithms.SEED(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        dc_text = decryptor.update(text) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()
        result_text = unpadded_dc_text.decode('utf-8')

        write_data(result_text, path_decry_text)
        return result_text