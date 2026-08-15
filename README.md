# Python Interview Practice

A coding-first repository documenting daily Python interview preparation for **Data Science, Machine Learning, AI/ML, Applied AI, Generative AI, RAG, and junior Python-oriented engineering roles**.

The objective is not to complete another Python course. The objective is to become comfortable writing, debugging, reviewing, and explaining Python under real interview constraints.

---

## What This Repository Builds

This practice focuses on:

- writing correct Python under interview pressure
- debugging unfamiliar code
- understanding Python behavior instead of memorizing syntax
- applying OOP through code
- handling edge cases and invalid inputs
- using Python standard-library modules effectively
- working with files, APIs, exceptions, logging, and testing
- writing clean, readable, PEP 8-style Python
- using NumPy and Pandas for practical data-oriented tasks
- explaining implementation choices clearly to an interviewer

This repository is intentionally **not a DSA repository**. Advanced graph, tree, dynamic-programming, and competitive-programming practice is kept separate.

---

## Practice Style

Sessions are intentionally **coding-heavy and interview-driven**.

Typical exercises include:

- live coding
- debugging
- output prediction
- code review
- Python internals
- OOP implementation
- edge-case handling
- exception handling
- standard-library usage
- API-oriented Python
- Data Science-oriented Python
- lightweight testing

Each daily file contains the cleaned version of the actual interview practice: final solutions, important mistakes, edge cases, visual explanations, and self-checks.

---

## Repository Structure

```text
python-interview-practice/
│
├── README.md
│
├── daily/
│   ├── day_001.py
│   ├── day_002.py
│   └── ...
│
├── debugging/
├── oop/
├── generators_iterators/
├── decorators/
├── context_managers/
├── standard_library/
├── api_python/
├── numpy_pandas/
└── tests/
```

Topic-specific folders will be added naturally as deeper standalone exercises appear. Empty folders are not created only for appearance.

---

# Progress

| Day | Focus | Status |
|---|---|---|
| Day 001 | Dictionary aggregation, missing keys, type hints, mutation vs rebinding, `+=` vs `+` | ✅ Completed |
| Day 002 | OOP, dictionary behavior, mutable defaults, exception handling, truthy/falsy values, numeric edge cases | ✅ Completed |

---

# Day 001

File:

```text
daily/day_001.py
```

## Main Exercise — Event Aggregation

The first coding task summarized API-style event records by event type.

```python
events = [
    {"type": "login", "success": True},
    {"type": "login", "success": False},
    {"type": "purchase", "success": True},
    {"success": True},
    {"type": "", "success": True},
    {"type": "purchase", "success": False},
]
```

Expected result:

```python
{
    "login": {"total": 2, "success": 1},
    "purchase": {"total": 2, "success": 1},
}
```

### Concepts Practiced

- nested dictionary aggregation
- missing-key handling
- single-pass processing
- `dict.get()`
- key existence vs value checking
- type hints
- requirement reading
- clean function design

---

## Safe Dictionary Access

Direct access:

```python
event["success"]
```

raises `KeyError` when the key does not exist.

When a field is optional:

```python
event.get("success", False)
```

can provide a safe default.

This pattern is useful with API responses, metadata, JSON payloads, and real-world data pipelines.

---

## Key Existence vs Falsy Value

These answer different questions:

```python
if "type" not in event:
    ...
```

checks whether the **key exists**.

```python
if not event.get("type"):
    ...
```

checks whether the resulting **value is falsy**.

Common falsy values:

```python
False
None
0
0.0
""
[]
{}
set()
```

---

## Mutation vs Rebinding

```python
a = [10, 20]
b = a
```

does not copy the list.

```text
a -----┐
       ├----> [10, 20]
b -----┘
```

### In-place mutation

```python
def add_score(scores, value):
    scores += [value]
```

For lists, `+=` normally mutates the same list object.

```text
a -----┐
       ├----> [10, 20, 30]
b -----┘
```

Therefore:

```python
a == [10, 20, 30]
b == [10, 20, 30]
a is b
# True
```

### Rebinding

```python
def add_score(scores, value):
    scores = scores + [value]
```

`+` creates a new list and the local name `scores` is rebound to it.

```text
scores --------> [10, 20, 30]

a -----┐
       ├----> [10, 20]
b -----┘
```

After the function returns:

```python
a == [10, 20]
b == [10, 20]
a is b
# True
```

### Interview Vocabulary

- object reference
- shared reference
- mutable object
- in-place mutation
- rebinding
- identity

---

# Day 002

File:

```text
daily/day_002.py
```

Day 002 moved from basic dictionary handling into more realistic Python interview behavior: OOP, hidden edge cases, function defaults, exception handling, and numeric data cleaning.

## 1. Mutation vs Rebinding Verification

A follow-up combined both behaviors:

```python
def update(values):
    values.append(40)
    values = values + [50]
    values.append(60)
```

With:

```python
nums = [10, 20, 30]
update(nums)
```

the caller sees:

```python
[10, 20, 30, 40]
```

Why?

```text
Initial:

nums ------┐
           ├----> [10, 20, 30]
values ----┘

append(40):

nums ------┐
           ├----> [10, 20, 30, 40]
values ----┘

values = values + [50]:

nums ------------> [10, 20, 30, 40]
values ----------> [10, 20, 30, 40, 50]

values.append(60):

nums ------------> [10, 20, 30, 40]
values ----------> [10, 20, 30, 40, 50, 60]
```

This reinforced the difference between **mutating an object** and **rebinding a local name**.

---

## 2. Single-Pass Model Score Aggregation

The task was to return the best valid score for each model while skipping incomplete records.

```python
{
    "fraud_v1": 0.96,
    "fraud_v2": 0.78,
}
```

Skills tested:

- single-pass dictionary aggregation
- missing-value handling
- comparison logic
- avoiding unnecessary intermediate collections
- accurate type hints

---

## 3. OOP — `ModelRegistry`

A class was implemented to:

- store all scores for each model
- add new scores
- return the best score
- return `None` for unknown models
- avoid built-in `max()` as an interview constraint

Conceptually:

```text
ModelRegistry
│
└── predictions
    ├── fraud_v1 -> [0.91, 0.96]
    ├── fraud_v2 -> [0.78]
    └── loss_model -> [-0.7, -0.3]
```

A hidden edge case exposed this unsafe initialization:

```python
result = 0
```

For:

```python
[-0.7, -0.3]
```

that would incorrectly keep `0`.

The robust manual scan used:

```python
result = float("-inf")
```

---

## 4. Mutable Default Arguments

Problematic code:

```python
def register_model(model, models=[]):
    models.append(model)
    return models
```

The default list is created once when the function is defined and may be reused across calls.

Safer pattern:

```python
def register_model(model, models=None):
    if models is None:
        models = []

    models.append(model)
    return models
```

This uses `None` as a sentinel and creates a fresh list when needed.

---

## 5. Dictionary Membership vs `.get()`

Given:

```python
x = {"a": 1, "b": 0}
```

Important behavior:

```python
"a" in x
# True

1 in x
# False

0 in x.values()
# True

x.get("b")
# 0

x.get("c")
# None
```

Dictionary membership checks **keys**, not values.

This condition is dangerous when checking key existence:

```python
if not x.get("b"):
    print("missing")
```

because key `"b"` exists but its value `0` is falsy.

Correct key-existence check:

```python
if "b" in x:
    ...
```

---

## 6. Exception Handling for Data Cleaning

Input:

```python
scores = ["0.91", "bad", None, "0.78", "", "1.0"]
```

Expected:

```python
[0.91, 0.78, 1.0]
```

Clean pattern:

```python
def clean_scores(scores):
    result = []

    for score in scores:
        if score is None:
            continue

        try:
            converted_score = float(score)
        except ValueError:
            continue

        result.append(converted_score)

    return result
```

Important lessons:

- catch specific exceptions
- do not `raise` when the requirement says skip invalid records
- successful conversion itself can be the validation step
- avoid repeatedly calling `float(score)`

---

## 7. Valid Zero vs Truthiness

This check is incorrect for numeric validation:

```python
if float(score):
    ...
```

because:

```python
float("0")
# 0.0

bool(0.0)
# False
```

`0.0` is a valid numeric value even though it is falsy.

Another unnecessary pattern discovered during debugging:

```python
if A or not A:
```

This is always `True`.

---

## 8. `NaN` and Infinity

Python accepts these strings as floating-point values:

```python
float("NaN")
# nan

float("inf")
# inf

float("-inf")
# -inf
```

They do not raise `ValueError`.

When only normal finite values are allowed:

```python
from math import isfinite

if isfinite(value):
    ...
```

can be used.

Example:

```python
["0.8", "NaN", "inf", "-inf", "1.2"]
```

becomes:

```python
[0.8, 1.2]
```

---

## 9. Type-Hint Lessons

Prefer annotations that match the real return type.

```python
dict[str, float]
```

instead of:

```python
dict[str, int]
```

when values are floating-point scores.

If a method may return `None`:

```python
def best(self, model: str) -> float | None:
```

is more accurate than:

```python
def best(self, model: str) -> float:
```

---

# Interview Lessons So Far

### Requirement reading matters

A solution can be logically close and still lose marks if it misses a requirement.

For example, skipping a record with a missing `"success"` field is different from treating that missing value as `False`.

### Edge cases matter

Working for the sample input is not enough.

Examples already encountered:

```text
positive scores only
        ↓
hidden negative-score case
        ↓
result = 0 fails
```

and:

```text
normal numeric strings
        ↓
valid "0"
        ↓
truthiness check fails
```

### Name the actual exception

Instead of:

> "This may give an error."

prefer:

> "`event["success"]` raises a `KeyError` if the key is missing."

### Prefer simple control flow

After:

```python
if model not in self.predictions:
    return None
```

an `else` block is unnecessary because the function has already exited.

---

# Practice Coverage

The repository will progressively cover:

## Core Python

- variables and data types
- truthy/falsy values
- lists
- tuples
- sets and frozensets
- dictionaries
- strings
- loops and conditions
- functions and scope
- `*args` / `**kwargs`
- comprehensions
- sorting
- identity vs equality
- shallow vs deep copying

## Object-Oriented Python

- classes and objects
- instance and class attributes
- instance methods
- `@classmethod`
- `@staticmethod`
- inheritance
- overriding
- `super()`
- encapsulation
- properties
- abstraction
- polymorphism
- dunder methods
- MRO

## Advanced Practical Python

- iterables and iterators
- generators
- `yield`
- decorators
- closures
- context managers
- exception handling
- custom exceptions
- type hints
- dataclasses

## Standard Library

- `collections`
- `functools`
- `itertools`
- `pathlib`
- `os`
- `sys`
- `datetime`
- `json`
- `csv`
- `re`
- `random`
- `math`
- `statistics`
- `logging`

## Applied Python

- `requests`
- JSON handling
- BeautifulSoup
- FastAPI-oriented Python
- file processing
- logging
- pytest
- edge-case handling

## Data Python

- NumPy
- Pandas
- vectorization
- indexing and filtering
- grouping
- merging
- missing-value handling
- practical performance considerations

## Python Internals

Interview-level understanding of:

- mutability
- object references
- identity
- hashing
- memory-management basics
- reference counting
- garbage collection
- CPython basics
- bytecode concept
- GIL basics
- dynamic typing
- duck typing

---

# Running the Practice Files

Clone the repository:

```bash
git clone https://github.com/shivamrajput-ds/python-interview-practice.git
cd python-interview-practice
```

Run Day 1:

```bash
python daily/day_001.py
```

Run Day 2:

```bash
python daily/day_002.py
```

On Windows, `py` can also be used depending on the Python installation:

```bash
py daily/day_002.py
```

---

# Daily Workflow

```text
Interview Question
       ↓
My Attempt
       ↓
Evaluation
       ↓
Follow-up / Hidden Edge Case
       ↓
Debugging
       ↓
Correct Understanding
       ↓
Clean Final Implementation
       ↓
Self-Checks
       ↓
Commit to Repository
```

Example commit:

```bash
git add .
git commit -m "Day 2: OOP, exceptions, dictionary behavior and edge cases"
git push
```

---

# Why This Repository Exists

Strong Python interview performance requires more than remembering syntax.

```text
READ CODE
   ↓
UNDERSTAND BEHAVIOR
   ↓
SPOT EDGE CASES
   ↓
CHOOSE THE RIGHT PYTHON TOOL
   ↓
WRITE CLEAN CODE
   ↓
EXPLAIN THE DECISION
```

This repository documents that progression through consistent, interview-style practice.

---

## Status

**Active — Daily Python Interview Practice**

New coding exercises, debugging cases, OOP implementations, Python internals, libraries, APIs, NumPy/Pandas tasks, and interview notes will be added progressively.
