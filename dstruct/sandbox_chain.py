import datetime
import hashlib

class Block:
    def __init__(self, data, previous_hash,timestamp = None):
        # Header
        self.previous_hash = previous_hash
        self.block_number = None
        self.timestamp = timestamp or datetime.datetime.now()
        self.nonce = 0
        self.difficulty = 2

        # Body
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        str_to_hash = \
            (
                    str(self.data) +
                    str(self.previous_hash) +
                    str(self.timestamp) +
                    str(self.nonce)
            )
        return hashlib.sha256(str_to_hash.encode()).hexdigest()

    def mine_block(self):
        while self.hash[0:self.difficulty] != "0" * self.difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print("Block mined! {}".format(self.hash))

class BlockChain:
    def __init__(self):
        self.chain = [self.genesis()]

    def genesis(self):
        return Block("Genesis Block", "Null")

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        new_block.mine_block()
        new_block.block_number = len(self.chain)
        self.chain.append(new_block)

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.previous_hash != previous_block.hash:
                return False
            if current_block.hash != current_block.calculate_hash():
                return False
        return True

    def show(self):
        prev_block = None
        for block in self.chain:
            print(f'Header:\n\tPrev Hash: {block.previous_hash}\n\tBlock Number: {block.block_number}')
            print(f'\tTime Created: {block.timestamp}\n\tNonce: {block.nonce}')
            if prev_block:
                creation_time = block.timestamp - prev_block.timestamp
                print(f'\tTime Since Last Block: {creation_time}')
            print(f'Body:\n\tData: {block.data}\n\tHash: {block.hash}\n\n')
            prev_block = block



def __main__():
    blockchain = BlockChain()
    blockchain.genesis()
    blockchain.add_block(Block("Test1", ""))
    blockchain.add_block(Block("Test2", ""))
    blockchain.add_block(Block("Test3", ""))
    blockchain.add_block(Block("Test4", ""))

    blockchain.show()

    print(f'\ntesting validity: {str(blockchain.validate_chain())}')
    blockchain.chain[2].data = "I just tampered with the data"
    print('\ntampering with data:')
    print(f'\ntesting validity: {str(blockchain.validate_chain())}')

if __name__ == '__main__':
    __main__()




