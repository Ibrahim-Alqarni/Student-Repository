""" 
    HW 10 -- Ibrahim Alqaeni
    Data repository of courses, students, instructors, majors and grades. 
"""
import os
from prettytable import PrettyTable
from collections import defaultdict
from typing import Dict, DefaultDict, Set, Any, Tuple, Iterator
from HW08_Ibrahim_Alqarni import file_reader


class Major:
    PT_FIELD_In = ['Dept', 'Required', 'Electives']
    pass_grade = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']

    def __init__(self, major):
        self.major: str = major
        self.required = set()
        self.elective = set()

    def add_major(self, flag: str, course: str):
        ''' sort the majors courses between required and elective courses '''
        if flag == 'R':
            self.required.add(course)
        elif flag == 'E':
            self.elective.add(course)
        else:
            raise ValueError(f'wrong flag for the {self.major} major')
    
    def remain_courses(self, courses: Dict[str, str]):
        ''' to test if the student passed the course or not and return:
            the major, completed courses, remaining required and elective courses 
        '''
        complete: Set[str] = set()
        for course, grade in courses.items():
            if grade in Major.pass_grade:
                complete.add(course)

        remain_req = self.required - complete
        remain_elec = self.elective
        if self.elective.intersection(complete):  # if anything in common then met all electives
            remain_elec = set()  # empty set

        return self.major, complete, remain_req, remain_elec

    def info(self):
        ''' to return a list of majors info to add to the pretty table '''
        return self.major, sorted(self.required), sorted(self.elective)


class Student:
    ''' a class to store the Student '''
    PT_FIELD_St = ['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Required', 'Remaining Electives', 'GPA']

    def __init__(self, cwid: str, name: str, major: Major):
        self.cwid: str = cwid
        self.name: str = name
        self.major: Major = major
        self.course: Dict[str, str] = dict()

    def store_course_grade(self, course: str, grade:str) -> None:
        """ to store the grade of the student which mean that she/he took the course """
        self.course[course] = grade

    def info(self):
        """ to return a list of Student info to add to the pretty table """
        major, completed, remain_req, remain_elec = self.major.remain_courses(self.course)
        return self.cwid, self.name, major, sorted(completed), sorted(remain_req), sorted(remain_elec), self.gpa()

    def gpa(self):
        score_gpa = {
                    'A': 4.0,'A-': 3.75,
                    'B+': 3.25, 'B': 3.0, 'B-': 2.75,
                    'C+': 2.25,'C': 2.0,
                    'C-': 0, 'D+': 0, 'D-': 0,'F': 0
                    }
        total: float = 0
        ncourses: int = 0
        for grade in self.course.values():
            total += score_gpa[grade]
            ncourses += 1

        if ncourses > 0:
            return round(total/ncourses, 2)
        else:
            return 0.0

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
        self._major: Dict[str, Major] = dict()


        try:
            self._read_major(os.path.join(the_dir, 'majors.txt'))
            self._read_student(os.path.join(the_dir, 'students.txt'))
            self._read_instructor(os.path.join(the_dir, 'instructors.txt'))
            self._read_grade(os.path.join(the_dir, 'grades.txt'))


        except ValueError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)
        
        if ptab:
            print('\nMajors Summary')
            self.major_pre_tab()

            print('\nStudent Summary')
            self.student_pre_tab()
        
            print('\nInstructor Summary')
            self.instructor_pre_tab()

    
    def major_pre_tab(self):
        ''' to print a pretty table with the students info '''
        pt = PrettyTable(field_names=Major.PT_FIELD_In)

        for name in self._major.values():
            pt.add_row(name.info())

        print(pt)

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
        for cwid, name, major in file_reader(the_dir, 3, sep=';', header=True):
            if major not in self._major:
                print(f'a student with the CWID {cwid} has unknown major')
            else:
                self._student[cwid] = Student(cwid, name, self._major[major])

    def _read_instructor(self, the_dir: str) -> None:
        ''' to read the instructor info and store it in instructor dict '''
        for cwid, name, dept in file_reader(the_dir, 3, sep='|', header=True):
            self._instructor[cwid] = Instructor(cwid, name, dept)

    def _read_grade(self, the_dir: str) -> None:
        ''' to assign the grade to each student and instructor '''
        for stud_cwid, course, grade, inst_cwid in file_reader(the_dir, 4, sep='|', header=True):
            if stud_cwid in self._student:
                self._student[stud_cwid].store_course_grade(course, grade)
            else:
                raise ValueError(f"can't find the value for the student with the CWID{stud_cwid}")

            if inst_cwid in self._instructor:
                self._instructor[inst_cwid].add_inst(course)
            else:
                raise ValueError(f"can't find the value for the instructor with the CWID{stud_cwid}")
    
    def _read_major(self, the_dir: str) -> None:
        ''' to read the major info and store it in major dict '''
        for major, flag, course in file_reader(the_dir, 3, sep='\t', header=True):
            if major not in self._major:
                self._major[major] = Major(major)
            self._major[major].add_major(flag, course)



def main():
    the_dir = "C:/Users/ibrah/OneDrive/Desktop/Python_Files"

    Repository(the_dir)

if __name__ == "__main__":
    main()