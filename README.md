## README.md

Random stuff about working with [Ganache](https://www.trufflesuite.com/docs/ganache/quickstart), [Truffle](https://www.trufflesuite.com/docs/truffle/overview), python and [Nightfall](https://github.com/EYBlockchain/nightfall).

# Setup python environment:

```
virtualenv -p python3 venv
source venv/bin/activate
pip install web3
python --version
# when done with virtual environment, run "deactivate"
```

# Use python environment to connect to ganache

https://web3py.readthedocs.io/en/stable/ is your friend

```
netstat | grep 7545
export WEB3_PROVIDER_URI='http://127.0.0.1:7545'
python
from web3.auto import w3
w3.eth.getBlock('latest')
```

# MetaCoin (optional)
Create a simple coin (not ERC20 compliant)

```
mkdir MetaCoin
truffle unbox metacoin
truffle compile
# Note: add workspace to Ganache by clicking the settings (wheel) and adding the truffle-config.js file then re-starting Ganache
truffle migrate
```

# Create MikeToken

```
mkdir MikeToken
cd MikeToken
truffle init
npm init
npm install truffle
# copy over some contracts from /Users/mikekinney/Documents/eth/nightfall/zkp/contracts (and modify)
ERC20Interface.sol    FToken.sol        Migrations.sol        SafeMath.sol
# copy over migrations (and modify)
truffle migrate
```

vi truffle-config.js and add these lines to network section:

        ganache: { // Ganache local test RPC blockchain
            network_id: "5777",
            host: "localhost",
            port: 7545,
            gas: 6721975,
        }

```
truffle build
truffle migrate
truffle console
```

# Truffle Console commands (to ganache)

```
let instance = await MikeCoin.new()
instance.name()

# print the abi
instance.abi

# show total supply
instance.totalSupply().then(s => s.toNumber())

let accounts = await web3.eth.getAccounts()
accounts[0]

# show balance of first account
instance.balanceOf(accounts[0]).then(b => b.toNumber())

# show the instance owner
instance.owner()

# mint some coins for first account
instance.mint(accounts[0], 1)

# transfer 1 coin to second account
instance.transfer(accounts[1], 1)

# show balance of second account
instance.balanceOf(accounts[1]).then(b => b.toNumber())

# burn 1 coin
instance.burn(accounts[0], 1)
```

# Using truffle console to connect to Nightfall
If you want to connect the truffle console to Nightfall's ganache instance, change into the zkp directory and create a `truffle-config.js` file that contains this:

```
module.exports = {
  networks: {
    development: {
      host: "127.0.0.1",
      port: 8545,
      network_id: "*" // Match any network id
    }
  }
};
```

Then connect to the deployed contract:

```
truffle(development)> let instance = await FToken.new()
undefined
truffle(development)> instance.name()
'EY OpsCoin'
truffle(development)>^d
```

(press control-d to quit out of the truffle console)

# Using python scripts
Created some python scripts to connecto to ganache. Just learning how to do it. Probable better ways.

`./latest_block.py` - shows the latest block using python

`./account_balance.py` - shows the account balances using python

`./token_info.py` - interact with the MikeCoin token using python

