import unittest
from src.zk_proof import ZeroKnowledgeProof

class TestZeroKnowledgeProof(unittest.TestCase):
    def setUp(self):
        self.secret = 10  # Example secret
        self.zk = ZeroKnowledgeProof(self.secret)

    def test_verify_proof(self):
        public_data = 5  # Example public data
        proof, random_factor = self.zk.generate_proof(public_data)  # Get proof and random factor
        self.assertTrue(self.zk.verify_proof(proof, public_data, random_factor))  # Pass the random factor

if __name__ == '__main__':
    unittest.main()
