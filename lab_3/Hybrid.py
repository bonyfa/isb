import logging

from BlowFishSymmetricalKey import BlowFishCipher
from AssymmetricalKey import RSACipher
import Workwithfile

logging.basicConfig(level=logging.INFO)


class HybridCryptoSystem:
    """
        Class for hybrid encryption using both symmetric and asymmetric keys.
        """

    @staticmethod
    def generate_keys(sym_key_length: int, options: dict) -> None:
        """
            Generate RSA key pair and symmetric key and save them to files.
            """
        rsa_private_key, rsa_public_key = RSACipher.generate_key_pair(key_size=2048)
        symmetric_key = BlowFishCipher.generate_key(sym_key_length)

        Workwithfile.serialization_private_key(rsa_private_key, options['rsa_private_key_path'])
        Workwithfile.serialization_public_key(rsa_public_key, options['rsa_public_key_path'])

        encrypted_sym_key = RSACipher.encrypt_with_public_key(symmetric_key, rsa_public_key)
        Workwithfile.serialization_symmetric_key(encrypted_sym_key, options['symmetric_key_path'])

    @staticmethod
    def encrypt_text(options: dict) -> None:
        """
            Encrypt text using hybrid encryption and save the result to a file.
            """
        text = Workwithfile.read_data_bytes(options['input_text'])
        enc_sym_key = Workwithfile.deserialization_symmetric_key(options['symmetric_key_path'])
        private_key = Workwithfile.deserialization_private_key(options['rsa_private_key_path'])

        symmetric_key = RSACipher.decrypt_with_private_key(enc_sym_key, private_key)

        encrypted_text = BlowFishCipher.encrypt_text(text, symmetric_key)

        Workwithfile.write_data_bytes(encrypted_text, options['encrypted_text_path'])

    @staticmethod
    def decrypt_text(options: dict) -> None:
        """
        Decrypt text using hybrid decryption and save the result to a file.
        """
        encrypted_symmetric_key = Workwithfile.deserialization_symmetric_key(options['symmetric_key_path'])
        encrypted_text = Workwithfile.read_data_bytes(options['encrypted_text_path'])

        rsa_private_key = Workwithfile.deserialization_private_key(options["rsa_private_key_path"])
        symmetric_key = RSACipher.decrypt_with_private_key(encrypted_symmetric_key, rsa_private_key)

        decrypted_text = BlowFishCipher.decrypt_text(encrypted_text, symmetric_key)

        Workwithfile.write_data(decrypted_text.decode('utf-8'), options['decrypted_text_path'])