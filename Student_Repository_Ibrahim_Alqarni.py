""" 
    HW 09 -- Ibrahim Alqaeni
    Data repository of courses, students, and instructors.
"""

from os import path
from prettytable import PrettyTable
from collections import defaultdict
from typing import Dict, DefaultDict
from HW08_Ibrahim_Alqarni import file_reader
import os
from os import listdir, chdir, path
from typing import Iterator, List, IO

class Student:
    ''' a class to store the Student '''
    PT_FIELD_St = ['CWID', 'Name', 'Completed Courses']

    def __init__(self, cwid: str, name: str, major: str):
        self.cwid: str = cwid
        self.name: str = name
        self.major: str = major
        self.course: Dict[str, str] = dict()

    def store_course_grade(self, course: str, grade:str) -> None:
        """ to store the grade of the student which mean that she/he took the course """
        self.course[course] = grade

    def info(self):
        """ to return a list of Student info to add to the pretty table """
        return self.cwid, self.name, self.major, sorted(self.course)


class Instructor:
    ''' a class to store the Instructor '''
    PT_FIELD_In = ['CWID', 'Name', 'Dept', 'Course', 'Students']

    def __init__(self, cwid: str, name: str, dept: str):
        self.cwid: str = cwid
        self.name: str = name
        self.dept: str = dept
        self.course: DefaultDict[str, int] = defaultdict(int)

    def add_inst(self, course: str):
        """ to count the students who toke the course """
        self.course[course] += 1

    def info(self):
        """ a generator to return instructor info to add to the pretty table """
        for course, count in self.course.items():
            yield self.cwid, self.name, self.dept, course, count

class Repository:
    ''' a class to store all info about the student and instructor '''
    def __init__(self, the_dir: str, ptab: bool = True):
        self._the_dir: str = the_dir
        self._student: Dict[str, Student] = dict()
        self._instructor: Dict[str, Instructor] = dict()

        try:
            self._read_student(os.path.join(the_dir, 'students.txt'))
            self._read_instructor(os.path.join(the_dir, 'instructors.txt'))
            self._read_grade(os.path.join(the_dir, 'grades.txt'))

        except ValueError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)

    def student_pre_tab(self):
        ''' to print a pretty table with the students info '''
        pt = PrettyTable(field_names= Student.PT_FIELD_St)

        for name in self._student.values():
            pt.add_row(name.info())
        print(pt)

    def instructor_pre_tab(self):
        ''' to print a pretty table with the instructors info '''
        pt = PrettyTable(field_names= Instructor.PT_FIELD_In)

        for name in self._instructor.values():
            for i in name.info():
                '''if the instructor have multaple courses'''
                pt.add_row(i)
        print(pt)
        
    def _read_student(self, the_dir: str) -> None:
        ''' to read the student info and store it in student dict '''
        for cwid, name, major in file_reader(the_dir, 3, sep='\t', header=False):
            self._student[cwid] = Student(cwid, name, major)

    def _read_instructor(self, the_dir: str) -> None:
        ''' to read the instructor info and store it in instructor dict '''
        for cwid, name, dept in file_reader(the_dir, 3, sep='\t', header=False):
            self._instructor[cwid] = Instructor(cwid, name, dept)

    def _read_grade(self, the_dir: str) -> None:
        ''' to assign the grade to each student and instructor '''
        for stud_cwid, course, grade, inst_cwid in file_reader(the_dir, 4, sep='\t', header=False):
            if stud_cwid in self._student:
                self._student[stud_cwid].store_course_grade(course, grade)
            else:
                raise ValueError(f"can't find the value for the student with the CWID{stud_cwid}")

            if inst_cwid in self._instructor:
                self._instructor[inst_cwid].add_inst(course)
            else:
                raise ValueError(f"can't find the value for the instructor with the CWID{stud_cwid}")


def main():
    the_dir = "C:/Users/ibrah/OneDrive/Desktop/Python_Files"

    Repository(the_dir)

if __name__ == "__main__":
    main()