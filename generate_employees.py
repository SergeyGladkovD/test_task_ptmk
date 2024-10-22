import random

from employee import Employee


def populate_employees(n):
    first_names = [
        "Ivan",
        "Petr",
        "Sergey",
        "Dmitry",
        "Alexander",
        "Vladimir",
        "Andrey",
        "Pavel",
        "Mikhail",
        "Nikita",
    ]
    last_names = ["Ivanov", "Petrov", "Sidorov", "Fedorov", "Fabianov", "Fedoseev"]
    genders = ["Male", "Female"]
    employees = []

    for _ in range(n):
        full_name = f"{random.choice(last_names)} {random.choice(first_names)} {random.choice(['Sergeevich', 'Petrovich', 'Nikolaevich'])}"
        birth_date = f"{random.randint(1950, 2000)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
        gender = random.choice(genders)
        employees.append(Employee(full_name, birth_date, gender))

    return employees
