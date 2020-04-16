""" 
    HW 11 -- Ibrahim Alqaeni
    Homework 11 contains 3 tests
"""
import unittest
import sqlite3
from HW11_Ibrahim_alqarni import Repository, Student, Instructor, Major


class TestRepository(unittest.TestCase):

    def setUp(self):
        self.dir = '/Users/ibrah/Downloads/DataGrip 2020.1/bin/'
        self.result = Repository(self.dir, False)


    def test_majors_data(self):
        """ A function to test the majors data """
        expected = [['SFEN', ['SSW 540', 'SSW 555', 'SSW 810'], ['CS 501', 'CS 546']],
                    ['CS', ['CS 546', 'CS 570'], ['SSW 565', 'SSW 810']]]

        result = [major.info() for major in self.result._major.values()]

        self.assertEqual(expected, result)

    def test_students_data(self):
        """ A function to test the students data """
        expected = [['10103', 'Jobs, S', 'SFEN', ['CS 501', 'SSW 810'], ['SSW 540', 'SSW 555'], [None]],
                    ['10115', 'Bezos, J', 'SFEN', ['SSW 810'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 546']],
                    ['10183', 'Musk, E', 'SFEN', ['SSW 555', 'SSW 810'], ['SSW 540'], ['CS 501', 'CS 546']],
                    ['11714', 'Gates, B', 'CS', ['CS 546', 'CS 570', 'SSW 810'], [], [None]],
                    ['11717', 'Kernighan, B', 'CS', [], ['CS 546', 'CS 570'], ['SSW 565', 'SSW 810']]]

        result = [student.info() for student in self.result._student.values()]

        self.assertEqual(expected, result)

    def test_instructors_data(self):
        """ A function to test the instructors data """
        expected = [[['98764', 'Cohen, R', 'SFEN', 'CS 546', 1]],
                    [['98763', 'Rowland, J', 'SFEN', 'SSW 810', 4],
                    ['98763', 'Rowland, J', 'SFEN', 'SSW 555', 1]],
                    [['98762', 'Hawking, S', 'CS', 'CS 501', 1],
                    ['98762', 'Hawking, S', 'CS', 'CS 546', 1],
                    ['98762', 'Hawking, S', 'CS', 'CS 570', 1]]]

        result = [list(instructor.info()) for cwid, instructor in self.result._instructor.items()]

        self.assertEqual(expected, result)

    def student_grades_db(self):
        """ A function to test the instructor_table_db """
        db = sqlite3.connect('/Users/ibrah/Downloads/DataGrip 2020.1/bin/StudentRepository.sqlite')

        query = """
                select s.Name as Student_Name, s.CWID, g.Grade, g.Course, i.Name as Instructor_Name
                from 
                    students s inner join grades g on s.CWID = g.StudentCWID 
                        inner join instructors i on i.CWID = g.InstructorCWID
                order by s.Name """

        result = set()

        for row in db.execute(query):
            result.add(row)

        expected = [
            ('Bezos, J','10115','A','SSW 810','Rowland, J')
            ('Bezos, J','10115','F','CS 546','Hawking, S')
            ('Gates, B','11714','B-','SSW 810','Rowland, J')
            ('Gates, B','11714','A','CS 546','Cohen, R')
            ('Gates, B','11714','A-','CS 570','Hawking, S')
            ('Jobs, S','10103','A-','SSW 810','Rowland, J')
            ('Jobs, S','10103','B','CS 501','Hawking, S')
            ('Musk, E','10183','A','SSW 555','Rowland, J')
            ('Musk, E','10183','A','SSW 810','Rowland, J')]

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)

