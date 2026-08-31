"""
Day 14 - Python Interview Practice

Focus:
- Decorators with *args and **kwargs
- Packing vs unpacking
- Preserving return values
- @property
- Property setters
- Validation through setters
"""


# 1. Generic Decorator

def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Exiting {func.__name__}")
        return result

    return wrapper


@log_execution
def predict(model_name: str, score: float) -> bool:
    print(f"{model_name}: {score}")
    return score > 0.90


result = predict("fraud_v1", score=0.94)
print(result)


# 2. @property + Setter Validation

class ModelConfig:
    def __init__(self, threshold: float):
        self.threshold = threshold

    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, new_value):
        if not 0 <= new_value <= 1:
            raise ValueError("Threshold must be between 0 and 1")

        self._threshold = new_value


config = ModelConfig(0.85)

print(config.threshold)

config.threshold = 0.95

print(config.threshold)


"""
DAY 14 NOTES

DECORATOR:
@log_execution is roughly:

    predict = log_execution(predict)

After decoration, predict(...) calls wrapper(...).

PACKING:
    def wrapper(*args, **kwargs)

*args becomes a tuple.
**kwargs becomes a dictionary.

UNPACKING:
    func(*args, **kwargs)

forwards the packed values back as normal arguments.

The wrapper should be generic, but the original function
can keep its normal meaningful parameters.


@property:
    config.threshold

looks like attribute access, but Python calls the getter method.

@threshold.setter:
    config.threshold = 0.95

calls the setter automatically.

Backing attribute:
    self._threshold

stores the real value internally.


IMPORTANT CORRECTION:

This condition is wrong:

    if 0 < new_value > 1:

It means:
    0 < new_value AND new_value > 1

So it catches values above 1, but not values below 0.

Correct:

    if not 0 <= new_value <= 1:
        raise ValueError(...)


Constructor validation:

Instead of:
    self._threshold = threshold

use:
    self.threshold = threshold

so the initial value also passes through the setter.
"""
