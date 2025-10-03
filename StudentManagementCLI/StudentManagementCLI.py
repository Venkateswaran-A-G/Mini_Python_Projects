import csv
def add_student():
    with open('students.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        marks = input("Enter student marks: ")
        grade = input("Enter student grade: ")
        writer.writerow([id, name, age, marks,grade])
        print("Student added successfully.")
def view_students():
    with open('students.csv', mode='r') as file:
        reader = csv.reader(file)
        print("ID\tName\tAge\tMarks\tGrade")
        for row in reader:
            print("\t".join(row))
def delete_student():
    id_to_delete = input("Enter student ID to delete: ")
    rows = []
    with open('students.csv', mode='r') as file:
        reader = csv.reader(file)
        rows = [row for row in reader if row[0] != id_to_delete]
    with open('students.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("Student deleted successfully.")
def search_student():
    id_to_search = input("Enter student ID to search: ")
    with open('students.csv', mode='r') as file:
        reader = csv.reader(file)
        found = False
        for row in reader:
            if row[0] == id_to_search:
                print("ID\tName\tAge\tMarks\tGrade")
                print("\t".join(row))
                found = True
                break
        if not found:
            print("Student not found.")
def main():
    print("Student Management CLI")
    print("1. Add Student") 
    print("2. View Students")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        add_student()
    elif ch == 2:
        view_students()
    elif ch == 3:
        delete_student()
    elif ch == 4:
        search_student()    
    elif ch == 5:
        exit()
    else:
        print("Invalid choice. Please try again.")
while True:
    main()