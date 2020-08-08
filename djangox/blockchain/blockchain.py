'''
blockchain secured digital currency
instead of electricity that ultimatlely powers bitcoin
with randomness to keep the network secure, this one will
be built up with software commits.
'''
import hashlib
import random
import string
import json
import binascii
import numpy as np
import pandas as pd
import pylab as pl
import logging
%matplotlib inline
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

def sha256(message):
    return hashlib.sha256(message.encode('ascii')).hexdigest()

message = 'hello bitcoin'
for nonce in range(1000):
    digest = sha256(message+str(nonce))
    if digest.startswith('11'):
        print('Found nonce: %d' % nonce)
        break
print(sha256(message+str(nonce)))
def dumb_hash(message):
    """
    Returns an hexadecimal hash
    """
    return sha256(message)
def mine(message, difficulty=1):
    """
    Given an input string, will return a nonce such that
    hash(string + nonce) starts with `difficulty` ones

    Returns: (nonce, niters)
        nonce: The found nonce
        niters: The number of iterations required to find the nonce
    """
    assert difficulty >= 1, "Difficulty of 0 is not possible"
    i = 0
    prefix = '1' * difficulty
    while True:
        nonce = str(i)
        digest = dumb_hash(message + nonce)
        if digest.startswith(prefix):
            return nonce, i
        i += 1
nonce, niters = mine('42', difficulty=1)
print('Took %d iterations' % niters)

nonce, niters = mine('42', difficulty=3)
print('Took %d iterations' % niters)
