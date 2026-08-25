"""
Day 12 - Python Interview Practice

Focus:
- OOP inheritance
- super()
- method overriding
- *args
- **kwargs
"""


class Model:
    def __init__(self, name: str):
        self.name = name


class TrainedModel(Model):
    def __init__(self, name: str, score: float):
        super().__init__(name)
        self.score = score

    def is_good(self) -> bool:
        return self.score >= 0.90


model = TrainedModel("fraud_v1", 0.94)

print(model.name)
print(model.score)
print(model.is_good())


class BaseModel:
    def predict(self) -> str:
        return "Base Prediction"


class FraudModel(BaseModel):
    def predict(self) -> str:
        return "Fraud Prediction"


base = BaseModel()
fraud = FraudModel()

print(base.predict())
print(fraud.predict())


def average(*scores: float) -> float:
    if len(scores) == 0:
        return 0

    return sum(scores) / len(scores)


print(average(10, 20, 30))
print(average(5))
print(average())


def build_profile(**details):
    return details


profile = build_profile(
    name="Shivam Rajput",
    role="ML Engineer",
    experience=0,
    cgpa=8.8,
)

print(profile)
print(build_profile())


"""
DAY 12 NOTES

1. Inheritance
   A child class can reuse behavior from a parent class.

2. super()
   super().__init__(name)
   calls the parent class constructor.

3. Method overriding
   A child class can define a method with the same name
   as the parent and provide its own implementation.

4. *args
   Collects positional arguments into a tuple.

   average(10, 20, 30)

   Inside:
       scores == (10, 20, 30)

5. **kwargs
   Collects keyword arguments into a dictionary.

   build_profile(name="Shivam", role="ML Engineer")

   Inside:
       details == {
           "name": "Shivam",
           "role": "ML Engineer"
       }

Memory rule:

    *args
        positional arguments
        tuple

    **kwargs
        keyword arguments
        dictionary
"""
