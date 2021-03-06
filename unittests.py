import unittest
import school
import student
import course

class TestRegistration(unittest.TestCase):
  school = None

  @classmethod
  def setUpClass(cls):
    # called one time, at beginning
    print('setUpClass()')
    cls.school = school.School().get()
    name_1 = 'Yangyi Li'
    name_2 = 'Jerry'
    name_3 = 'Grass'
    gender_a = 'male'
    gender_b = 'male'
    gender_c = 'female'
    cls.student1 = student.Student(name_1, gender_a, 'yli43')
    cls.student2 = student.Student(name_2, gender_b, 'j777')
    cls.student3 = student.Student(name_3, gender_c, 'g690')
    cls.cs201 = course.Course("cs201", "Jason Hibbeler")
    cls.cs205 = course.Course("cs205", "Jason Hibbeler")
    cls.cs011 = course.Course("cs011", "teacher")
    cls.school.add_course(cls.cs201)
    cls.school.add_course(cls.cs205)
    cls.school.add_student(cls.student1)
    cls.school.add_student(cls.student2)
    cls.school.add_student(cls.student3)
    
  @classmethod
  def tearDownClass(cls):
    # called one time, at end
    print('tearDownClass()')
    
  def setUp(self):
    # called before every test
    print('setUp()')

  def tearDown(self):
    # called after every test
    print('tearDown()')

  #-------------------------------------------------------------

  def test_drop(self):
    print('test_drop()')
    # return cs201's student, should return False
    rc = self.school.drop(self.cs201, self.student1)
    self.assertFalse(rc)
    
    # try toreturn cs201's student again, should return False
    rc = self.school.drop(self.cs201, self.student1)
    self.assertFalse(rc)

    # check that the school shows that cs201 has no student register
    students = self.school.get_registrations(self.cs201)
    self.assertEqual(len(students), 0)

    # check that cs201 shows no student register
    students = self.cs201.get_registrations()
    self.assertEqual(len(students), 0)

  #-------------------------------------------------------------

  def testdrop_new(self):
    # register 3 students in cs011
    students = self.school.get_registrations(self.cs011)
    r = self.school.do_registration(self.cs011, self.student1)
    r2 = self.school.do_registration(self.cs011, self.student2)
    r3 = self.school.do_registration(self.cs011, self.student3)
    
    # student1 and student2 drop cs011
    r4 = self.school.drop(self.cs011, self.student1)
    r5 = self.school.drop(self.cs011, self.student2)

    # check how many students in cs011
    students = self.school.get_registrations(self.cs011)
    self.assertEqual(len(students),1 )

    # the last student is student3
    if len(students) == 1:
      self.assertEqual(students[0], self.student3)
  #-------------------------------------------------------------

  def test_registration_one(self):
    print('test_checkout_one()')
    # check that the school shows that no students are register
    students = self.school.get_registrations(self.cs201)
    self.assertEqual(len(students), 0)

    # register one student
    r = self.school.do_registration(self.cs201, self.student1)
    students = self.school.get_registrations(self.cs201)
    self.assertEqual(len(students), 1)

    # check that the school shows one student registration
    if len(students) == 1:
      self.assertEqual(students[0], self.student1)

    # check that cs201 shows one student checked out
    students = self.cs201.get_registrations()
    self.assertEqual(len(students), 1)

    # check that is student1
    if len(students) == 1:
      self.assertEqual(students[0], self.student1)

  #-------------------------------------------------------------

  def test_registration_two(self):
    print('test_checkout_two()')
    # check 205
    r = self.school.do_registration(self.cs205, self.student2)
    self.assertIsNotNone(r)

    # check one student in the cs205
    students = self.school.get_registrations(self.cs205)
    self.assertEqual(len(students), 1)

    #check the  student is student2
    if len(students) == 1:
      self.assertEqual(students[0], self.student2)

    # check registration shows one student register
    students = self.cs205.get_registrations()
    self.assertEqual(len(students), 1)

    # check the registration is student2
    if len(students) == 1:
      self.assertEqual(students[0], self.student2)


  #-------------------------------------------------------------
        
      
if __name__ == "__main__":
  unittest.main()
