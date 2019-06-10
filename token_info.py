#!/usr/bin/env python
import json
from web3.auto import w3

with open("MikeCoin/build/contracts/MikeCoin.json") as f:
    info_json = json.load(f)

abi = info_json["abi"]

# TODO: See if we can get this address from the json file above
address = '0x2b43eE9CC1C0e0F85553b8eC14B5dE7Bb7675B7C'
erc20 = w3.eth.contract(address=address, abi=abi)

first = w3.personal.listAccounts[0]
second = w3.personal.listAccounts[1]

# print the contract name
print('Name:', erc20.functions.name().call())
print('Address:', address)
print('Total supply:', erc20.functions.totalSupply().call())
#print('first address:', first)
#print('second address:', second)
# TODO: These balances do not match the truffle console values
#print('Token balance of first account:', erc20.functions.balanceOf(first).call())
#print('Token balance of second account:', erc20.functions.balanceOf(second).call())
