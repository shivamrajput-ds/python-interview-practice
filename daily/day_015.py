"""
Day 15 - Python Interview Practice

Topics:
- Generators
- yield
- Sets
- Validation
- Duplicate handling
"""


def trusted_models(predictions, threshold):
    seen = set()

    for model_name, score in predictions:
        if score < 0.0 or score > 1.0:
            continue

        if score < threshold:
            continue

        if model_name in seen:
            continue

        seen.add(model_name)
        yield model_name


predictions = [
    ("fraud_v1", 0.92),
    ("spam_v1", 0.81),
    ("fraud_v1", 0.95),
    ("churn_v2", 1.20),
    ("rag_v1", 0.91),
]


if __name__ == "__main__":
    for model in trusted_models(predictions, 0.90):
        print(model)


"""
DAY 15 NOTES

Generator:
    yield produces values one at a time instead of building
    a complete result list.

Set:
    seen = set()

    stores model names that were already yielded.

Validation:
    score < 0.0 or score > 1.0

    skips confidence values outside the valid [0, 1] range.

Threshold:
    score < threshold

    skips low-confidence predictions.

Duplicate handling:
    if model_name in seen:
        continue

Input order remains preserved because predictions are processed
from left to right.

Important correction:

    0.0 > score > 1.0

is wrong because it means the score must be below 0 and above 1
at the same time.

Correct:

    score < 0.0 or score > 1.0
"""
