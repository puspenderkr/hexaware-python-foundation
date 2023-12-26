class Enrollment:
    def __init__(self, enrollment_id, student, course, enrollment_date):
        self.enrollment_id = enrollment_id
        self.student = student
        self.course = course
        self.enrollment_date = enrollment_date

    def get_student(self):
        # Retrieves the student associated with the enrollment
        return self.student

    def get_course(self):
        # Retrieves the course associated with the enrollment
        return self.course
