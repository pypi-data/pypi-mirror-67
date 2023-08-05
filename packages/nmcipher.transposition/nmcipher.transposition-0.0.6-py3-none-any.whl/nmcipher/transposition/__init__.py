from nmcipher.cli import Parser
from .columnar import Columnar

def encrypt_func(key, message):
    cipher = Columnar(key)
    print(message)
    print(cipher.encrypt(message))

def decrypt_func(key, message):
    cipher = Columnar(key)
    print(message)
    print(cipher.decrypt(message))

def hack_func(method, message):
    if method != "brute":
        raise NotImplementedError("Columnar class only supports brute-force method")
    for key in range(1, len(message) + 1):
        cipher = Columnar(key)
        print(f"With key = {key}:")
        print(f"\tOutput: {cipher.decrypt(message)}")

def main():
    Parser(encrypt_func, decrypt_func, hack_func)()
