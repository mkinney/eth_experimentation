#!/usr/bin/env python
from web3.auto import w3
print('all accounts:', w3.personal.listAccounts)
#print('first account:', w3.personal.listAccounts[0])
#print('balance of first account in wei:', w3.eth.getBalance(w3.personal.listAccounts[0]))
print('balance of first account in ether:', w3.fromWei(w3.eth.getBalance(w3.personal.listAccounts[0]), 'ether'))
print('balance of second account in ether:', w3.fromWei(w3.eth.getBalance(w3.personal.listAccounts[1]), 'ether'))

