import datetime
import re


class Employee:

    def __init__(self, name, phone, birth_date, email, specialty):
        self._name = name
        self._phone = phone
        self._birth_date = birth_date
        self._email = email
        self._specialty = specialty

    def calculateAge(self):
        today = datetime.date.today()
        birth_date = datetime.datetime.strptime(self._birth_date, '%d.%m.%Y').date()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def _calculateSalary(self):
        pass

    # Getters and setters using property() and decorators
    def get_name(self):
        return self._name

    def set_name(self, name):
        if re.fullmatch(r'^[A-Za-z]+$', name):
            self._name = name
        else:
            raise ValueError("Invalid name format")

    name = property(get_name, set_name)

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        if re.fullmatch(r'^\+373\d{8}$', phone):
            self._phone = phone
        else:
            raise ValueError("Invalid phone format")

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        if re.fullmatch(r'^\d{2}\.\d{2}\.\d{4}$', birth_date):
            self._birth_date = birth_date
        else:
            raise ValueError("Invalid birth date format")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if re.fullmatch(r'^[A-Za-z0-9._-]+@[A-Za-z]{4,7}\.[A-Za-z]{2,4}$', email):
            self._email = email
        else:
            raise ValueError("Invalid email format")

    @property
    def specialty(self):
        return self._specialty

    @specialty.setter
    def specialty(self, specialty):
        if re.fullmatch(r'^[A-Za-z]{4,20}$', specialty):
            self._specialty = specialty
        else:
            raise ValueError("Invalid specialty format")

    def __str__(self):
        return f"Employee(Name: {self.name}, Phone: {self.phone}, Birth Date: {self.birth_date}, Email: {self.email}, Specialty: {self.specialty})"

