import csv
def add_student():
    pass
def view_students():
    pass
def update_student():
    pass
def delete_student():
    pass
def search_student():
    pass    

print("Student Management CLI")
print("1. Add Student") 
print("2. View Students")
print("3. Update Student")  
print("4. Delete Student")
print("5. Search Student")
print("6. Exit")
ch = int(input("Enter your choice: "))
if ch == 1:
    add_student()
elif ch == 2:
    view_students()
elif ch == 3:
    update_student()
elif ch == 4:
    delete_student()
elif ch == 5:
    search_student()    
elif ch == 6:
    exit()
    
