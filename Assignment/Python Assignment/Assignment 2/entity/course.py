class Course:
    def __init__(self, course_id, course_name, course_code, instructor_name):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.instructor_name = instructor_name
        self.enrollments = []  # List to store references to Enrollment objects
        self.teacher = None

    def assign_teacher(self, teacher):
        # Assigns a teacher to the course
        self.teacher = teacher
        teacher.assigned_courses.append(self)

    def update_course_info(self, course_code, course_name, instructor):
        # Updates course information
        self.course_code = course_code
        self.course_name = course_name
        self.instructor_name = instructor

    def display_course_info(self):
        # Displays detailed information about the course
        print(f"Course ID: {self.course_id}")
        print(f"Course Name: {self.course_name}")
        print(f"Course Code: {self.course_code}")
        print(f"Instructor: {self.instructor_name}")
        if self.teacher:
            print(f"Assigned Teacher: {self.teacher.first_name} {self.teacher.last_name}")
        print("Enrollments:")
        for enrollment in self.enrollments:
            print(f"  - {enrollment.student.first_name} {enrollment.student.last_name}")

    def get_enrollments(self):
        # Retrieves a list of student enrollments for the course
        return self.enrollments

    def get_teacher(self):
        # Retrieves the assigned teacher for the course
        return self.teacher