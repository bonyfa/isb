import argparse
import logging
import json

from HybridEncryption import HybridCryptoSystem


logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    """
    Main function to generate keys, encrypt data, or decrypt data based on the mode specified in the options.
    """
    parser = argparse.ArgumentParser(description="Process options for Hybrid Crypto System")
    parser.add_argument("--options_file",
                        type=str,
                        default="lab_3/options.json",
                        help="Path to the JSON options file")
    parser.add_argument("--mode",
                        type=int,
                        default=0,
                        help="operation type")
    parser.add_argument("--sym_key_length",
                        type=int,
                        default=128,
                        help="length of symmetric key")
    args = parser.parse_args()

    try:
        with open(args.options_file, "r") as options_file:
            options = json.load(options_file)

        match args.mode:
            case 0:
                HybridCryptoSystem.generate_keys(args.sym_key_length, options['generation'])
            case 1:
                HybridCryptoSystem.encrypt_text(options['encryption'])
            case 2:
                HybridCryptoSystem.decrypt_text(options['decryption'])
            case _:
                raise ValueError(f"Invalid mode: {args.mode}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")