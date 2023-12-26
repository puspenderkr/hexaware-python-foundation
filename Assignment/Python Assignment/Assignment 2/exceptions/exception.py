class DuplicateEnrollmentException(Exception):
    def __init__(self, student, course):
        super().__init__(f"Student {student.first_name} {student.last_name} is already enrolled in the course {course.course_name}.")

class CourseNotFoundException(Exception):
    def __init__(self, course_id):
        super().__init__(f"Course with ID {course_id} not found.")

class StudentNotFoundException(Exception):
    def __init__(self, student_id):
        super().__init__(f"Student with ID {student_id} not found.")

class TeacherNotFoundException(Exception):
    def __init__(self, teacher_id):
        super().__init__(f"Teacher with ID {teacher_id} not found.")

class PaymentValidationException(Exception):
    def __init__(self, message):
        super().__init__(f"Payment validation failed: {message}")

class InvalidStudentDataException(Exception):
    def __init__(self, message):
        super().__init__(f"Invalid student data: {message}")

class InvalidCourseDataException(Exception):
    def __init__(self, message):
        super().__init__(f"Invalid course data: {message}")

class InvalidEnrollmentDataException(Exception):
    def __init__(self, message):
        super().__init__(f"Invalid enrollment data: {message}")

class InvalidTeacherDataException(Exception):
    def __init__(self, message):
        super().__init__(f"Invalid teacher data: {message}")

class InsufficientFundsException(Exception):
    def __init__(self, student, course, required_amount):
        super().__init__(f"Insufficient funds for student {student.first_name} {student.last_name} to enroll in the course {course.course_name}. Required amount: {required_amount}")
