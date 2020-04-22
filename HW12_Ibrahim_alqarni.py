""" 
    HW 12 -- Ibrahim Alqaeni
    Data repository of courses, students, instructors, majors and grades. 
    Using Database and show the result on the Brawser 
"""
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/StudentsDetails')
def StudentsDetails():
    db_path = '/Users/ibrah/OneDrive/Desktop/HW12/StudentRepository.sqlite'

    try:
        db = sqlite3.connect(db_path)
    except sqlite3.OperationalError:
        return f"Error: Unable to open the Database at {db_path}"
    else:
        query = """
                select s.Name as Student, s.CWID, g.Course, g.Grade, i.Name as Instructor
                from 
                    students s inner join grades g on s.CWID = g.StudentCWID 
                        inner join instructors i on i.CWID = g.InstructorCWID
                order by s.Name """

        data: Dict[str, str] = [{'student': student, 'cwid': cwid, 'course': course, 'grade': grade, 'instructor': instructor}
                for student, cwid, course, grade, instructor in db.execute(query)]
        db.close()

        return render_template(
                'StudentsDetails.html',
                title='Stevens Students Details',
                header='Stevens Repository',
                table_name='Student, Course, Grade, and Instructor',
                students=data)

app.run(debug=True)