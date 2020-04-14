""" 
    HW 09 -- Ibrahim Alqaeni
    Homework 9 contains 2 tests
"""

import unittest
from HW09_Ibrahim_Alqarni import Repository, Student, Instructor

class TestRepository(unittest.TestCase):

    def setUp(self):
        self.dir = '/Users/ibrah/OneDrive/Desktop/Python_Files'
        self.result = Repository(self.dir, False)

    # I couldn't run it without failure :(
    def test_students_data(self):
        '''A function to test the students data '''
        expected = {'10103': ['10103', 'Baldwin, C', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']], 
                    '10115': ['10115', 'Wyatt, X', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']], 
                    '10172': ['10172', 'Forbes, I', ['SSW 555', 'SSW 567']], 
                    '10175': ['10175', 'Erickson, D', ['SSW 564', 'SSW 567', 'SSW 687']], 
                    '10183': ['10183', 'Chapman, O', ['SSW 689']], 
                    '11399': ['11399', 'Cordova, I', ['SSW 540']], 
                    '11461': ['11461', 'Wright, U', ['SYS 611', 'SYS 750', 'SYS 800']], 
                    '11658': ['11658', 'Kelly, P', ['SSW 540']], 
                    '11714': ['11714', 'Morton, A', ['SYS 611', 'SYS 645']], 
                    '11788': ['11788', 'Fuller, E', ['SSW 540']]}

        result = {cwid: student.info() for cwid, student in self.result._student.items()}
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