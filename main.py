import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(previous_hash="Here is the statement for block.", proof=100)

# Create a new block listing key/value pairs of block information in a JSON object. Reset the list of pending transactions & append the newest block to the chain.

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block

#Search the blockchain for the most recent block.

    @property
    def last_block(self):
 
        return self.chain[-1]

# Add a transaction with relevant info to the 'blockpool' - list of pending tx's. 

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

# receive one block. Turn it into a string, turn that into Unicode (for hashing). Hash with SHA256 encryption, then translate the Unicode into a hexidecimal string.

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash



blockchain = Blockchain()
t1 = blockchain.new_transaction("Satoshi", "Adhi", '5 BTC')
t2 = blockchain.new_transaction("Adhi", "Satoshi", '1 BTC')
t3 = blockchain.new_transaction("Satoshi", "Adhi", '5 BTC')
blockchain.new_block(12345)

t4 = blockchain.new_transaction("Adhi", "Nakamura", '1 BTC')
t5 = blockchain.new_transaction("Nakamura", "Bob", '0.5 BTC')
t6 = blockchain.new_transaction("Bob", "Adhi", '0.5 BTC')
blockchain.new_block(6789)

print("Genesis block: ", blockchain.chain)