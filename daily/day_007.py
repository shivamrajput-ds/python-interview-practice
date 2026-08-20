"""
Day 7 - Python Interview Practice
Focus: OOP methods, class variables, classmethod, staticmethod,
instance attribute shadowing, and alternative constructors.
"""


# ---------------------------------------------------------
# 1. Class variable + instance method + classmethod
# ---------------------------------------------------------

class ModelRun:
    count = 0

    def __init__(self, model: str, latency_ms: int):
        self.model = model
        self.latency_ms = latency_ms
        ModelRun.count += 1

    def is_slow(self, threshold: int) -> bool:
        return self.latency_ms > threshold

    @classmethod
    def total_created(cls) -> int:
        return cls.count


r1 = ModelRun("fraud_v1", 180)
r2 = ModelRun("fraud_v2", 320)
r3 = ModelRun("fraud_v1", 250)

print(r1.is_slow(200))           # False
print(r2.is_slow(200))           # True
print(ModelRun.total_created())  # 3


# ---------------------------------------------------------
# 2. Class variable and instance attribute shadowing
# ---------------------------------------------------------

class Model:
    category = "ML"

    def __init__(self, name: str):
        self.name = name

    @classmethod
    def change_category(cls, new_category: str) -> None:
        cls.category = new_category


m1 = Model("fraud")
m2 = Model("spam")

Model.change_category("AI")

print(m1.category)      # AI
print(m2.category)      # AI
print(Model.category)   # AI

# Creates an instance attribute only for m1.
m1.category = "NLP"

print(m1.category)      # NLP
print(m2.category)      # AI
print(Model.category)   # AI


# ---------------------------------------------------------
# 3. Instance method + classmethod
# ---------------------------------------------------------

class Employee:
    company = "OpenAI"

    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    def give_raise(self, percent: int) -> None:
        self.salary += self.salary * percent // 100

    @classmethod
    def change_company(cls, new_company: str) -> None:
        cls.company = new_company


employee = Employee("A", 50000)
employee.give_raise(10)

print(employee.salary)   # 55000

Employee.change_company("DeepMind")
print(Employee.company)  # DeepMind


# ---------------------------------------------------------
# 4. Static method
# ---------------------------------------------------------

class EmployeeValidator:

    @staticmethod
    def greet() -> str:
        return "Welcome"

    @staticmethod
    def is_valid_salary(salary: int) -> bool:
        return salary > 0


validator = EmployeeValidator()

# Static methods can be called through both class and object.
# Neither call automatically passes self or cls.
print(EmployeeValidator.greet())  # Welcome
print(validator.greet())           # Welcome

print(EmployeeValidator.is_valid_salary(50000))  # True
print(EmployeeValidator.is_valid_salary(-100))   # False


# ---------------------------------------------------------
# 5. Alternative constructor using @classmethod
# ---------------------------------------------------------

class EmployeeRecord:
    company = "OpenAI"

    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, text: str):
        name, salary = text.split("-")
        return cls(name, int(salary))


e = EmployeeRecord.from_string("Shivam-50000")

print(e.name)     # Shivam
print(e.salary)   # 50000
print(e.company)  # OpenAI


# ---------------------------------------------------------
# Interview Notes
# ---------------------------------------------------------

"""
Instance method
---------------
- Receives self automatically.
- Use when object-specific data is needed.

Class method
------------
- Receives cls automatically.
- Use when class-level data is needed.
- Commonly used for alternative constructors.

Static method
-------------
- Receives neither self nor cls automatically.
- Use for utility/validation logic related to the class.

Object lookup
-------------
- An object can access attributes/methods defined on its class.
- Example: validator.greet() finds greet() on EmployeeValidator.

Static method binding
---------------------
- Calling a static method through an object does NOT pass that object
  as self.
- EmployeeValidator.greet() and validator.greet() both call the same
  static function without an automatic first argument.

Instance attribute shadowing
----------------------------
- m1.category = "NLP" creates/updates category only on m1.
- It does not change Model.category or m2.category.

Alternative constructor
-----------------------
- EmployeeRecord("Shivam", 50000) is the normal constructor approach.
- EmployeeRecord.from_string("Shivam-50000") is an alternative
  constructor approach.
"""
