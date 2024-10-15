# utils.py
import random
from hashlib import sha256

def hash_data(data):
    return sha256(data.encode()).hexdigest()

def generate_random_number(limit):
    return random.randint(1, limit)
