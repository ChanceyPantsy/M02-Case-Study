#-----------------------------------------------------------
# Name: Chance Kizer
# File: Honor_roll.py
# This program will prompt user to input student's first name, last name, and GPA.
# The program will check the student's GPA and inform if the student is eligible for the Dean's List or the Honor Roll.
# If the last name input is 'ZZZ', the program will terminate.
#-----------------------------------------------------------

def main():
    while True:
        last_name = input("Enter student's last name (or 'ZZZ' to quit): ")
        if last_name.upper() == 'ZZZ':
            break

        first_name = input("Enter student's first name: ")
        gpa = float(input("Enter student's GPA: "))

        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List!")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll!")
        else:
            print(f"{first_name} {last_name} needs to improve GPA to qualify for the Dean's List or Honor Roll.")

if __name__ == "__main__":
    main()
