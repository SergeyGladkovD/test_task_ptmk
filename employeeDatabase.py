import sqlite3
import time


class EmployeeDatabase:
    """Класс база данных."""

    @staticmethod
    def create_table():
        """Создаем базу данных."""
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS employees (
                        id INTEGER PRIMARY KEY,
                        full_name TEXT,
                        birth_date DATE,
                        gender TEXT)""")
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_employees():
        """Получаем всех работников, отсортированных по ФИО."""
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT full_name, birth_date, gender FROM employees ORDER BY full_name""")
        employees = cursor.fetchall()
        conn.close()
        return employees

    @staticmethod
    def bulk_insert(employees):
        """Заполняем базу данных массой значений."""
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()
        cursor.executemany("""
        INSERT INTO employees (full_name, birth_date, gender) VALUES (?, ?, ?)""",
        [(emp.full_name, emp.birth_date, emp.gender) for emp in employees])
        conn.commit()
        conn.close()

    @staticmethod
    def get_filtered_employees(gender, starts_with):
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()
        start_time = time.time()
        cursor.execute("SELECT full_name, birth_date, gender FROM employees WHERE gender=? AND full_name LIKE ?",
                       (gender, starts_with + '%'))
        result = cursor.fetchall()
        execution_time = time.time() - start_time
        conn.close()
        return result, execution_time
