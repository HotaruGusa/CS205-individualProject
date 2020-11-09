import registration

class School:
    s_school = None

    @classmethod
    def get(self):
        if self.s_school is None:
            self.s_school = School()
        return self.s_school

    def __init__(self):
        self.students = set()
        self.courses = set()
        self.registrations = set()

    def add_student(self, student):
        self.students.add(student)

    def get_student(self):
        return self.student

    def add_course(self, course):
        self.courses.add(course)

    def get_courses(self):
        return self.courses

    def find_course(self, name):
        for c in self.courses:
            if c.get_name() == name:
                return c
        return None

    def find_student(self, name):
        students = []
        for s in self.students:
            if p.get_name() == name:
                students.append(s)
        return students

    def do_registration(self, c, s):
        if not self.is_registration(s):
          r = registration.Registration(c, s)
          self.registrations.add(r)
          c.do_registration(s)
          return r
        else:
          return None

    def is_registration(self, s):
        for r in self.registrations:
          if r.get_student() == s:
            return True
        return False

    def show_registrations(self):
        for c in self.registrations:
          s = c.get_course().to_string() + ' => ' + c.get_student().to_string()
          print(s)

    def get_registrations(self, c):
        list = []
        for r in self.registrations:
          if r.get_course() == c:
            list.append(r.get_student())
        return list

    def drop(self, c, s):
        for r in self.registrations:
            if r.get_course() == c and r.get_student() == s:
                self.registrations.remove(r)
                return True
        return False
