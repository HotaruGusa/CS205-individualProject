import course
import student


class Registration:
    
    def __init__(self, student, course):
        self.student = course
        self.course = course

    def get_student(self):
        return self.student

    def get_course(self):
        return self.course
