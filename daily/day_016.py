"""
Day 16 - Python Interview Practice

Focus:
- Python dunder methods
- __len__()
- __contains__()
- __str__()
- Custom object behavior
- OOP with sets and dictionaries
"""


class ModelRegistry:
    def __init__(self):
        self.models = set()

    def add(self, model_name):
        self.models.add(model_name)

    def __len__(self):
        return len(self.models)

    def __contains__(self, model_name):
        return model_name in self.models


registry = ModelRegistry()

registry.add("fraud_v1")
registry.add("spam_v2")
registry.add("fraud_v1")

print(len(registry))
print("fraud_v1" in registry)
print("churn_v1" in registry)


class Model:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"Model(name={self.name}, score={self.score})"


model = Model("fraud_v1", 0.94)
print(model)


class ScoreBoard:
    def __init__(self):
        self.models = {}

    def add(self, name, score):
        self.models[name] = score

    def __len__(self):
        return len(self.models)

    def __contains__(self, model_name):
        return model_name in self.models

    def __str__(self):
        return f"ScoreBoard({len(self)} models)"


board = ScoreBoard()

board.add("fraud_v1", 0.91)
board.add("spam_v1", 0.84)
board.add("churn_v1", 0.95)

print(len(board))
print("fraud_v1" in board)
print(board)


"""
DAY 16 NOTES

Dunder methods are special methods with double underscores.

len(obj)
    -> obj.__len__()

value in obj
    -> obj.__contains__(value)

print(obj)
    -> str(obj)
    -> obj.__str__()

A set automatically ignores duplicates, so:

    self.models.add(model_name)

is enough for unique storage.

Direct boolean return:

    return model_name in self.models

is cleaner than a full if/else returning True or False.

Day 16 Takeaways:
- __len__ connects custom objects to len()
- __contains__ connects custom objects to the in operator
- __str__ controls readable object output
- sets are useful for uniqueness
- dictionaries are useful for model -> score storage
- dunder methods make custom classes behave naturally with Python syntax
"""
