#!/usr/bin/env python
from web3.auto import w3
first = w3.personal.listAccounts[0]
second = w3.personal.listAccounts[1]
amount = w3.toWei('0.15', 'ether')
w3.eth.sendTransaction({'to': second, 'from': first, 'value': amount})
print('balance of first account in ether:', w3.fromWei(w3.eth.getBalance(first), 'ether'))
print('balance of second account in ether:', w3.fromWei(w3.eth.getBalance(second), 'ether'))

