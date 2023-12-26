from dao.ICourierAdminService import ICourierAdminService
from util.database_connector import DBConnection

class CourierAdminServiceImpl( ICourierAdminService):

    def __init__(self):
        self.conn = DBConnection.getConnection()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def addCustomer(self, userName, email, password, contactNumber, address):
        try:
            query = "INSERT INTO customers (userName, email, password, contactNumber, address) VALUES (%s, %s, %s, %s, %s)"
            values = (userName, email, password, contactNumber, address)
            self.cursor.execute(query, values)
            self.conn.commit()
            return "Customer added successfully"
        except Exception as e:
            return f"Error adding customer: {e}"

    def addCourierStaff(self, employeeObj):
        try:
            query = "INSERT INTO courier_staff (employeeID, employeeName, email, contactNumber, role, salary) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (employeeObj.employeeID, employeeObj.employeeName, employeeObj.email, employeeObj.contactNumber, employeeObj.role, employeeObj.salary)
            self.cursor.execute(query, values)
            self.conn.commit()
            return "Courier staff added successfully"
        except Exception as e:
            return f"Error adding courier staff: {e}"

    def addLocation(self, locationObj):
        try:
            query = "INSERT INTO locations (LocationID, LocationName, Address) VALUES (%s, %s, %s)"
            values = (locationObj.locationID, locationObj.locationName, locationObj.address)
            self.cursor.execute(query, values)
            self.conn.commit()
            return "Location added successfully"
        except Exception as e:
            return f"Error adding location: {e}"
