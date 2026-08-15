"""
Day 002 - Python Interview Practice

Topics:
- mutation vs rebinding
- dictionary aggregation
- OOP
- negative-number edge cases
- mutable default arguments
- dictionary membership vs truthy/falsy values
- exception handling
- numeric conversion
- NaN / infinity
- type hints
"""

from math import isfinite


# ============================================================
# Q1 - Mutation vs Rebinding
# ============================================================

def update(values: list[int]) -> None:
    values.append(40)          # mutates the original shared list
    values = values + [50]     # creates a new list; local rebinding
    values.append(60)          # mutates only the new local list


nums = [10, 20, 30]
update(nums)

assert nums == [10, 20, 30, 40]

MUTATION_VISUAL = """
Initially:

nums ------┐
           ├----> [10, 20, 30]
values ----┘

After values.append(40):

nums ------┐
           ├----> [10, 20, 30, 40]
values ----┘

After values = values + [50]:

nums ------------> [10, 20, 30, 40]
values ----------> [10, 20, 30, 40, 50]

After values.append(60):

nums ------------> [10, 20, 30, 40]
values ----------> [10, 20, 30, 40, 50, 60]

Final caller-visible value:
nums == [10, 20, 30, 40]
"""


# ============================================================
# Q2 - Best Score per Model
# ============================================================

def best_scores(
    predictions: list[dict[str, object]],
) -> dict[str, float]:
    result: dict[str, float] = {}

    for prediction in predictions:
        model = prediction.get("model")
        score = prediction.get("score")

        if model is None or score is None:
            continue

        model_name = str(model)
        numeric_score = float(score)

        if (
            model_name not in result
            or numeric_score > result[model_name]
        ):
            result[model_name] = numeric_score

    return result


predictions = [
    {"model": "fraud_v1", "score": 0.91},
    {"model": "fraud_v2", "score": 0.78},
    {"model": "fraud_v1", "score": 0.84},
    {"model": "fraud_v2", "score": None},
    {"score": 0.95},
    {"model": "fraud_v1", "score": 0.96},
]

assert best_scores(predictions) == {
    "fraud_v1": 0.96,
    "fraud_v2": 0.78,
}


# ============================================================
# Q3 - OOP: ModelRegistry
# ============================================================

class ModelRegistry:
    def __init__(self) -> None:
        self.predictions: dict[str, list[float]] = {}

    def add(self, model: str, score: float) -> None:
        if model not in self.predictions:
            self.predictions[model] = []

        self.predictions[model].append(score)

    def best(self, model: str) -> float | None:
        if model not in self.predictions:
            return None

        result = float("-inf")

        for score in self.predictions[model]:
            if score > result:
                result = score

        return result


registry = ModelRegistry()
registry.add("fraud_v1", 0.91)
registry.add("fraud_v2", 0.78)
registry.add("fraud_v1", 0.96)

assert registry.best("fraud_v1") == 0.96
assert registry.best("fraud_v2") == 0.78
assert registry.best("unknown") is None

# Hidden negative-score edge case
registry.add("loss_model", -0.7)
registry.add("loss_model", -0.3)

assert registry.best("loss_model") == -0.3


# Why not result = 0?
#
# If all valid scores are negative:
#
# [-0.7, -0.3]
#
# starting from 0 would incorrectly keep 0.
#
# float("-inf") is safer for a manual maximum scan.


# ============================================================
# Q4 - Mutable Default Argument
# ============================================================

def register_model(
    model: str,
    models: list[str] | None = None,
) -> list[str]:
    if models is None:
        models = []

    models.append(model)
    return models


assert register_model("fraud_v1") == ["fraud_v1"]
assert register_model("fraud_v2") == ["fraud_v2"]


MUTABLE_DEFAULT_NOTE = """
Avoid:

def register_model(model, models=[]):
    ...

The default list is created when the function is defined,
not freshly on every call.

Safer:

def register_model(model, models=None):
    if models is None:
        models = []
"""


# ============================================================
# Q5 - Dictionary Membership vs Value Checking
# ============================================================

x = {"a": 1, "b": 0}

assert ("a" in x) is True
assert (1 in x) is False
assert (0 in x.values()) is True
assert bool(x.get("b")) is False
assert x.get("c") is None


DICTIONARY_NOTE = """
Dictionary membership checks KEYS:

"b" in x

dict.get() retrieves a VALUE:

x.get("b")

If x = {"b": 0}, then:

x.get("b")       -> 0
bool(0)          -> False
not x.get("b")   -> True

So this can be wrong for key-existence checking:

if not x.get("b"):
    print("missing")

because the key exists; its value is only falsy.

Use this when you specifically mean key existence:

if "b" in x:
    ...
"""


# ============================================================
# Q6 - Exception Handling and Numeric Cleaning
# ============================================================

def clean_scores(scores: list[str | None]) -> list[float]:
    result: list[float] = []

    for score in scores:
        if score is None:
            continue

        try:
            converted_score = float(score)
        except ValueError:
            continue

        result.append(converted_score)

    return result


assert clean_scores(
    ["0.91", "bad", None, "0.78", "", "1.0"]
) == [0.91, 0.78, 1.0]

assert clean_scores(
    ["0", "0.0", "bad", None, "", "1.5"]
) == [0.0, 0.0, 1.5]


TRUTHINESS_NOTE = """
Avoid:

if float(score):
    ...

because 0.0 is a valid float but:

bool(0.0) == False

Also avoid:

if A or not A:
    ...

because it is always True.

Clean pattern:

try:
    converted_score = float(score)
except ValueError:
    continue

result.append(converted_score)
"""


# ============================================================
# Q7 - NaN and Infinity
# ============================================================

SPECIAL_FLOAT_NOTE = """
These are valid Python float conversions:

float("NaN")   -> nan
float("inf")   -> inf
float("-inf")  -> -inf

They do not raise ValueError.

To require a normal finite number, use:

math.isfinite(value)
"""


def clean_finite_scores(
    scores: list[str | None],
) -> list[float]:
    result: list[float] = []

    for score in scores:
        if score is None:
            continue

        try:
            converted_score = float(score)
        except ValueError:
            continue

        if not isfinite(converted_score):
            continue

        result.append(converted_score)

    return result


assert clean_finite_scores(
    ["0.8", "NaN", "inf", "-inf", "1.2"]
) == [0.8, 1.2]


# ============================================================
# Type Hint Lessons
# ============================================================

TYPE_HINT_NOTE = """
Prefer accurate return types.

If a function returns floats:

dict[str, float]

not:

dict[str, int]

If a method may return None:

def best(self, model: str) -> float | None:
    ...

Modern Python can use:

list[str]
dict[str, float]
"""


# ============================================================
# Day 002 Key Interview Takeaways
# ============================================================

DAY_002_NOTES = """
1. b = a does not copy a mutable object.
2. append() mutates a list.
3. values = values + [...] creates a new list and rebinds.
4. Manual maximum logic must handle negative values.
5. Mutable default arguments can persist across calls.
6. Dictionary 'in' checks keys.
7. dict.get() checks/retrieves a value, not key existence.
8. 0, 0.0, "", None, [] and {} are falsy.
9. Valid numeric 0.0 must not be rejected accidentally.
10. Catch specific exceptions such as ValueError.
11. float("NaN") and float("inf") succeed.
12. math.isfinite() checks whether a float is finite.
"""

print("Day 002 completed successfully.")
print(MUTATION_VISUAL)
print(MUTABLE_DEFAULT_NOTE)
print(DICTIONARY_NOTE)
print(TRUTHINESS_NOTE)
print(SPECIAL_FLOAT_NOTE)
print(TYPE_HINT_NOTE)
print(DAY_002_NOTES)
