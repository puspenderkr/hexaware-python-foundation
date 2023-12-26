from entity.enrollment import Enrollment
from entity.payment import Payment

from util.database_connector import DBConnection
from datetime import datetime


class SIS:
    def __init__(self):
        self.conn = DBConnection.getConnection()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def execute_query(self, query, data=None):
        try:
            self.cursor.execute(query, data)
            self.conn.commit()
        except Exception as e:
            print(f"Error executing query: {e}")

    def fetch_query(self, query, data=None):
        result = None
        try:
            self.cursor.execute(query, data)
            result = self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching data: {e}")
        return result
    
    def add_student_to_database(self, student):
        query = "INSERT INTO students (student_id, first_name, last_name, date_of_birth, email, phone_number) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (student.student_id, student.first_name, student.last_name, student.date_of_birth, student.email, student.phone_number)
        self.execute_query(query, data)

    def add_teacher_to_database(self, teacher):
        query = "INSERT INTO teachers (teacher_id, first_name, last_name, email) VALUES (%s, %s, %s, %s)"
        data = (teacher.teacher_id, teacher.first_name, teacher.last_name, teacher.email)
        self.execute_query(query, data)

    def add_course_to_database(self, course):
        query = "INSERT INTO courses (course_id, course_name, course_code, instructor_name) VALUES (%s, %s, %s, %s)"
        data = (course.course_id, course.course_name, course.course_code, course.instructor_name)
        self.execute_query(query, data)

    def enroll_student_in_course(self, student, course):
        enrollment_date = datetime.now().strftime("%Y-%m-%d")
        query = "INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES (%s, %s, %s)"
        data = (student.student_id, course.course_id, enrollment_date)
        self.execute_query(query, data)

    def assign_teacher_to_course(self, teacher, course):
        query = "UPDATE courses SET teacher_id = %s WHERE course_id = %s"
        data = (teacher.teacher_id, course.course_id)
        self.execute_query(query, data)

    def record_payment(self, student, amount, payment_date):
        query = "INSERT INTO payments (student_id, amount, payment_date) VALUES (%s, %s, %s)"
        data = (student.student_id, amount, payment_date)
        self.execute_query(query, data)

    def generate_enrollment_report(self, course):
        query = "SELECT * FROM enrollments WHERE course_id = %s"
        data = (course.course_id,)
        enrollments_data = self.fetch_query(query, data)

        enrollments = []
        for enrollment_data in enrollments_data:
            enrollment = Enrollment(enrollment_data[0], None, None, enrollment_data[3])
            enrollments.append(enrollment)

        return enrollments

    def generate_payment_report(self, student):
        query = "SELECT * FROM payments WHERE student_id = %s"
        data = (student.student_id,)
        payments_data = self.fetch_query(query, data)

        payments = []
        for payment_data in payments_data:
            payment = Payment(payment_data[0], None, payment_data[2], payment_data[3])
            payments.append(payment)

        return payments

    def calculate_course_statistics(self, course):
        query = "SELECT COUNT(*) FROM enrollments WHERE course_id = %s"
        data = (course.course_id,)
        enrollment_count = self.fetch_query(query, data)[0][0]

        query = "SELECT SUM(amount) FROM payments WHERE student_id IN (SELECT student_id FROM enrollments WHERE course_id = %s)"
        total_payments = self.fetch_query(query, data)[0][0]

        return {
            "enrollment_count": enrollment_count,
            "total_payments": total_payments
        }