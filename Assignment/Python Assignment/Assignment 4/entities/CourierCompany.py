class CourierCompany:
    def __init__(self, companyName, courierDetails, employeeDetails, locationDetails):
        self.__companyName = companyName
        self.__courierDetails = courierDetails
        self.__employeeDetails = employeeDetails
        self.__locationDetails = locationDetails


    def __str__(self):
        return f"CourierCompany(Name: {self.__companyName}, " \
               f"Couriers: {len(self.__courierDetails)}, Employees: {len(self.__employeeDetails)}, " \
               f"Locations: {len(self.__locationDetails)})"
