 # 1. Employee Management System 


employees = []

while True:
    employee_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    department = input("Enter employee Department: ")
    salary = float(input("Enter employee salary: "))

    employee = {
        "id" : employee_id,
        "name" : name,
        "department" : department,
        "salary" : salary
    }

    employees.append(employee)

    choice = input("Do you want to add anther employee? (yes/no): ")

    if choice == "no":
        break

print("\n-------EMPLOYEE LIST-------")

for employee in employees:
    print(f"Employee ID : {employee['id']}")
    print(f"Name : {employee['name']}")
    print(f"Department : {employee['department']}")
    print(f"Salary : {employee['salary']}")
    print("------------------------------------")

search_id = input("\nEnter employee ID to search: ")

found = False

for employee in employees:
    if employee["id"] == search_id:
        print("\n--------EMPLOYEE FOUND---------")
        print(f"Employee ID : {employee['id']}")
        print(f"Name : {employee['name']}")
        print(f"Department : {employee['department']}")
        print(f"Salary : {employee['salary']}")

        found = True
        break

if found == False:
    print("\nEmployee Not Found")

update_id = input("\nEnter employee ID to update: ")

for employee in employees:
    if employee["id"] == update_id:
        employee["name"] = input("Enter new name: ")
        employee["department"] = input("Enter new department: ")
        employee["salary"] = float(input("Enter new salary: "))

while True:
    print("\n======EMPLOYEE MANAGEMENT SYSTEM=======")
    print("1. Add Employee")
    print("2. view Employees" )
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")
        


            




