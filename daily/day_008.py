"""
Day 8 - Python Interview Practice

Topics:
- Data validation and aggregation
- Case-insensitive skill search
- staticmethod review
- Decorators
- Function references and rebinding
"""


def average_latency(records):
    grouped = {}

    for record in records:
        if "model" not in record or record.get("latency_ms") is None:
            continue

        try:
            latency = float(record["latency_ms"])
        except (TypeError, ValueError):
            continue

        model = record["model"]
        grouped.setdefault(model, []).append(latency)

    return {
        model: sum(latencies) / len(latencies)
        for model, latencies in grouped.items()
    }


records = [
    {"model": "fraud_v1", "latency_ms": 120},
    {"model": "fraud_v2", "latency_ms": "200"},
    {"model": "fraud_v1", "latency_ms": 180},
    {"model": "fraud_v2", "latency_ms": None},
    {"model": "fraud_v1", "latency_ms": "bad"},
    {"latency_ms": 150},
]

print(average_latency(records))
# {'fraud_v1': 150.0, 'fraud_v2': 200.0}


def find_users_by_skill(users, skill):
    result = []

    for user in users:
        if "name" not in user or "skills" not in user:
            continue

        for user_skill in user["skills"]:
            if skill.lower() == user_skill.lower():
                result.append(user["name"])
                break

    return result


users = [
    {"name": "Shivam", "skills": ["Python", "SQL"]},
    {"name": "Aman", "skills": ["Java", "Python"]},
    {"name": "Riya", "skills": []},
    {"name": "Karan"},
    {"skills": ["Python"]},
]

print(find_users_by_skill(users, "python"))
# ['Shivam', 'Aman']


class Employee:
    @staticmethod
    def greet():
        return "Welcome"


e = Employee()

print(Employee.greet())  # Welcome
print(e.greet())         # Welcome

# staticmethod:
# - no automatic self
# - no automatic cls
# - can be called through the class
# - can also be accessed through an existing object


def log_execution(func):
    def wrapper():
        print(func.__name__ + " Function started")
        func()
        print(func.__name__ + " execution ended")

    return wrapper


@log_execution
def train_model():
    print("Training model")


train_model()


"""
DECORATOR MENTAL MODEL

@log_execution
def train_model():
    print("Training model")

is approximately:

def train_model():
    print("Training model")

train_model = log_execution(train_model)


Flow:

1. Original train_model is passed to log_execution.
2. Inside log_execution:
       func -> original train_model
3. wrapper is created.
4. return wrapper returns the wrapper FUNCTION OBJECT.
5. train_model now refers to wrapper.
6. Later train_model() actually runs wrapper().
7. wrapper calls func(), which is the original train_model.

Important:

    return wrapper
        -> return function object, do not run it yet

    wrapper()
        -> run the wrapper

Memory rule:

    @decorator
    def function():
        ...

    means roughly:

    function = decorator(function)
"""


def hello():
    return "Hello"


reference = hello   # function object; not executed
value = hello()     # function executes

print(value)        # Hello
