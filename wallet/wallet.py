# Import dependencies
import subprocess
import json
from dotenv import load_dotenv
from web3 import Web3

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic")

# Import constants.py and necessary functions from bit and web3
from constants import *
 
 
# Create a function called `derive_wallets`
def derive_wallets(mnemonic,coin,numderive,format):
    command = 'php ./derive -g --mnemonic="'+str(mnemonic)+'" --numderive='+str(numderive)+', --coin='+str(coin)+' --format='+str(format)
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {'eth': derive_wallets(mnemonic,ETH,3,json), 'btc-test': derive_wallets(mnemonic,BTCTEST,3,json)}

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    if coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin, account, to, amount):
    gasEstimate = w3.eth.estimateGas (
        {"from": account.address, "to": to, "value": amcount}
    )
    return {
        "from": account.address,
        "to": to,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": w3.eth.getTransactionCount(W3.toChecksumAddress(account.address))
    }

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(coin, account, to, amount):
    tx = create_tx(coin, account, to, amount)
    signed_tx = account.sign_transaction(tx)
    result = w3.eth.send_raw_transaction(signed_tx.rawTransacton)
    print(result.hex())
    return result.hex()
