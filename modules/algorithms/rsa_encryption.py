#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ast

from Crypto.PublicKey import RSA


def enc_dec():
    print("\n\t[1.] Encrypt with RSA algorithm")
    print("\t[2.] Decrypt with RSA algorithm")
    print("\t[CTRL + C] EXIT mirror-enc")
    x = '0'
    while x not in ['1', '2']:
        x = str(raw_input("\nmirror-enc > "))
    if x == '1':
        return "enc"
    elif x == '2':
        return "dec"


def choose_key(alg):
    if alg == "enc":
        key_path = raw_input("\npubKey.pem path: ")
    elif alg == "dec":
        key_path = raw_input("\nprvKey.pem path: ")
    f = open(key_path, 'rb')
    key = RSA.importKey(f.read())
    return key


def encrypt(plaintext, key):
    try:
        cipher = key.encrypt(plaintext, 32)
        return cipher
    except Exception as e:
        raise e


def decrypt(ciphertext, key):
    try:
        plain = key.decrypt(ast.literal_eval(str(ciphertext)))
        return plain
    except Exception as e:
        raise e
