import random
import logging
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='formatted.log',
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s'
)

class BankAccount:
    def __init__(self):
        self.balance = 100
        print("Hello! Welcome to the ATM Depot!")

    def authenticate(self):
        """Authenticate user with a PIN"""
        while True:
            try:
                pin = int(input("Enter account pin: "))
                if pin != 1234:
                    logger.error(f"Error! {pin} is an invalid PIN. Try again.")
                    print("Error! Invalid PIN. Try again.")
                else:
                    return True 
            except ValueError:
                logger.error("Error! Non-numeric PIN entered.")
                print("Error! Please enter a numeric PIN.")

    def deposit(self):
        """Deposit money into account"""
        try:
            amount = float(input("Enter amount to be deposited: "))
            if amount < 0:
                logger.warning("Warning! Negative deposit amount entered.")
                print("Warning! Cannot deposit a negative amount.")
                return  
            self.balance += amount
            logger.info(f"Amount Deposited: ${amount:.2f}")
            logger.info("Transaction Info: Successful")
            logger.info(f"Transaction #{random.randint(10000, 1000000)}")
            print(f"Successfully deposited ${amount:.2f}")
        except ValueError:
            logger.error("Error! Non-numeric value entered for deposit.")
            print("Error! Please enter a valid number.")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to be withdrawn: "))
            if amount > self.balance:
                logger.error("Error! Insufficient balance.")
                print("Error! Insufficient balance.")
                print("Transaction Failed. Please try again.")
                return  
            self.balance -= amount
            logger.info(f"Amount Withdrawn: ${amount:.2f}")
            logger.info("Transaction Info: Successful")
            logger.info(f"Transaction #{random.randint(10000, 1000000)}")
            print(f"You withdrew: ${amount:.2f}")
        except ValueError:
            logger.error("Error! Non-numeric value entered for withdrawal.")
            print("Error! Please enter a valid number.")

    def display(self):
        logger.info(f"Available Balance: ${self.balance:.2f}")
        print(f"Available Balance: ${self.balance:.2f}")  


acct = BankAccount()
if acct.authenticate():
    acct.deposit()
    acct.withdraw()
    acct.display()
