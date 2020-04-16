""" 
    HW 09 -- Ibrahim Alqaeni
    Homework 9 contains 3 tests
"""
import unittest
from HHW10_Ibrahim_Alqarni import Repository, Student, Instructor, Major
# The Test didn't Work :(

class TestRepository(unittest.TestCase):

    def setUp(self):
        self.dir = "C:/Users/ibrah/OneDrive/Desktop/Python_Files"
        self.result = Repository(self.dir, False)

    def test_majors_data(self):
        '''A function to test the majors data '''
        expected = [['SFEN', ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']],
                    ['SYEN', ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']]]

        result = [major.info() for major in self.result._major.values()]
        
        self.assertEqual(expected, result)

    def test_students_data(self):
        '''A function to test the students data '''
        expected = [['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [None]],
                    ['10115', 'Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [None]],
                    ['10172', 'Forbes, I', 'SFEN', ['SSW 555', 'SSW 567'], ['SSW 540', 'SSW 564'], ['CS 501', 'CS 513', 'CS 545']],
                    ['10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 513', 'CS 545']],
                    ['10183', 'Chapman, O', 'SFEN', ['SSW 689'], ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']],
                    ['11399', 'Cordova, I', 'SYEN', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], [None]],
                    ['11461', 'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800'], ['SYS 612', 'SYS 671'], ['SSW 540', 'SSW 565', 'SSW 810']],
                    ['11658', 'Kelly, P', 'SYEN', [], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']],
                    ['11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645'], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']],
                    ['11788', 'Fuller, E', 'SYEN', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], [None]]]

        result = [student.info() for student in self.result._student.values()]
        
        self.assertEqual(expected, result)

    def test_instructors_data(self):
        '''A function to test the instructors data '''
        expected = [[['98765', 'Einstein, A', 'SFEN', 'SSW 567', 4],
                    ['98765', 'Einstein, A', 'SFEN', 'SSW 540', 3]],
                    [['98764', 'Feynman, R', 'SFEN', 'SSW 564', 3],
                    ['98764', 'Feynman, R', 'SFEN', 'SSW 687', 3],
                    ['98764', 'Feynman, R', 'SFEN', 'CS 501', 1],
                    ['98764', 'Feynman, R', 'SFEN', 'CS 545', 1]],
                    [['98763', 'Newton, I', 'SFEN', 'SSW 555', 1],
                    ['98763', 'Newton, I', 'SFEN', 'SSW 689', 1]],[],[],
                    [['98760', 'Darwin, C', 'SYEN', 'SYS 800', 1],
                    ['98760', 'Darwin, C', 'SYEN', 'SYS 750', 1],
                    ['98760', 'Darwin, C', 'SYEN', 'SYS 611', 2],
                    ['98760', 'Darwin, C', 'SYEN', 'SYS 645', 1]]]

        result = [list(instructor.info()) for cwid, instructor in self.result._instructor.items()]

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)

