from unittest import TestCase, main

from student.project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.test_student = Student("Test_student", {})

    def test_if_student_initialised_successfully(self):
        self.assertEqual("Test_student", self.test_student.name)
        self.assertEqual({}, self.test_student.courses)

    def test_if_student_enroll_course_not_added__notes_empty__course_notes_is_N(self):
        res = self.test_student.enroll("Python OOP", [], "N")
        self.assertEqual({"Python OOP": []}, self.test_student.courses)
        self.assertEqual("Course has been added.", res)

    def test_if_student_enroll_course_not_added__notes_not_empty__course_notes_is_N(self):
        res = self.test_student.enroll("Python OOP", ["Testing"], "N")
        self.assertEqual({"Python OOP": []}, self.test_student.courses)
        self.assertEqual("Course has been added.", res)

    def test_if_student_enroll_course_already_added__notes_not_empty__course_notes_is_N(self):
        self.test_student.courses = {"Python OOP": ["Inheritance"]}
        res = self.test_student.enroll("Python OOP", ["Testing"], "N")
        self.assertEqual({"Python OOP": ["Inheritance", "Testing"]}, self.test_student.courses)
        self.assertEqual("Course already added. Notes have been updated.", res)

    def test_if_student_enroll_course_already_added__notes_empty__course_notes_is_N(self):
        self.test_student.courses = {"Python OOP": ["Inheritance"]}
        res = self.test_student.enroll("Python OOP", [], "N")
        self.assertEqual({"Python OOP": ["Inheritance"]}, self.test_student.courses)
        self.assertEqual("Course already added. Notes have been updated.", res)

    def test_if_student_enroll_course_not_added__notes_not_empty__course_notes_is_Y(self):
        self.test_student.courses = {"Python Advanced": ["Inheritance"]}
        res = self.test_student.enroll("Python OOP", ["Testing"], "Y")
        self.assertEqual({'Python Advanced': ['Inheritance'], 'Python OOP': ['Testing']}, self.test_student.courses)
        self.assertEqual("Course and course notes have been added.", res)

    def test_if_student_enroll_course_not_added__notes_empty__course_notes_is_Y(self):
        self.test_student.courses = {"Python Advanced": ["Inheritance"]}
        res = self.test_student.enroll("Python OOP", [], "Y")
        self.assertEqual({'Python Advanced': ['Inheritance'], 'Python OOP': []}, self.test_student.courses)
        self.assertEqual("Course and course notes have been added.", res)

    def test_if_student_enroll_course_not_added__notes_not_empty__course_notes_is_empty(self):
        self.test_student.courses = {"Python Advanced": ["Inheritance"]}
        res = self.test_student.enroll("Python OOP", ["Testing"], "")
        self.assertEqual({'Python Advanced': ['Inheritance'], 'Python OOP': ['Testing']}, self.test_student.courses)
        self.assertEqual("Course and course notes have been added.", res)

    def test_if_student_enroll_course_not_added__notes_empty__course_notes_is_empty(self):
        self.test_student.courses = {"Python Advanced": ["Inheritance"]}
        res = self.test_student.enroll("Python OOP", [], "")
        self.assertEqual({'Python Advanced': ['Inheritance'], 'Python OOP': []}, self.test_student.courses)
        self.assertEqual("Course and course notes have been added.", res)

    def test_if_student_add_notes_to_not_existing_course_raises(self):
        self.test_student.courses = {}
        with self.assertRaises(Exception) as ex:
            self.test_student.add_notes("Python OOP", "Testing")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_if_student_add_notes_successfully(self):
        self.test_student.courses = {"Python OOP": []}
        res = self.test_student.add_notes("Python OOP", "Testing")
        self.assertEqual({"Python OOP": ["Testing"]}, self.test_student.courses)
        self.assertEqual("Notes have been updated", res)

    def test_if_student_leave_course_for_not_existing_course_raises(self):
        self.test_student.courses = {}
        with self.assertRaises(Exception) as ex:
            self.test_student.leave_course("Python OOP")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_if_student_leave_course_successfully(self):
        self.test_student.courses = {"Python OOP": ["Inheritance"]}
        res = self.test_student.leave_course("Python OOP")
        self.assertEqual({}, self.test_student.courses)
        self.assertEqual("Course has been removed", res)


if __name__ == '__main__':
    main()