# Anonymous Digital Payment System

This project implements an anonymous digital payment system that mimics the privacy of cash transactions while ensuring the security and integrity of digital payments. The system incorporates cryptographic protocols such as Zero-Knowledge Proofs (ZKP), Secure Multi-Party Computation (SMPC), and Blind Signatures to maintain anonymity and prevent malicious behavior like fraud or money laundering.


## Project Overview

This project aims to create a digital payment system that prioritizes user privacy and security. The key objectives of the system include:

- **User Privacy**: Ensure that neither the sender nor the receiver has access to each other’s sensitive details while maintaining the privacy and security of the transaction.
- **Transaction Integrity**: Ensure that transactions only proceed when the sender has sufficient balance while keeping the user details anonymous.
- **Fraud Prevention**: Implement cryptographic techniques to prevent fraud, abuse, or illegal activities while respecting user privacy.

## Key Components

### 1. `accounts.py`
Handles user accounts, including balance creation, updates, and validation. Each user has a unique account that holds their balance in the system.

### 2. `blind_signatures.py`
Implements blind signature cryptography to ensure that sensitive data such as account numbers and transaction histories remain private during the signing of transactions.

### 3. `zk_proof.py`
Implements Zero-Knowledge Proofs (ZKP) for validating transaction amounts without revealing sensitive user information, ensuring privacy and security.

### 4. `smpc.py`
Implements Secure Multi-Party Computation (SMPC), allowing for collaborative computation over private data without revealing sensitive information.

### 5. `ot.py`
Implements Oblivious Transfer (OT), a cryptographic protocol that enables one party to send data to another without revealing any additional information.

### 6. `transaction.py`
Handles the core transaction logic, including verification of balances, executing transactions between users, and logging necessary transaction information.

### 7. `utils.py`
Provides utility functions to support the main cryptographic modules and transaction processes, such as key generation, hashing, and encoding.

## Tests

The `tests/` folder contains unit tests for validating the correctness of the cryptographic protocols, account handling, and transaction logic. The key test files are:

- `test_accounts.py`: Tests for account creation and balance handling.
- `test_zk_proof.py`: Tests for validating Zero-Knowledge Proofs.
- `test_smpc.py`: Tests for Secure Multi-Party Computation.
- `test_transaction.py`: Tests for transaction verification and processing.
- `test_ot.py`: Tests for Oblivious Transfer.

## Getting Started

### Prerequisites

- Python 3.7+
- Flask for serving backend APIs
- Cryptographic libraries such as `PyCryptodome`, `gmpy2`, or similar

### Running the tests
- Step-1
  ```bash
  pip install -r requirements.txt
- Step-2
  ```bash
  python -m pytest tests/


### Explanation of the Structure:
- **`src/`**: Contains all the core source code for the system, including cryptographic modules and transaction handling.
- **`tests/`**: Contains unit tests for all the core functionalities.
