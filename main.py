import argparse
from datetime import datetime

from employee import Employee
from employeeDatabase import EmployeeDatabase
from generate_employees import populate_employees


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", type=int, help="Mode of operation")
    parser.add_argument("employee_data", nargs='*', help="Employee data (for modes 2 and 5)")
    args = parser.parse_args()

    db = EmployeeDatabase()

    if args.mode == 1:
        db.create_table()
        print("Table created successfully.")

    elif args.mode == 2:
        if len(args.employee_data) < 3:
            print("Please provide full name, birth date (YYYY-MM-DD), and gender.")
            return
        full_name = args.employee_data[0]
        birth_date = args.employee_data[1]
        gender = args.employee_data[2]

        try:
            employee = Employee(full_name, birth_date, gender)
            employee.save_to_db()
            print("Employee record saved successfully.")
        except Exception as e:
            print(f"Error saving employee: {e}")

    elif args.mode == 3:
        employees = db.get_all_employees()
        print(f"{'Full Name':<30} {'Birth Date':<12} {'Gender':<6} {'Age':<4}")
        for emp in employees:
            full_name, birth_date, gender = emp
            age = datetime.today().year - datetime.strptime(birth_date, "%Y-%m-%d").year
            print(f"{full_name:<30} {birth_date:<12} {gender:<6} {age:<4}")

    elif args.mode == 4:
        employees = populate_employees(999900)  # 1 million with the special ones
        special_employees = populate_employees(100)  # 100 with surname starting with "F"
        db.bulk_insert(employees + special_employees)
        print("Bulk employees inserted successfully.")

    elif args.mode == 5:
        result, exec_time = db.get_filtered_employees("Male", "F")
        print(f"Filtered Employees: {len(result)} found, Execution Time: {exec_time:.4f} seconds")

    else:
        print("Invalid mode. Please use a mode between 1 and 5.")


if __name__ == '__main__':
    main()
