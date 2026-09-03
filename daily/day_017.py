"""
Day 17 - Python Interview Practice

Focus:
- @dataclass
- __post_init__()
- collections.Counter
- JSON file writing
- validation
"""


from dataclasses import dataclass
from collections import Counter
import json
import os


# 1. Dataclass + Validation

@dataclass
class ModelResult:
    model_name: str
    accuracy: float
    latency_ms: int

    def __post_init__(self):
        if self.accuracy < 0 or self.accuracy > 1:
            raise ValueError("Accuracy must be between 0 and 1")

        if self.latency_ms < 0:
            raise ValueError("Latency cannot be negative")


result = ModelResult(
    model_name="fraud_v1",
    accuracy=0.94,
    latency_ms=120,
)

print(result)


# 2. Counter -> dict

def prediction_counts(predictions):
    freq = Counter(predictions)
    return dict(freq)


predictions = [
    "fraud",
    "spam",
    "fraud",
    "fraud",
    "churn",
    "spam",
]

print(prediction_counts(predictions))


# 3. Save Metrics to JSON

DATA_DIR = "data"


def save_metrics(file_path, metrics):
    os.makedirs(DATA_DIR, exist_ok=True)
    full_path = os.path.join(DATA_DIR, file_path)

    try:
        with open(full_path, "w", encoding="utf-8") as file:
            json.dump(metrics, file, indent=4)
    except OSError as error:
        print(error)
        return False

    return True


metrics = {
    "model": "fraud_v1",
    "accuracy": 0.94,
    "latency_ms": 120,
}

print(save_metrics("metrics.json", metrics))


"""
DAY 17 NOTES

1. @dataclass
   Automatically generates common methods such as:
   __init__(), __repr__(), and __eq__().

2. __post_init__()
   Runs after the dataclass-generated __init__().
   Useful for validation.

3. Counter
   Counter(values) counts repeated hashable values.
   dict(counter) converts it to a normal dictionary.

4. JSON
   json.dump(data, file, indent=4)
   writes Python data directly to a JSON file.

5. Directory handling
   Writing to data/metrics.json requires the data directory
   to already exist, so os.makedirs(..., exist_ok=True)
   is useful.

6. File-system errors
   OSError is appropriate for general file write failures.

DAY 17 TAKEAWAYS
- dataclasses reduce boilerplate
- __post_init__ supports validation
- Counter simplifies frequency counting
- dict(...) converts Counter to a normal dictionary
- json.dump() serializes Python objects to a file
- indent=4 creates readable JSON
- directories may need to be created before file writing
"""
