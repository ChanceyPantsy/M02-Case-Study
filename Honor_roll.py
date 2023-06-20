#-----------------------------------------------------------
# Name: Chance Kizer
# File: Honor_roll.py
# This program will prompt user to input student's first name, last name, and GPA.
# The program will check the student's GPA and inform if the student is eligible for the Dean's List or the Honor Roll.
# If the last name input is 'ZZZ', the program will terminate.
#-----------------------------------------------------------

print("Welcome to the GPA tester!")
while True:
    last_name = input("Please type the student's last name. Type 'ZZZ' if you want to stop. ")
    if last_name == "ZZZ" or last_name == "zzz":
        print("Goodbye!")
        break
    first_name = input("Now, please type the student's first name. ")
    gpa_string = input("Lastly, type the student's GPA. ")
    gpa = float(gpa_string)
    if gpa >= 3.5:
        print(first_name + " " + last_name + " has made the Dean's List!")
    elif gpa >= 3.25:
        print(first_name + " " + last_name + " has made the Honor Roll!")
    else:
        print(first_name + " " + last_name + " has not made the Dean's List or the Honor Roll.")
