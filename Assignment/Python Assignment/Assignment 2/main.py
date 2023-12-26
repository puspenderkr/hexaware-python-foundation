from entity.student import Student
from entity.course import Course
from entity.enrollment import Enrollment
from entity.teacher import Teacher
from dao.sis import SIS

def main():
    # Creating an instance of the SIS class
    sis = SIS()

    # Creating students
    student1 = Student(1, "John", "Doe", "2000-01-01", "john.doe@example.com", "123-456-7890")
    student2 = Student(2, "Jane", "Smith", "1999-05-15", "jane.smith@example.com", "987-654-3210")

    # Creating courses
    course1 = Course(101, "Introduction to Python", "PY101", "Instructor Name 1")
    course2 = Course(102, "Advanced Python", "PY102", "Instructor Name 2")

    # Creating teachers
    teacher1 = Teacher(201, "Instructor1", "One", "instructor1@example.com")
    teacher2 = Teacher(202, "Instructor2", "Two", "instructor2@example.com")

    # Adding students, teachers, and courses to the database
    sis.add_student_to_database(student1)
    sis.add_student_to_database(student2)

    sis.add_teacher_to_database(teacher1)
    sis.add_teacher_to_database(teacher2)

    sis.add_course_to_database(course1)
    sis.add_course_to_database(course2)

    # Enrolling students in courses
    sis.enroll_student_in_course(student1, course1)
    sis.enroll_student_in_course(student2, course1)
    sis.enroll_student_in_course(student2, course2)

    # Assigning teachers to courses
    sis.assign_teacher_to_course(teacher1, course1)
    sis.assign_teacher_to_course(teacher2, course2)

    # Recording payments
    sis.record_payment(student1, 500.0, "2023-02-01")
    sis.record_payment(student2, 750.0, "2023-02-15")

    # Generating reports
    enrollment_report = sis.generate_enrollment_report(course1)
    payment_report = sis.generate_payment_report(student2)
    course_statistics = sis.calculate_course_statistics(course1)

    # Displaying information
    print("Student Information:")
    for student in [student1, student2]:
        student.display_student_info()
        print()

    print("Course Information:")
    for course in [course1, course2]:
        course.display_course_info()
        print()

    print("Teacher Information:")
    for teacher in [teacher1, teacher2]:
        teacher.display_teacher_info()
        print()

    print("Enrollment Report:")
    for enrollment in enrollment_report:
        print(f"Student ID: {enrollment.student.student_id}, Course ID: {enrollment.course.course_id}, Enrollment Date: {enrollment.enrollment_date}")
    print()

    print("Payment Report:")
    for payment in payment_report:
        print(f"Student ID: {payment.student.student_id}, Amount: {payment.amount}, Payment Date: {payment.payment_date}")
    print()

    print("Course Statistics:")
    print(f"Enrollment Count: {course_statistics['enrollment_count']}")
    print(f"Total Payments: {course_statistics['total_payments']}")

if __name__ == "__main__":
    main()
