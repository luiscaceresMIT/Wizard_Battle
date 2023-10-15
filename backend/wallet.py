from web3 import Web3

# Connect to a local Ethereum node (e.g., Ganache)
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# Ensure connection
if not w3.isConnected():
    print("Error: Unable to connect to Ethereum node.")
    exit()

# Contract ABI (Application Binary Interface) - You'll need to compile your Solidity contract to get this
CONTRACT_ABI = []  # Replace with your contract's ABI

# Contract address - Deploy your contract to the Ethereum network and get its address
CONTRACT_ADDRESS = '0xYourContractAddressHere'

# Create a contract object
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

# Set a player's score (example)
def set_player_score(player_address, score):
    tx_hash = contract.functions.setScore(score).transact({'from': player_address})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return receipt

# Get a player's score (example)
def get_player_score(player_address):
    score = contract.functions.getScore(player_address).call()
    return score

# Example usage
if __name__ == "__main__":
    player = '0xPlayerAddressHere'
    set_player_score(player, 100)
    print(get_player_score(player))
