import pandas as pd
from datetime import datetime

import os
import time
import requests

from dotenv import load_dotenv

def get_addresses():
    return ['0x3f5ce5fbfe3e9af3971dd833d26ba9b5c936f0be', '0x85b931a32a0725be14285b66f1a22178c672d69b', '0x708396f17127c42383e3b9014072679b2f60b82f', '0xe0f0cfde7ee664943906f17f7f14342e76a5cec7', '0x8f22f2063d253846b53609231ed80fa571bc0c8f', '0x28c6c06298d514db089934071355e5743bf21d60', '0x21a31ee1afc51d94c2efccaa2092ad1028285549', '0xdfd5293d8e347dfe59e90efd55b2956a1343963d', '0x56eddb7aa87536c09ccc2793473599fd21a8b17f', '0x9696f59e4d72e237be84ffd425dcad154bf96976', '0x4d9ff50ef4da947364bb9650892b2554e7be5e2b', '0xd551234ae421e3bcba99a0da6d736074f22192ff', '0x4976a4a02f38326660d17bf34b431dc6e2eb2327', '0xd88b55467f58af508dbfdc597e8ebd2ad2de49b3', '0x7dfe9a368b6cf0c0309b763bb8d16da326e8f46e', '0x345d8e3a1f62ee6b1d483890976fd66168e390f2', '0xc3c8e0a39769e2308869f7461364ca48155d1d9e', '0x2e581a5ae722207aa59acd3939771e7c7052dd3d', '0x44592b81c05b4c35efb8424eb9d62538b949ebbf', '0xd5fd1bc99d5801278345e9d29be2225d06c26e93', '0x06a0048079ec6571cd1b537418869cde6191d42d', '0x564286362092d8e7936f0549571a803b203aaced', '0x892e9e24aea3f27f4c6e9360e312cce93cc98ebe', '0x00799bbc833d5b168f0410312d2a8fd9e0e3079c', '0x141fef8cd8397a390afe94846c8bd6f4ab981c48', '0x50d669f43b484166680ecc3670e4766cdb0945ce', '0x2f7e209e0f5f645c7612d7610193fe268f118b28', '0x0681d8db095565fe8a346fa0277bffde9c0edbbf', '0xfe9e8709d3215310075d67e3ed32a380ccf451c8', '0x4e9ce36e442e55ecd9025b9a6e0d88485d628a67', '0xbe0eb53f46cd790cd13851d5eff43d12404d33e8', '0xf977814e90da44bfa03b6295a0616a897441acec', '0x001866ae5b3de6caa5a51543fd9fb64f524f5478', '0x8b99f3660622e21f2910ecca7fbe51d654a1517d', '0xab83d182f3485cf1d6ccdd34c7cfef95b4c08da4', '0xc365c3315cf926351ccaf13fa7d19c8c4058c8e1', '0x61189da79177950a7272c88c6058b96d4bcd6be2', '0x4fabb145d64652a948d72533023f6e7a623c7c53', '0xc9a2c4868f0f96faaa739b59934dc9cb304112ec', '0x47ac0fb4f2d84898e4d9e7b4dab3c24507a6d503', '0xb8c77482e45f1f44de1745f52c74426c631bdd52', '0x0b95993a39a363d99280ac950f5e4536ab5c5566', '0x2f47a1c2db4a3b78cda44eade915c3b19107ddcc', '0xb3f923eabaf178fc1bd8e13902fc5c61d3ddef5b']

def get_balance(address):
    time.sleep(0.5)

    print(f'Getting balance for {address}')

    url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={os.getenv('API_KEY')}"

    response = requests.get(url)
    if response.status_code == 200:
        return float(response.json()['result']) * 10 ** -18
    else:
        return 0

if __name__ == '__main__':
    addresses =  get_addresses()

    load_dotenv()

    data = [(addresses, get_balance(address)) for address in addresses]

    df = pd.DataFrame(data, columns=['addresses', 'balance'])
    df['timestamp'] = datetime.now().strftime("%Y-%m-%d %H%M%S")

    balance_sum = round(df['balance'].sum(), 2)

    print(balance_sum)