# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import solana
from solana.rpc.api import Client
# http_client = Client("https://api.devnet.solana.com").
http_client = Client("https://api.mainnet-beta.solana.com")


def connect_to_blockchain():
    # Should connect to the Blockchain. We will use Solana
    if http_client.is_connected():
        print("Connected to Mainnet Solana Blockchain")
    else:
        print("Not Connected to Solana Blockchain")
    print("Block Height is ", http_client.get_block_height())


def search_non_fungible_tokens_to_mint():
    # Scour the Blockchain for Smart Contracts that are NFTs and have the mint function
    print('Search to be implemented')


def run_security_analysis_on_smart_contract():
    # Do some sort of security analysis on the NFT code
    print('Security Checks to be implemented')


def mint_non_fungible_tokens():
    # Out of all the mint-able NFTs, mint at least one
    print('Minting to be implemented')


def connect_to_secondary_market():
    # OpenSea or equivalent.
    print('Connecting to Secondary market to be implemented')
    put_non_fungible_token_on_sale()


def put_non_fungible_token_on_sale():
    # It will have to find the floor price
    print('Putting up for Sale to be implemented')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    connect_to_blockchain()
    search_non_fungible_tokens_to_mint()
    run_security_analysis_on_smart_contract()
    mint_non_fungible_tokens()
    connect_to_secondary_market()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
