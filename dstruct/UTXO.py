import hashlib
""" 
A UTXO is like a certificate that is worth a certain value.
With each transaction, some are created and some are spent. It 
is kind of like a special dollar bill, with its 
dollar amount, transaction id, and unique ID written on the dollar bill.
Say bob pays alice 25 bitcoins. Alice will now have a UTXO with a value of 25 bitcoins.
She wants to buy a house with 30 bitcoins. From another transaction, she has a UTXO
with a value of 5 bitcoins. She uses both UTXOs in single transaction
with a combined value of 30 bitcoin. The owner of the house now has a single 
UTXO worth 30 bitcoins.
"""

class UTXO:

    def __init__(self, txid, index, value):
        # txid: transaction that UTXO belongs to. Txid is Foreign Key referencing transaction
        # index: like a primary key, differentiates among UTXOs
        # value: simply the value of the UTXO
        self.txid = txid
        self.index = index
        self.value = value

    def __str__(self):
        return f'UTXO ({self.txid}:{self.index}) with value {self.value}'


class Transaction:
    # inputs: list of the UTXOs being spent
    # outputs: list of the UTXOs being created
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs

    def __str__(self):
        return f"Transaction with {len(self.inputs)} inputs and {len(self.outputs)} outputs"

    def hash(self):
        #Generates unique hash for transaction
        tx_input  = ''.join([str(inp.txid) + str(inp.index) for inp in self.inputs])
        tx_output = ''.join([str(out.value) for out in self.outputs])
        tx_data   = tx_input + tx_output
        return hashlib.sha256(tx_data.encode()).hexdigest()

def main():
    utxo_1 = UTXO(0,0,25)
    utxo_2 = UTXO(1, 1, 10)
    utxo_3 = UTXO(1, 4, 30)

    input_1 = [utxo_1, utxo_2]
    output_1 = [UTXO(4, 2, 5), UTXO(4, 3, 30)]

    input_2 = [utxo_3]
    output_2 = [UTXO(5, 5, 10), UTXO(5, 6, 20)]

    tx1 = Transaction(input_1, output_1)
    tx2 = Transaction(input_2, output_2)

    print(utxo_1)
    print(utxo_2)
    print(utxo_3)
    print(tx1)
    print(tx2)

    print("tx1 hash:",tx1.hash())
    print("tx2 hash:", tx2.hash())

if __name__ == '__main__':
    main()