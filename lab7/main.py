import re

from lab7.Employee import Employee
from lab7.HourlyEmployee import HourlyEmployee
from lab7.SalaryEmployee import SalaryEmployee
def validate_input(pattern, input_text, prompt):
    while not re.fullmatch(pattern, input_text):
        input_text = input(prompt)
    return input_text


def create_employee():
    name = validate_input(r'^[A-Za-z]+$', input("Введите имя: "), "Неправильный формат имени. Попробуйте снова: ")
    phone = validate_input(r'^\+373\d{8}$', input("Введите телефон (+373XXXXXXXXX): "), "Неправильный формат телефона. Попробуйте снова: ")
    birth_date = validate_input(r'^\d{2}\.\d{2}\.\d{4}$', input("Введите дату рождения (дд.мм.гггг): "), "Неправильный формат даты рождения. Попробуйте снова: ")
    email = validate_input(r'^[A-Za-z0-9._-]+@[A-Za-z]{4,7}\.[A-Za-z]{2,4}$', input("Введите email: "), "Неправильный формат email. Попробуйте снова: ")
    specialty = validate_input(r'^[A-Za-z]{4,20}$', input("Введите специальность: "), "Неправильный формат специальности. Попробуйте снова: ")
    return Employee(name, phone, birth_date, email, specialty)


def create_hourly_employee():
    name = validate_input(r'^[A-Za-z]+$', input("Введите имя: "), "Неправильный формат имени. Попробуйте снова: ")
    phone = validate_input(r'^\+373\d{8}$', input("Введите телефон (+373XXXXXXXXX): "), "Неправильный формат телефона. Попробуйте снова: ")
    birth_date = validate_input(r'^\d{2}\.\d{2}\.\d{4}$', input("Введите дату рождения (дд.мм.гггг): "), "Неправильный формат даты рождения. Попробуйте снова: ")
    email = validate_input(r'^[A-Za-z0-9._-]+@[A-Za-z]{4,7}\.[A-Za-z]{2,4}$', input("Введите email: "), "Неправильный формат email. Попробуйте снова: ")
    specialty = validate_input(r'^[A-Za-z]{4,20}$', input("Введите специальность: "), "Неправильный формат специальности. Попробуйте снова: ")
    hourly_rate = float(input("Введите почасовую оплату: "))
    hours_worked = float(input("Введите количество отработанных часов: "))
    return HourlyEmployee(name, phone, birth_date, email, specialty, hourly_rate, hours_worked)


def create_salary_employee():
    name = validate_input(r'^[A-Za-z]+$', input("Введите имя: "), "Неправильный формат имени. Попробуйте снова: ")
    phone = validate_input(r'^\+373\d{8}$', input("Введите телефон (+373XXXXXXXXX): "), "Неправильный формат телефона. Попробуйте снова: ")
    birth_date = validate_input(r'^\d{2}\.\d{2}\.\d{4}$', input("Введите дату рождения (дд.мм.гггг): "), "Неправильный формат даты рождения. Попробуйте снова: ")
    email = validate_input(r'^[A-Za-z0-9._-]+@[A-Za-z]{4,7}\.[A-Za-z]{2,4}$', input("Введите email: "), "Неправильный формат email. Попробуйте снова: ")
    specialty = validate_input(r'^[A-Za-z]{4,20}$', input("Введите специальность: "), "Неправильный формат специальности. Попробуйте снова: ")
    monthly_salary = float(input("Введите месячную зарплату: "))
    return SalaryEmployee(name, phone, birth_date, email, specialty, monthly_salary)


def add_employee(employees):
    employee_type = input("Введите тип сотрудника (employee/hourly/salary): ").strip().lower()
    if employee_type == 'employee':
        employees.append(create_employee())
    elif employee_type == 'hourly':
        employees.append(create_hourly_employee())
    elif employee_type == 'salary':
        employees.append(create_salary_employee())
    else:
        print("Неверный тип сотрудника")


def remove_employee(employees):
    name = input("Введите имя сотрудника для удаления: ").strip()
    for employee in employees:
        if employee.name == name:
            employees.remove(employee)
            print(f"Сотрудник {name} удален.")
            return
    print(f"Сотрудник {name} не найден.")


def view_employees():
    employees = []
    try:
        with open("data.txt", "r") as file:
            for line in file:
                employee_data = line.strip().split(',')
                if len(employee_data) == 5:
                    employees.append(Employee(*employee_data))
                elif len(employee_data) == 7 and '.' in employee_data[5]:
                    employees.append(HourlyEmployee(*employee_data))
                elif len(employee_data) == 6 and '.' not in employee_data[5]:
                    employees.append(SalaryEmployee(*employee_data))
    except FileNotFoundError:
        print("Файл не найден. Нет данных для отображения.")
        return

    for employee in employees:
        print(employee)


def save_to_file(employees):
    with open("data.txt", "w") as file:
        for employee in employees:
            if isinstance(employee, HourlyEmployee):
                file.write(f"{employee.name},{employee.phone},{employee.birth_date},{employee.email},{employee.specialty},{employee.hourly_rate},{employee.hours_worked}\n")
            elif isinstance(employee, SalaryEmployee):
                file.write(f"{employee.name},{employee.phone},{employee.birth_date},{employee.email},{employee.specialty},{employee.monthly_salary}\n")
            else:
                file.write(f"{employee.name},{employee.phone},{employee.birth_date},{employee.email},{employee.specialty}\n")


def main():
    employees = []
    while True:
        action = input("Что вы хотите сделать? (add/remove/view/exit): ").strip().lower()
        if action == "add":
            add_employee(employees)
            save_to_file(employees)
        elif action == "remove":
            remove_employee(employees)
            save_to_file(employees)
        elif action == "view":
            view_employees()
        elif action == "exit":
            break
        else:
            print("Неверная команда")


if __name__ == '__main__':
    main()