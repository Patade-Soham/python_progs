students = {}

while True:
    print("\n1. Add 2. Update 3. View 4. Exit")
    ch = input("Enter choice: ")

    if ch == '1':
        name = input("Name: ")
        grade = input("Grade: ")
        attendance = int(input("Attendance: "))
        students[name] = {'grade': grade, 'attendance': attendance}
    elif ch == '2':
        name = input("Student name to update: ")
        if name in students:
            students[name]['grade'] = input("New grade: ")
            students[name]['attendance'] = int(input("New attendance: "))
    elif ch == '3':
        print(students)
    elif ch == '4':
        break
