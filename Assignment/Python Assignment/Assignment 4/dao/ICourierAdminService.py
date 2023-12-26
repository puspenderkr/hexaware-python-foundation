from abc import ABC, abstractmethod

class ICourierAdminService(ABC):

    @abstractmethod
    def addCustomer(self, userName, email, password, contactNumber, address):
        pass

    @abstractmethod
    def addCourierStaff(self, employeeObj):
        pass

    @abstractmethod
    def addLocation(self, locationObj):
        pass
