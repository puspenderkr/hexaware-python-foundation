from abc import ABC, abstractmethod
from entities import Courier, Employee

class ICourierUserService(ABC):
    tracking_number_generator = 1000  # Static variable to generate unique tracking numbers

    @abstractmethod
    def place_order(self, courier_obj):
        pass

    @abstractmethod
    def get_order_status(self, tracking_number):
        pass

    @abstractmethod
    def cancel_order(self, tracking_number):
        pass

    @abstractmethod
    def get_assigned_order(self, courier_staff_id):
        pass
