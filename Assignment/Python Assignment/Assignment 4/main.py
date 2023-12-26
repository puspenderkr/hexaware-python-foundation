from dao.CourierAdminServiceImpl import CourierAdminServiceImpl
from entities.Employee import Employee
from entities.Location import Location

def main():
    # Create an instance of CourierAdminServiceImpl
    courier_admin_service = CourierAdminServiceImpl()

    # Example: Add a customer
    result_customer = courier_admin_service.addCustomer("John Doe", "john@example.com", "password123", "1234567890", "123 Main St")
    print(result_customer)

    # Example: Add a courier staff
    staff_obj = Employee(employeeID=1, employeeName="Courier Staff 1", email="staff1@example.com", contactNumber="9876543210", role="Courier", salary=50000)
    result_staff = courier_admin_service.addCourierStaff(staff_obj)
    print(result_staff)

    # Example: Add a location
    location_obj = Location(locationID=1, locationName="Office 1", address="456 Business St")
    result_location = courier_admin_service.addLocation(location_obj)
    print(result_location)

if __name__ == "__main__":
    main()
