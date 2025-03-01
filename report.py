import sys
import csv
from datetime import datetime


def parse_month(month_str: str) -> int:
    """
    Принимает строковое название месяца (англ. вариант, например 'april' или 'April')
    и возвращает номер месяца (1 – январь, 12 – декабрь).
    Можно дополнить, если нужны локализованные названия.
    """
    months_map = {
        "january": 1, "february": 2, "march": 3, "april": 4,
        "may": 5, "june": 6, "july": 7, "august": 8,
        "september": 9, "october": 10, "november": 11, "december": 12
    }
    month_str_lower = month_str.lower()
    return months_map.get(month_str_lower, 0)


def read_employees(file_name: str):
    employees = []
    with open(file_name, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            employees.append({
                "name": row["name"],
                "department": row["department"],
                "birth_date": row["birth_date"],
                "hire_date": row["hire_date"]
            })
    return employees


def main():
    if len(sys.argv) < 3:
        print("Использование: python report.py <database.csv> <month> [-v]")
        sys.exit(1)

    file_name = sys.argv[1]
    month_str = sys.argv[2]
    verbose_flag = "-v" in sys.argv

    month_num = parse_month(month_str)
    if month_num == 0:
        print(f"Ошибка: некорректное название месяца: {month_str}")
        sys.exit(1)

    employees = read_employees(file_name)

    birthdays = []
    anniversaries = []

    for emp in employees:
        birth_month = datetime.strptime(emp["birth_date"], "%Y-%m-%d").month
        hire_month = datetime.strptime(emp["hire_date"], "%Y-%m-%d").month

        if birth_month == month_num:
            birthdays.append(emp)

        if hire_month == month_num:
            anniversaries.append(emp)

    def count_by_department(records):
        dept_count = {}
        for r in records:
            dept = r["department"]
            dept_count[dept] = dept_count.get(dept, 0) + 1
        return dept_count

    bdays_by_dept = count_by_department(birthdays)
    anns_by_dept = count_by_department(anniversaries)

    print(f"Report for {month_str.capitalize()} generated")

    print("--- Birthdays ---")
    print(f"Total: {len(birthdays)}")
    print("By department:")
    for dept, count in bdays_by_dept.items():
        print(f"- {dept}: {count}")
    if verbose_flag and birthdays:
        print("List of employees (birthdays):")
        for emp in birthdays:
            print(f"  {emp['name']} ({emp['department']})")

    print("--- Anniversaries ---")
    print(f"Total: {len(anniversaries)}")
    print("By department:")
    for dept, count in anns_by_dept.items():
        print(f"- {dept}: {count}")
    if verbose_flag and anniversaries:
        print("List of employees (anniversaries):")
        for emp in anniversaries:
            print(f"  {emp['name']} ({emp['department']})")


if __name__ == "__main__":
    main()
