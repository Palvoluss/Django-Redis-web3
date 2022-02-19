import os
from pathlib import Path
from dotenv import load_dotenv
from web3 import Web3

env_path = Path('/Users/pablomicheletti/Desktop/S2I/DjangoRedis/.env', '.env')
load_dotenv(dotenv_path=env_path)

ADDRESS = os.getenv('ADDRESS')
KEY = os.getenv('KEY')


def sendTransaction(message):
    w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/b85ca4dfafd94e1ea8f0b77e326fdc64'))
    address = ADDRESS
    privateKey = KEY
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0, "ether")
    signedTx = w3.eth.account.sign_transaction(dict(
        nonce=nonce,
        gasPrice=gasPrice,
        gas=100000,
        to='0xFe0196504dF34c4Bf30D3089EfFf86cFe3B34617',
        value=value,
        data=message.encode('utf-8')
    ), privateKey)
    tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId