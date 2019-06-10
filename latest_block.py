#!/usr/bin/env python
from web3.auto import w3
latest = w3.eth.getBlock('latest')
print('block:', w3.eth.blockNumber)
print(latest)
