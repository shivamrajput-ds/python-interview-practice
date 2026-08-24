"""
Day 11 - Python Interview Practice

Focus:
- Sets for duplicate detection
- String normalization with strip() and lower()
- Preserving first occurrence and order
- Tuple-based sorting
- sorted() with lambda
- Multi-key sorting
"""


def unique_tags(tags: list[str]) -> list[str]:
    result = []
    seen = set()

    for tag in tags:
        cleaned = tag.strip()
        normalized = cleaned.lower()

        if normalized in seen:
            continue

        seen.add(normalized)
        result.append(cleaned)

    return result


tags = [
    "Python",
    "ML",
    "python",
    "FastAPI",
    "ml",
    "RAG",
    "fastapi",
    "  Python  ",
]

print(unique_tags(tags))
# ['Python', 'ML', 'FastAPI', 'RAG']


def rank_models(models: list[tuple[str, float]]) -> list[tuple[str, float]]:
    return sorted(models, key=lambda x: (-x[1], x[0]))


models = [
    ("fraud_v1", 0.91),
    ("spam_v2", 0.85),
    ("churn_v1", 0.95),
    ("rag_v1", 0.85),
]

ranked_models = rank_models(models)

print(ranked_models)
# [
#     ('churn_v1', 0.95),
#     ('fraud_v1', 0.91),
#     ('rag_v1', 0.85),
#     ('spam_v2', 0.85),
# ]


"""
DAY 11 NOTES

1. Set for duplicate detection
   seen = set()

   if value in seen:
       ...

2. String normalization
   cleaned = tag.strip()
   normalized = cleaned.lower()

3. Preserve first occurrence
   - store normalized value in seen
   - append cleaned original form to result

4. sorted() vs .sort()
   sorted(...)
       -> returns a new list
       -> original input is not mutated

   list.sort()
       -> mutates the original list
       -> returns None

5. Multi-key sorting
   lambda x: (-x[1], x[0])

   -x[1] -> score descending
   x[0]  -> name ascending for ties

6. Python compares tuple sort keys from left to right.
"""
