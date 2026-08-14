# Python Interview Practice

A structured, coding-first repository for building strong **Python interview skills** through daily hands-on practice.

This repository focuses on the kind of Python questions commonly asked in **Data Science, Machine Learning, AI/ML, Applied AI, Generative AI, RAG, and Python-oriented junior engineering interviews**.

The goal is not to complete another Python course.

The goal is to become comfortable with:

- writing correct Python under interview pressure
- debugging unfamiliar code
- understanding Python behavior instead of memorizing syntax
- applying OOP through code
- working with dictionaries, lists, sets, strings, functions, generators, decorators, and context managers
- using Python standard-library modules effectively
- handling files, APIs, exceptions, logging, and testing
- writing clean, readable, PEP 8-style code
- using NumPy and Pandas for practical data-oriented problems
- explaining Python decisions clearly to an interviewer

---

## Practice Philosophy

The sessions are intentionally **coding-heavy and interview-driven**.

Typical practice includes:

- live coding
- debugging broken Python
- output prediction
- code review
- Python internals
- OOP implementation
- edge-case handling
- library usage
- API-oriented Python
- Data Science-oriented Python
- testing and clean-code improvements

The repository does **not** aim to duplicate full DSA practice.

Algorithms such as advanced dynamic programming, trees, graphs, and competitive-programming problems are kept separate. Here, small list/string/dictionary problems are used mainly to strengthen Python itself.

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

### `daily/`

Contains the cleaned, final version of each day's interview practice.

Each daily file may include:

- interview question
- final solution
- important edge cases
- corrected implementation
- visual explanation where useful
- key interview takeaways
- lightweight self-checks

### Topic folders

As the repository grows, reusable or deeper exercises will also be organized by topic:

- `debugging/`
- `oop/`
- `generators_iterators/`
- `decorators/`
- `context_managers/`
- `standard_library/`
- `api_python/`
- `numpy_pandas/`
- `tests/`

---

# Progress

| Day | Focus | Status |
|---|---|---|
| Day 001 | Dictionary aggregation, missing keys, type hints, mutation vs rebinding, `+=` vs `+` | ✅ Completed |

This table will grow as new interview sessions are completed.

---

# Day 001

File:

```text
daily/day_001.py
```

## Topics Practiced

### 1. Nested Dictionary Aggregation

Built a function that summarizes event records by event type.

Example input:

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
    "login": {
        "total": 2,
        "success": 1,
    },
    "purchase": {
        "total": 2,
        "success": 1,
    },
}
```

The exercise tested:

- dictionary lookup
- nested dictionary updates
- missing keys
- edge-case handling
- single-pass aggregation
- type hints
- readable function design

---

### 2. Safe Dictionary Access

Direct access:

```python
event["success"]
```

raises:

```text
KeyError
```

when the key does not exist.

Safer access:

```python
event.get("success", False)
```

returns `False` when `"success"` is missing.

This distinction is important in API responses, document metadata, JSON payloads, and real-world data pipelines where fields may be optional.

---

### 3. Key Existence vs Value Checking

These checks are not equivalent:

```python
if "type" not in event:
    ...
```

This checks whether the **key exists**.

```python
if not event.get("type"):
    ...
```

This checks whether the resulting **value is falsy**.

Possible falsy values include:

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

Understanding this distinction prevents subtle dictionary bugs.

---

# Mutation vs Rebinding

One of the most important concepts from Day 001 was understanding what happens when multiple variables reference the same mutable object.

Consider:

```python
a = [10, 20]
b = a
```

No copy is created.

Conceptually:

```text
a -----┐
       ├----> [10, 20]
b -----┘
```

Both names refer to the same list object.

---

## Case 1 — `+=`

```python
def add_score(scores, value):
    scores += [value]
```

After:

```python
add_score(b, 30)
```

the same list is mutated:

```text
a -----┐
       ├----> [10, 20, 30]
b -----┘
```

Therefore:

```python
print(a)
# [10, 20, 30]

print(b)
# [10, 20, 30]

print(a is b)
# True
```

---

## Case 2 — `scores = scores + [value]`

Now consider:

```python
def add_score(scores, value):
    scores = scores + [value]
```

The expression:

```python
scores + [value]
```

creates a **new list**.

Inside the function:

```text
scores --------> [10, 20, 30]

a -----┐
       ├----> [10, 20]
b -----┘
```

The local name `scores` is rebound to the new object.

After the function returns, `a` and `b` still reference the original list:

```python
print(a)
# [10, 20]

print(b)
# [10, 20]

print(a is b)
# True
```

### Interview vocabulary

This difference is best explained using the terms:

- object reference
- shared reference
- mutable object
- in-place mutation
- rebinding
- identity

---

# Interview Lessons from Day 001

### Requirement reading matters

A solution can be logically close but still lose marks if it does not exactly satisfy the requirement.

For example:

```python
if "success" in event:
    ...
```

may avoid a `KeyError`, but simply skipping the record is different from treating the missing value as `False`.

---

### Prefer clean single-pass solutions when appropriate

Avoid creating unnecessary intermediate collections when the same task can be performed clearly in one pass.

Instead of:

```text
filter records
      ↓
create new list
      ↓
iterate again
      ↓
aggregate
```

prefer:

```text
iterate once
      ↓
validate record
      ↓
aggregate immediately
```

when readability remains good.

---

### Know the exception you are preventing

It is not enough to say:

> "This may give an error."

A stronger interview answer is:

> "`event["success"]` raises a `KeyError` if the key is missing, so I can use `dict.get()` with a default value when the field is optional."

---

# Practice Areas

This repository will gradually cover:

## Core Python

- variables and data types
- truthy/falsy values
- lists
- tuples
- sets
- frozensets
- dictionaries
- strings
- loops
- conditions
- functions
- scope
- `*args`
- `**kwargs`
- comprehensions
- sorting
- identity vs equality
- shallow vs deep copying

## Object-Oriented Python

- classes and objects
- instance attributes
- class attributes
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

- iterables
- iterators
- generators
- `yield`
- decorators
- closures
- context managers
- exceptions
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

- API consumption with `requests`
- JSON handling
- BeautifulSoup basics
- FastAPI-oriented Python
- file processing
- logging
- testing with `pytest`
- edge-case handling

## Data Python

- NumPy
- Pandas
- vectorization
- indexing
- filtering
- grouping
- merging
- missing values
- practical performance considerations

## Python Internals

Interview-level understanding of:

- mutability
- object references
- identity
- hashing
- garbage collection basics
- reference counting basics
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

Run a daily practice file:

```bash
python daily/day_001.py
```

For Windows, depending on the Python installation:

```bash
py daily/day_001.py
```

---

# Daily Workflow

The workflow is intentionally simple:

```text
Interview Question
       ↓
My Attempt
       ↓
Evaluation
       ↓
Follow-up / Debugging
       ↓
Correct Understanding
       ↓
Clean Final Implementation
       ↓
Commit to Repository
```

A typical commit:

```bash
git add .
git commit -m "Day 1: dictionary aggregation and object references"
git push
```

---

# Why This Repository Exists

Strong Python interview performance requires more than remembering syntax.

A candidate should be able to:

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

This repository documents that progression through consistent practice.

---

## Status

**Active — Daily Python Interview Practice**

More exercises, debugging cases, OOP implementations, library questions, API tasks, NumPy/Pandas challenges, and interview notes will be added progressively.
