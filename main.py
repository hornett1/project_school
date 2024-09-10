import os
import django
from django.contrib import admin

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_school.settings")
django.setup()

from app_school.models import *

while True:
    print("1 - Add Subject")
    print("2 - Add Teacher")
    print("3 - Add Class")
    print("4 - Add student")
    print("5 - Exit")
    choice = input("Choose option")

    if choice == "1":
        name = input("Subject name")
        description = input("Subject's description")

        subject = Subject(subject_name=name, description=description)

        subject.save()

    elif choice == "2":
        name = input("Teacher's name")
        surname = input("Teacher's surname")

        teacher = Teacher(teacher_name=name, teacher_surname=surname, subject=subject)

        teacher.save()

    elif choice == "3":
        name = input("Class' name")
        year = input("Class' year")

        classroom = Class(class_name=name, year=year)

        classroom.save()

    elif choice == "4":
        name = input("Student's name")
        surname = input("Student's surname")
        
        student = Student(student_name=name, student_surname=surname, student_class=classroom)

    elif choice == "5":
        break

    else:
        print("Wrong option")