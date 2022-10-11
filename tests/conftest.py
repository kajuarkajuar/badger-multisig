from random import random
import pytest
from brownie import Contract, accounts
from brownie_tokens import MintableForkToken
from great_ape_safe import GreatApeSafe
from helpers.addresses import registry


@pytest.fixture(scope="module", autouse=True)
def shared_setup(module_isolation):
    pass


@pytest.fixture
def safe():
    return GreatApeSafe(accounts[9].address)


@pytest.fixture
def dev():
    return GreatApeSafe(registry.eth.badger_wallets.dev_multisig)


@pytest.fixture
def techops():
    return GreatApeSafe(registry.eth.badger_wallets.techops_multisig)


@pytest.fixture
def vault():
    return GreatApeSafe(registry.eth.badger_wallets.treasury_vault_multisig)


@pytest.fixture
def ibbtc_msig():
    return GreatApeSafe(registry.eth.badger_wallets.ibbtc_multisig)


@pytest.fixture
def USDC(safe):
    Contract.from_explorer(registry.eth.treasury_tokens.USDC)
    usdc = MintableForkToken(registry.eth.treasury_tokens.USDC, owner=safe.account)
    usdc._mint_for_testing(safe, 1_000_000 * 10 ** usdc.decimals())
    return Contract(registry.eth.treasury_tokens.USDC, owner=safe.account)
