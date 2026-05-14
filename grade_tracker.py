all_grades = { }

def add_student(all_grades):
    name = input("Enter student to add")
    all_grades[name] = {}

def add_grades(all_grades):
    name = input("Enter student to store grade")
    if name not in all_grades:
        print(f"{name} is not in the records add it first")
    else:
        while True:
            sub = input("Enter subject")
            marks = int(input("Enter marks"))
            all_grades[name][sub] = marks
            choice = input("Press Y add more subjects N to end")
            if choice == 'N' or choice == 'n':
                break 
        

def display_std_avg(all_grades):
    if not all_grades:
        print("No students in records")
        return
    name = input("Enter student to find")

    if name not in all_grades:
        print(f"{name} is not in the records add it first")
    else:
        total = 0

        total = sum(all_grades[name].values())        
        print(f"Name : {name} Average: {total/len(all_grades[name])}")

def find_top_student(all_grades):
    if not all_grades:
        print("No students in records")
        return
    top_student = None
    highest_avg = 0
    
    for name, grades in all_grades.items():
        if not grades:  # skip students with no grades
            continue
        
        total = sum(grades.values())
        avg = total / len(grades)
        
        if avg > highest_avg:
            highest_avg = avg
            top_student = name
    
    if top_student:
        print(f"Top student: {top_student} with average {highest_avg}")
    else:
        print("No students have grades yet")

def display_all_std_grades(all_grades):
    for name, grades in all_grades.items():
        print (f"Name : {name}")
        for subject, values in all_grades[name].items():
            print(subject, ":", values)

        


while True:
    print("=======Main Menu=======")
    print("A. Add Student")
    print("B. Add grade for specific subject")
    print("C. Calculate and add students average across all subs")
    print("D. Find and display top student (highest avg)")
    print("E. Display all students and their grades")
    print("F. Quit")
    choice = input("=======Enter Choice=======")

    if choice == 'A':
        add_student(all_grades)

    elif choice == 'B':
        add_grades(all_grades)

    elif choice == 'C':
        display_std_avg(all_grades)

    elif choice == 'D':
        find_top_student(all_grades)

    elif choice == 'E':
        display_all_std_grades(all_grades)

    elif choice == 'F':
        break

    else:
        print("Enter valid Choice")
    
    ch = input("Press Y to continue N to end")
    if ch == 'N' or choice == 'n':
        break 