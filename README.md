# Pyteal_Account_Creation_And_Withdraw
A simple decentralized application which allow users to generate account address and to withdraw amount from an account using pyteal.

Smart Contract is written in PyTeal Language.<br/>
PyTeal is a Python based language used to write smart contracts in Algorand Blockchain.

command to run file:
--------------------
**python generate_account.py**<br/>
this will generate account address and private key.

**python withdraw.py**<br/>
this will compile PyTeal code to Teal one and store it in a directory **tealFiles** with the given name.