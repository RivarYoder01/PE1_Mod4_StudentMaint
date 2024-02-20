#!/usr/bin/env python3

"""
Student Maintenance
This module contains the functions for adding, updating, and deleting student data
Example of students = {
    1: {
            'first_name': 'Debbie',
            'last_name': 'Johnson'
        },
    2: {
            'first_name': 'Sam',
            'last_name': 'Smith'
    }
}

GitHub URL: https://github.com/lindllgrn/PE1_Mod4_StudentMaint
"""

import data_validation as dv

# the following are module level dunders (metadata) for the authorship information
__author__ = 'Rivar Yoder | Lindsay Green'
__version__ = '1.0'
__date__ = '2024.02.12'
__status__ = 'Development'

DASH_LENGTH = 35
COLUMN_LENGTH = 60


def list_students(students):
    """
    Display the all student information stored in a 2D list (id, first name, last name)
    It will notify the student if there is no data found.
	
	  ID First Name      Last Name      
	==== =============== ===============
	   1 Debbie          Johnson        
	   2 Sam             Jones          
	   3 Billy           Bob            

    :param students: 2D dictionary {id: {'first_name': value}, {'last_name': value}}
    :return: None
    """

    print(f'{"List Students":>10}')
    print(f'{"-------------":>10}')

    print(f'{"ID": >5} {"First Name":>13} {"Last Name":>10}')
    print('=' * DASH_LENGTH)

    for id, student_data in students.items():
        first_name, last_name = student_data.values()
        first_name = first_name.title()
        last_name = last_name.title()
        print(f'{id:>5} {first_name:>10} {last_name:>10}')

    input("Press enter to continue...")


def add_student(students, next_student_id):
    """
    Display the all student information stored in a 2D list.  It will increment the last student id by one
    and use it as the new student's id.  It also, displays that the student was successfully added.
	
	Add Student
	-----------
	Please enter the Student's First Name: <example if the user enters nothing>
	Invalid Input: Please enter a value!
	Please enter the Student's First Name: Debbie
	Please enter the Student's Last Name: Johnson

	Student ID #1 Debbie Johnson was added.
	Press Enter to continue...
	
    :param students: 2D dictionary {id: {'first_name': value}, {'last_name': value}}
    :param next_student_id: the next student id to be used for the add function
    :return: None
    """

    print('Add Student')
    print('-----------')

    first_name = input('Enter the Students First Name:')
    last_name = input('Enter the Students Last Name:')

    students[next_student_id] = {'first_name': first_name, 'last_name': last_name}

    print('Student ID#', next_student_id, first_name, last_name, 'Was Added')

    return


def update_student(students):
    """
    It will first check to see if there is any student data, and notify the user if no data is found.
    It will then prompt the user for a valid student ID to be updated from the 2D list
    It handles for non-numeric data, and student IDs that do not exist via the find_student_index
    It will prompt the user to confirm they want to update the selected student, and then let the user know
    if the user was successfully updated.
	
	Update Student
	--------------
	Please enter the Student ID to be updated: 1
	Do you want to update Student ID #1 Debbie Johnson (y=Yes, n=No): y
	Please enter the Student's First Name or press enter to keep Debbie: Deb
	Please enter the Student's Last Name or press enter to keep Johnson: <no data entered>

	Student ID #1 Debbie Johnson was update to Deb Johnson
	Press Enter to continue...
	
    :param student_id: 
    :param students: 2D dictionary {id: {'first_name': value}, {'last_name': value}}
    :return: None
    """

    if len(students) == 0:
        print('There are no students to update.')
        return

    print('Update Student')
    print('--------------')

    student_id = dv.get_num('Please enter the Student ID to be updated', data_type="int")

    student = students[student_id]
    first_name, last_name = student.values()

    new_first_name = input(f'Please enter the Student\'s First Name or press enter to keep {first_name}: ').title()
    new_last_name = input(f'Please enter the Student\'s Last Name or press enter to keep {last_name}: ').title()

    if new_first_name > '':
        student['first_name'] = new_first_name

    if new_last_name > '':
        student['last_name'] = new_last_name

    if new_first_name == '' and new_last_name == '':
        print('No Data Changed. Update Cancelled. :(')

    if not dv.get_yes_no(f'Please confirm updating Student ID #{student_id} {first_name} {last_name}'):
        print('Update Cancelled')
        return
    return


def delete_student(students):
    """
    It will first check to see if there is any student data, and notify the user if no data is found.
    It will then prompt the user for a valid student ID to be deleted from the 2D list
    It handles for non-numeric data, and student IDs that do not exist via the find_student_index
    It will prompt the user to confirm they want to delete the selected student, and then let the user know
    if the user was successfully deleted.
	
	Delete Student
	--------------
	Please enter the Student ID to be deleted: 2
	Please confirm deleting Student ID #2 Sam Jones (y=Yes, n=No): y
	Student ID #2 Sam Jones was deleted.
	Press Enter to continue...
	
    :param students: students 2D dictionary {id: {'first_name': value}, {'last_name': value}}
    :return: None
    """

    if len(students) == 0:
        print('There are no students to delete.')
        return

    print('Delete Student')
    print('--------------')

    #if not dv.get_yes_no(f'Please confirm deleting Student ID #{student_id} {first_name} {last_name}'):
     #   print('Update Cancelled')
      #  return

    return


# if this is the module where the program started from, then display the module docstring
if __name__ == '__main__':
    help('student_maintenance')
