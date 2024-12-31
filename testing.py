import pytest
from banking import BankAccount, load_accounts, save_accounts
import os

@pytest.fixture
def setup_accounts():
    """Fixture to create a temporary accounts file."""
    accounts = {
        "user1": {"dollars": 100, "cents": 50, "password": "pass1"},
        "user2": {"dollars": 200, "cents": 75, "password": "pass2"}
    }
    with open("test_accounts.txt", "w") as file:
        save_accounts(accounts, "test_accounts.txt")
    yield accounts
    os.remove("test_accounts.txt")

@pytest.fixture
def setup_account_instance():
    """Fixture to create a BankAccount instance."""
    return BankAccount(100, 50, "password")

def test_account_initialization():
    account = BankAccount(100, 50, "password")
    assert account.dollars == 100
    assert account.cents == 50
    assert account.password == "password"

def test_deposit(setup_account_instance):
    account = setup_account_instance
    account.deposit(20, 75)
    assert account.dollars == 121
    assert account.cents == 25

def test_withdraw(setup_account_instance):
    account = setup_account_instance
    account.withdraw(50, 25)
    assert account.dollars == 50
    assert account.cents == 25

def test_withdraw_insufficient_funds(setup_account_instance):
    account = setup_account_instance
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(200, 0)

def test_transfer_funds(setup_accounts):
    accounts = load_accounts("test_accounts.txt")

    sender_data = accounts["user1"]
    recipient_data = accounts["user2"]

    sender = BankAccount.from_dict(sender_data)
    recipient = BankAccount.from_dict(recipient_data)

    # Transfer 50 dollars and 60 cents from user1 to user2
    sender.withdraw(50, 60)
    recipient.deposit(50, 60)

    # Update accounts
    accounts["user1"] = sender.to_dict()
    accounts["user2"] = recipient.to_dict()
    save_accounts(accounts, "test_accounts.txt")

    updated_accounts = load_accounts("test_accounts.txt")
    assert updated_accounts["user1"]["dollars"] == 49
    assert updated_accounts["user1"]["cents"] == 90
    assert updated_accounts["user2"]["dollars"] == 251
    assert updated_accounts["user2"]["cents"] == 35

def test_load_and_save_accounts(setup_accounts):
    accounts = load_accounts("test_accounts.txt")
    assert "user1" in accounts
    assert accounts["user1"]["dollars"] == 100
    assert accounts["user1"]["cents"] == 50
    assert accounts["user1"]["password"] == "pass1"

    accounts["user3"] = {"dollars": 50, "cents": 25, "password": "pass3"}
    save_accounts(accounts, "test_accounts.txt")
    updated_accounts = load_accounts("test_accounts.txt")
    assert "user3" in updated_accounts
    assert updated_accounts["user3"]["dollars"] == 50
    assert updated_accounts["user3"]["cents"] == 25
    assert updated_accounts["user3"]["password"] == "pass3"
