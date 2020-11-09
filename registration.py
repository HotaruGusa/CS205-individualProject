import course
import student

class Registration:
  def __init__(self, course, student):
    self.course = course
    self.student = student

  def get_student(self):
    return self.student

  def get_course(self):
    return self.course
