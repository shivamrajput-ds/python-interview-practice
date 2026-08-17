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
- explaining Python decisions clearly to an interviewer

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
├── daily/
│   ├── day_001.py
│   ├── day_002.py
│   ├── day_003.py
│   ├── day_004.py
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
| Day 003 | Generators, lazy iteration, `yield` vs `return`, `next()`, `StopIteration`, memory-efficient processing | ✅ Completed |
| Day 004 | Generator reinforcement, execution timing, shallow copy, deep copy, nested mutability | ✅ Completed |

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

The first `append()` mutates the original shared list. The `+` expression then creates a new list and rebinds only the local name.

---

## 2. Single-Pass Model Score Aggregation

The task returned the best valid score for each model while skipping incomplete records.

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

---

## 9. Type-Hint Lessons

Prefer annotations that match the real return type.

```python
dict[str, float]
```

If a method may return `None`:

```python
def best(self, model: str) -> float | None:
```

---

# Day 003

File:

```text
daily/day_003.py
```

Day 003 focused on **generators and lazy iteration**, especially how Python can process large streams of records without building another complete list in memory.

## 1. Memory-Efficient Filtering with `yield`

The main coding task processed model inference logs and yielded matching records one at a time.

```python
def slow_requests(records, threshold):
    for record in records:
        if (
            "model" not in record
            or "latency_ms" not in record
            or record["latency_ms"] is None
        ):
            continue

        if record["latency_ms"] > threshold:
            yield {
                "model": record["model"],
                "latency_ms": record["latency_ms"],
            }
```

This avoids accumulating every matching record in another list.

---

## 2. Why a List Was Not the Right Tool

A normal list-based approach stores all matching records before returning.

A generator:

```python
yield record
```

can produce one value and pause.

```text
record
  ↓
validate
  ↓
match?
  ↓
yield value
  ↓
PAUSE
  ↓
next()
  ↓
RESUME
```

This is useful for large logs, streaming records, large datasets, API result streams, and data-processing pipelines.

---

## 3. `iter()` vs Generator

```python
iterator = iter(values)
```

creates an iterator over an existing iterable.

But:

```python
list(iter(values))
```

consumes that iterator and creates a list again.

A generator is a **specific kind of iterator** and can be created with a function containing `yield`.

---

## 4. `next()` and Generator State

Given:

```python
def numbers():
    yield 10
    yield 20
    return 30
```

then:

```python
g = numbers()

next(g)  # 10
next(g)  # 20
```

Each `yield` produces a value and pauses the function while preserving its state.

---

## 5. `return` vs `yield` Inside a Generator

```python
yield 30
```

means:

```text
produce 30
    ↓
pause
    ↓
allow future continuation
```

But:

```python
return 30
```

means:

```text
finish generator
    ↓
raise StopIteration(30)
```

So `return 30` does **not** produce `30` as another normal yielded item.

---

## 6. `StopIteration.value`

```python
def demo():
    yield 1
    yield 2
    return 3
```

Then:

```python
g = demo()

print(next(g))
print(next(g))

try:
    print(next(g))
except StopIteration as e:
    print("finished:", e.value)
```

Exact output:

```text
1
2
finished: 3
```

The return value is available through `StopIteration.value`.

---

## 7. What Changes with `yield 3`?

With:

```python
yield 3
```

the third `next()` returns `3` normally.

Only the fourth `next()` raises `StopIteration`.

```text
yield value  → produce value + pause
return value → finish generator + StopIteration(value)
```

---

# Day 004

File:

```text
daily/day_004.py
```

Day 004 reinforced generators and then moved into **copying, nested mutability, shallow copy, and deep copy**.

## 1. Generator Retry — Valid Numeric Scores

The coding task converted valid numeric strings and produced them one at a time.

```python
values = ["0.91", "bad", None, "0", "0.78", ""]
```

Final pattern:

```python
def valid_scores(values):
    for value in values:
        if value is None or value == "":
            continue

        try:
            converted_value = float(value)
        except ValueError:
            continue

        yield converted_value
```

Expected values:

```text
0.91
0.0
0.78
```

The key correction was understanding that:

```python
print(converted_value)
```

only displays a value, while:

```python
yield converted_value
```

produces it for the caller and pauses the generator.

---

## 2. Generator Execution Timing

Given:

```python
def test():
    print("A")
    yield 10
    print("B")
    yield 20
    print("C")
```

and:

```python
g = test()

print("start")
print(next(g))
print("middle")
print(next(g))
```

the exact output is:

```text
start
A
10
middle
B
20
```

Calling `test()` creates a generator object but does not execute the body immediately.

The first `next()` starts execution, and each `yield` pauses the function.

`"C"` is not printed because a third `next()` is never called.

---

## 3. `return` Inside a Generator

```python
def test():
    print("A")
    yield 10
    print("B")
    return 99
```

The first `next()` yields `10`.

The second `next()` reaches:

```python
return 99
```

which ends the generator and raises:

```text
StopIteration(99)
```

The value can be read through:

```python
except StopIteration as e:
    print(e.value)
```

---

## 4. Assignment vs Shallow Copy

```python
x = [1, 2, 3]
y = x
z = x.copy()

x.append(4)
```

Results:

```python
y
# [1, 2, 3, 4]

z
# [1, 2, 3]

x is y
# True

x is z
# False
```

`y = x` creates another reference to the same list.

`x.copy()` creates a new outer list.

---

## 5. Shallow Copy with Nested Objects

Consider:

```python
x = [[1, 2], [3, 4]]
y = x.copy()

x[0].append(99)
```

Both become:

```python
[[1, 2, 99], [3, 4]]
```

because shallow copy creates a new outer list but still shares the nested lists.

```text
x ----------> outer list A ----┐
                               ├----> shared inner list
y ----------> outer list B ----┘
```

Therefore:

```python
x is y
# False

x[0] is y[0]
# True
```

---

## 6. Deep Copy

Using:

```python
import copy

y = copy.deepcopy(x)
```

recursively copies nested mutable objects.

Conceptually:

```text
x ----------> outer list A ----> inner list A

y ----------> outer list B ----> inner list B
```

Now:

```python
x is y
# False

x[0] is y[0]
# False
```

A mutation inside `x` does not affect `y`.

---

## 7. Practical Nested Copy — `add_skill()`

The final coding task required returning an updated nested dictionary without changing the original.

```python
data = {
    "user": {
        "name": "Shivam",
        "skills": ["Python", "SQL"],
    }
}
```

Solution:

```python
import copy

def add_skill(data, skill):
    updated_data = copy.deepcopy(data)
    updated_data["user"]["skills"].append(skill)
    return updated_data
```

After:

```python
updated = add_skill(data, "FastAPI")
```

the original remains:

```python
data["user"]["skills"]
# ["Python", "SQL"]
```

while the copied structure contains:

```python
updated["user"]["skills"]
# ["Python", "SQL", "FastAPI"]
```

The nested skills lists are independent objects.

---

## Day 004 Interview Takeaways

- `print()` and `yield` serve different purposes
- generator bodies begin execution when iteration starts
- `next()` resumes a generator from its previous pause point
- `return value` inside a generator becomes `StopIteration.value`
- assignment does not copy mutable objects
- `.copy()` creates a shallow copy
- shallow copies still share nested mutable objects
- `copy.deepcopy()` recursively copies nested mutable state
- identity checks with `is` help reason about shared objects
- deep copying is useful when nested data must be independently modified

---

# Interview Lessons So Far

### Requirement reading matters

A solution can be logically close and still lose marks if it misses a requirement.

### Edge cases matter

Working for the sample input is not enough. Hidden cases have already included negative values, valid numeric zero, missing dictionary fields, and nested mutable objects.

### Name the actual exception

Instead of:

> "This may give an error."

prefer:

> "`event["success"]` raises a `KeyError` if the key is missing."

### Prefer simple control flow

After an early `return` or `continue`, avoid unnecessary `else` blocks when they do not improve readability.

### Understand object behavior

Python interview questions frequently test whether two names refer to the same object, whether an operation mutates that object, and whether a copy is shallow or deep.

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
- `copy`

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

Run any completed day:

```bash
python daily/day_001.py
python daily/day_002.py
python daily/day_003.py
python daily/day_004.py
```

On Windows, `py` can also be used depending on the Python installation:

```bash
py daily/day_004.py
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
git commit -m "Day 4: generators, shallow copy and deep copy"
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
