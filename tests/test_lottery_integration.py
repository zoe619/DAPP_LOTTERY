from brownie import Lottery, network, config, accounts, exceptions
from scripts.deploy_lottery import deploy_lottery, start_lottery
from web3 import Web3
import pytest
from scripts.helpful_scripts import(
     LOCAL_BLOCKCHAIN_ENVIRONMENTS, 
     get_account,
    fund_with_link,
    get_contract
)
import time


def test_can_pick_winner():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    lottery = deploy_lottery()
    account = get_account()
    lottery.start_lottery({"from": account})
    lottery.enter({"from": account, "value": lottery.getEntranceFee()})
    lottery.enter({"from": account, "value": lottery.getEntranceFee()})
    fund_with_link(lottery)
    lottery.end_lottery({"from": account})
    time.sleep(60)
    assert lottery.recentWinner() == account
    assert lottery.balance() == 0
