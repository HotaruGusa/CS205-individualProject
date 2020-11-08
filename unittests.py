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
    rc = self.school.drop(self.cs201, self.student1)
    self.assertFalse(rc)
    
    students = self.school.get_registrations(self.cs201)
    self.assertEqual(len(students), 0)

    students = self.cs201.get_registrations()
    self.assertEqual(len(students), 0)

  #-------------------------------------------------------------

  def testdrop_new(self):
    r = self.school.drop(self.cs201, self.student1)
    self.assertIsNotNone(r)

    students = self.school.get_registrations(self.cs201)
    self.assertEqual(len(students), 2)

    r = self.school.drop(self.cs201, self.student2)
    self.assertIsNotNone(len(students), 1)

    if len(students) == 1:
      self.assertEqual(students[0], self.student3)
  #-------------------------------------------------------------

  def test_registration_one(self):
    print('test_checkout_one()')
    students = self.school.get_registrations(self.cs201)
    self.assertEqual(len(students), 0)

    r = self.school.do_registration(self.cs201, self.student1)
    students = self.school.get_registrations(self.cs201)
    self.assertEqual(len(students), 1)

    if len(students) == 1:
      self.assertEqual(students[0], self.student1)

    students = self.cs201.get_registrations()
    self.assertEqual(len(students), 1)

    if len(students) == 1:
      self.assertEqual(students[0], self.student1)

  #-------------------------------------------------------------

  def test_registration_two(self):
    print('test_checkout_two()')
    r = self.school.do_registration(self.cs205, self.student2)
    self.assertIsNotNone(r)

    students = self.school.get_registrations(self.cs205)
    self.assertEqual(len(students), 2)

    if len(students) == 1:
      self.assertEqual(students[0], self.student2)

    students = self.cs205.get_registrations()
    self.assertEqual(len(students), 1)

    if len(students) == 1:
      self.assertEqual(students[0], self.student2)

  #-------------------------------------------------------------
        
      
if __name__ == "__main__":
  unittest.main()
