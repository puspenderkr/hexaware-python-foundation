from abc import ABC, abstractmethod
from typing import List

class IBankServiceProvider(ABC):
    @abstractmethod
    def create_account(self, customer: Customer, acc_no: int, acc_type: str, balance: float):
        pass

    @abstractmethod
    def list_accounts(self) -> List[Account]:
        pass

    @abstractmethod
    def get_account_details(self, account_number: int):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass
