from datetime import datetime
from entity.enrollment import Enrollment
from entity.payment import Payment

class Student:
    def __init__(self, student_id, first_name, last_name, date_of_birth, email, phone_number):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number
        self.enrolled_courses = []
        self.enrollments = []  # List to store references to Enrollment objects
        self.payment_history = []

    def enroll_in_course(self, course):
        # Enrolls the student in a course
        enrollment_date = datetime.now().strftime("%Y-%m-%d")
        enrollment = Enrollment(enrollment_id=len(self.enrolled_courses) + 1, student=self, course=course, enrollment_date=enrollment_date)
        self.enrolled_courses.append(enrollment)

    def update_student_info(self, first_name, last_name, date_of_birth, email, phone_number):
        # Updates the student's information
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number

    def make_payment(self, amount, payment_date):
        # Records a payment made by the student
        payment = Payment(payment_id=len(self.payment_history) + 1, student=self, amount=amount, payment_date=payment_date)
        self.payment_history.append(payment)

    def display_student_info(self):
        # Displays detailed information about the student
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")
        print("Enrolled Courses:")
        for enrollment in self.enrolled_courses:
            print(f"  - {enrollment.course.course_name}")
        print("Payment History:")
        for payment in self.payment_history:
            print(f"  - Amount: {payment.amount}, Date: {payment.payment_date}")

    def get_enrolled_courses(self):
        # Retrieves a list of courses in which the student is enrolled
        return [enrollment.course for enrollment in self.enrolled_courses]

    def get_payment_history(self):
        # Retrieves a list of payment records for the student
        return self.payment_history
