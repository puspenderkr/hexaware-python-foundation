class Employee:
    def __init__(self, employeeID, employeeName, email, contactNumber, role, salary):
        self.employeeID = employeeID
        self.employeeName = employeeName
        self.email = email
        self.contactNumber = contactNumber
        self.role = role
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.employeeID}, Name: {self.employeeName}, Email: {self.email}, Role: {self.role}, Salary: {self.salary}"
