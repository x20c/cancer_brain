import csv
from faker import Faker
import random
import datetime


def generate_data(file_name: str, num_records: int = 100):
    fake = Faker("ru_RU")

    departments = ["HR", "Finance", "Engineering", "R&D", "Sales"]

    with open(file_name, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "department", "birth_date", "hire_date"])

        for _ in range(num_records):
            name = fake.name()
            department = random.choice(departments)

            birth_date = fake.date_of_birth(minimum_age=20, maximum_age=65)

            hire_date = fake.date_between_dates(
                date_start=datetime.date(1995, 1, 1),
                date_end=datetime.date.today()
            )

            birth_date_str = birth_date.strftime("%Y-%m-%d")
            hire_date_str = hire_date.strftime("%Y-%m-%d")

            writer.writerow([name, department, birth_date_str, hire_date_str])

    print(f"Данные успешно сгенерированы и записаны в файл: {file_name}")


if __name__ == "__main__":
    generate_data("database.csv", num_records=100)
