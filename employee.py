import sqlite3
from datetime import date


class Employee:
    """Класс работник."""
    def __init__(self, full_name, birth_date, gender):
        self.full_name = full_name
        self.birth_date = birth_date
        self.gender = gender

    def calculate_age(self):
        """Вычисляем возраст работника."""
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    def save_to_db(self):
        """Сохраняем работника в базу."""
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO employees (full_name, birth_date, gender) VALUES (?, ?, ?)""",
                       (self.full_name, self.birth_date, self.gender))
        conn.commit()
        conn.close()
