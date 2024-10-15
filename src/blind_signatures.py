# blind_signatures.py
import random

class BlindSignature:
    def __init__(self, private_key, public_key):
        self.private_key = private_key
        self.public_key = public_key

    def blind(self, message):
        blinding_factor = random.randint(1, self.public_key - 1)
        blinded_message = (message * pow(blinding_factor, self.public_key)) % self.public_key
        return blinded_message, blinding_factor

    def sign(self, blinded_message):
        return pow(blinded_message, self.private_key) % self.public_key

    def unblind(self, signed_message, blinding_factor):
        return (signed_message * pow(blinding_factor, -1, self.public_key)) % self.public_key
