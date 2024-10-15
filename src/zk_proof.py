import random

class ZeroKnowledgeProof:
    def __init__(self, secret):
        self.secret = secret

    def generate_proof(self, public_data):
        random_factor = random.randint(1, 100)
        proof = (public_data * self.secret) + random_factor
        return proof, random_factor  # Return both proof and the random factor

    def verify_proof(self, proof, public_data, random_factor):
        expected_value = public_data * self.secret
        # Proof should be within the range of expected_value and expected_value + random_factor
        return expected_value < proof <= expected_value + 100  # Adjust as per your random factor logic