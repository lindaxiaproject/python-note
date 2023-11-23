
class User:
    def __init__(self, name, month_salary):
        self.name = name
        self.month_salary = month_salary

    @property
    def year_salary(self):
        return int(self.month_salary) * 12


if __name__ == '__main__':
    u1 = User("lindaxia", "30000")
    print(u1.year_salary)