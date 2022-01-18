from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

ADDRESS = os.environ.get('ADDRESS')
KEY = os.environ.get('KEY')


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