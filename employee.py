"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary_type, **kwargs):
        self.name = name
        self.salary_type = salary_type
        self.additional_info = kwargs

    def get_pay(self):
        if self.salary_type == 'monthly':
            return 4000
        elif self.salary_type == 'contract':
            hours_worked = self.additional_info.get('hours_worked', 0)
            hourly_rate = self.additional_info.get('hourly_rate', 0)
            return hours_worked * hourly_rate
        elif self.salary_type == 'monthly_with_commission':
            base_salary = 3000
            commission_rate = self.additional_info.get('commission_rate', 0)
            num_contracts = self.additional_info.get('num_contracts', 0)
            return base_salary + (commission_rate * num_contracts)
        elif self.salary_type == 'contract_with_commission':
            hours_worked = self.additional_info.get('hours_worked', 0)
            hourly_rate = self.additional_info.get('hourly_rate', 0)
            commission_rate = self.additional_info.get('commission_rate', 0)
            num_contracts = self.additional_info.get('num_contracts', 0)
            return (hours_worked * hourly_rate) + (commission_rate * num_contracts)
        elif self.salary_type == 'monthly_with_bonus':
            base_salary = 2000
            bonus = self.additional_info.get('bonus', 0)
            return base_salary + bonus
        elif self.salary_type == 'contract_with_bonus':
            hours_worked = self.additional_info.get('hours_worked', 0)
            hourly_rate = self.additional_info.get('hourly_rate', 0)
            bonus = self.additional_info.get('bonus', 0)
            return (hours_worked * hourly_rate) + bonus
        else:
            return 0  # Unknown salary type

    def __str__(self):
        if self.salary_type == 'monthly':
            return f"{self.name} works on a monthly salary of {self.get_pay()}. Their total pay is {self.get_pay()}."
        elif self.salary_type == 'contract':
            hours_worked = self.additional_info.get('hours_worked', 0)
            hourly_rate = self.additional_info.get('hourly_rate', 0)
            return f"{self.name} works on a contract of {hours_worked} hours at {hourly_rate}/hour. Their total pay is {self.get_pay()}."
        elif self.salary_type == 'monthly_with_commission':
            base_salary = 3000
            commission_rate = self.additional_info.get('commission_rate', 0)
            num_contracts = self.additional_info.get('num_contracts', 0)
            return f"{self.name} works on a monthly salary of {base_salary} and receives a commission for {num_contracts} contract(s) at {commission_rate}/contract. Their total pay is {self.get_pay()}."
        elif self.salary_type == 'contract_with_commission':
            hours_worked = self.additional_info.get('hours_worked', 0)
            hourly_rate = self.additional_info.get('hourly_rate', 0)
            commission_rate = self.additional_info.get('commission_rate', 0)
            num_contracts = self.additional_info.get('num_contracts', 0)
            return f"{self.name} works on a contract of {hours_worked} hours at {hourly_rate}/hour and receives a commission for {num_contracts} contract(s) at {commission_rate}/contract. Their total pay is {self.get_pay()}."
        elif self.salary_type == 'monthly_with_bonus':
            base_salary = 2000
            bonus = self.additional_info.get('bonus', 0)
            return f"{self.name} works on a monthly salary of {base_salary} and receives a bonus commission of {bonus}. Their total pay is {self.get_pay()}."
        elif self.salary_type == 'contract_with_bonus':
            hours_worked = self.additional_info.get('hours_worked', 0)
            hourly_rate = self.additional_info.get('hourly_rate', 0)
            bonus = self.additional_info.get('bonus', 0)
            return f"{self.name} works on a contract of {hours_worked} hours at {hourly_rate}/hour and receives a bonus commission of {bonus}. Their total pay is {self.get_pay()}."

# Create instances of employees with additional information
billie = Employee('Billie', 'monthly')
charlie = Employee('Charlie', 'contract', hours_worked=100, hourly_rate=25)
renee = Employee('Renee', 'monthly_with_commission', num_contracts=4, commission_rate=200)
jan = Employee('Jan', 'contract_with_commission', hours_worked=150, hourly_rate=25, num_contracts=3, commission_rate=220)
robbie = Employee('Robbie', 'monthly_with_bonus', bonus=1500)
ariel = Employee('Ariel', 'contract_with_bonus', hours_worked=120, hourly_rate=30, bonus=600)
