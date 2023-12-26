class CourierCompanyCollection:
    def __init__(self, company_name):
        self.company_name = company_name
        self.courier_details = []  # List to store Courier objects
        self.employee_details = []  # List to store Employee objects
        self.location_details = []  # List to store Location objects

    def __str__(self):
        return f"CourierCompanyCollection(Name: {self.company_name}, " \
               f"Couriers: {len(self.courier_details)}, Employees: {len(self.employee_details)}, " \
               f"Locations: {len(self.location_details)})"
