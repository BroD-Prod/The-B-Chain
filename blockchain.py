import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self, proof, previous_hash=None):
        """
        :param proof: <int> Proof of Work Algo
        :param previous_hash: <str> Hash of previous Block
        :return: <dict> New Block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        :param sender: <str> Sender Address
        :param recipient: <str> Recipient Address
        :param amount: <int> Amount
        :return: <int> The Block That Holds the Transaction
        """

        self.current_transactions.append({
            'sender':sender,
            'recipient':recipient,
            'amount': amount
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        :param block:  <dict> Block
        :return: <str>
        """

        block_string = json.dumps(block, sort_keys=True).encode()
        return  hashlib.sha256(block_string).hexdigest()

    def last_block(self):
        return self.chain[-1]