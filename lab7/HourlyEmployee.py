from lab7.Employee import Employee


class HourlyEmployee(Employee):
    def __init__(self, name, phone, birth_date, email, specialty, hourly_rate, hours_worked):
        super().__init__(name, phone, birth_date, email, specialty)
        self._hourly_rate = hourly_rate
        self._hours_worked = hours_worked

    @property
    def hourly_rate(self):
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, hourly_rate):
        self._hourly_rate = hourly_rate

    @property
    def hours_worked(self):
        return self._hours_worked

    @hours_worked.setter
    def hours_worked(self, hours_worked):
        self._hours_worked = hours_worked

    def _calculateSalary(self):
        return self._hourly_rate * self._hours_worked

    def __str__(self):
        return f"HourlyEmployee(Name: {self.name}, Phone: {self.phone}, Birth Date: {self.birth_date}, Email: {self.email}, Specialty: {self.specialty}, Hourly Rate: {self.hourly_rate}, Hours Worked: {self.hours_worked})"
