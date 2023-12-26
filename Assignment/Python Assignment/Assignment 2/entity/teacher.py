class Teacher:
    def __init__(self, teacher_id, first_name, last_name, email):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.assigned_courses = []

    def update_teacher_info(self, name, email, expertise):
        # Updates teacher information
        self.first_name = name.split()[0]
        self.last_name = name.split()[1]
        self.email = email

    def display_teacher_info(self):
        # Displays detailed information about the teacher
        print(f"Teacher ID: {self.teacher_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print("Assigned Courses:")
        for course in self.assigned_courses:
            print(f"  - {course.course_name}")

    def get_assigned_courses(self):
        # Retrieves a list of courses assigned to the teacher
        return self.assigned_courses