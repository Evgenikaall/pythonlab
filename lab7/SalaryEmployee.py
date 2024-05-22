from lab7.Employee import Employee


class SalaryEmployee(Employee):
    def __init__(self, name, phone, birth_date, email, specialty, monthly_salary):
        super().__init__(name, phone, birth_date, email, specialty)
        self._monthly_salary = monthly_salary

    @property
    def monthly_salary(self):
        return self._monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, monthly_salary):
        self._monthly_salary = monthly_salary

    def _calculateSalary(self):
        return self._monthly_salary

    def __str__(self):
        return f"SalaryEmployee(Name: {self.name}, Phone: {self.phone}, Birth Date: {self.birth_date}, Email: {self.email}, Specialty: {self.specialty}, Monthly Salary: {self.monthly_salary})"
