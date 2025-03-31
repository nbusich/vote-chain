import hashlib
import datetime

from dstruct.basic_chain import block


class BlockNode:
    def __init__(self, data, timestamp = None):
        """Initializes a new block node. Next_back points to the block behind"""
        self.data = data
        self.timestamp = timestamp or datetime.datetime.now()
        self.next_back = None

class Blockchain:
    def __init__(self):
        """ Initializes the blockchain, head is the newest block."""
        self.head = None

    def add_block(self, data):
        """ Adds a new block to the blockchain."""
        new_block = BlockNode(data)
        if self.head is None: # If head is none, the blockchain is empty.
            self.head = new_block
        else: # This else statement will locate the newest block,
            current_block = self.head # Sets the current block to the newest block
            while current_block.next_back: # Loops from head to genesis block
                current_block = current_block.next_back
            current_block.next_back = new_block

    def mine_block(self, data):
        new_block = BlockNode(data)
        new_block.next = self.head
        self.head = new_block

    def traverse(self):
        current_block = self.head
        while current_block:
            print(f'\nData: {current_block.data}\nTimestamp: {current_block.timestamp}')
            current_block = current_block.next_back

bc = Blockchain()
bc.add_block("Test1")
bc.add_block("Test2")

print("Before adding new mined block")
bc.traverse()
print("\n\nBlockchain after adding new mined block")
bc.mine_block("Test3")
bc.traverse()