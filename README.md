# Python Interview Practice

> Coding-first Python practice for Data Science, Machine Learning, AI/ML, Applied AI, Generative AI, RAG, and junior Python engineering roles.

This repository documents my daily effort to become stronger at **writing, debugging, reviewing, and explaining Python under interview and real-development constraints**.

The goal is not to complete another Python course or collect isolated syntax examples. The goal is to build the ability to:

- understand unfamiliar Python code
- design clean solutions from requirements
- handle edge cases and invalid input
- write modular and maintainable code
- reason about Python behavior and internals
- explain technical decisions clearly
- use Python naturally in data, ML, AI, API, and backend-oriented work

> **This is not a DSA repository.**  
> Advanced graph, tree, dynamic-programming, and competitive-programming practice is maintained separately.

---

## Practice Philosophy

Each session follows a coding-first interview workflow:

```text
Requirement
   ↓
My First Attempt
   ↓
Evaluation
   ↓
Hidden Edge Case / Follow-up
   ↓
Debugging
   ↓
Correct Mental Model
   ↓
Clean Final Implementation
   ↓
Self-Checks
   ↓
Commit to Repository
```

The emphasis is on learning through implementation rather than memorizing answers.

### Practice Mix

- live Python coding
- OOP implementation
- debugging
- output prediction
- Python internals
- exception handling
- file handling
- generators and iterators
- decorators and closures
- context managers
- standard-library usage
- API-oriented Python
- NumPy / Pandas
- lightweight testing
- code review
- modular application structure

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
│   ├── day_003.py
│   ├── day_004.py
│   ├── day_005.py
│   ├── day_006.py
│   ├── day_007.py
│   ├── day_008.py
│   ├── day_009.py
│   ├── day_010.py
│   ├── day_011.py
│   ├── day_012.py
│   └── day_013.py
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

Topic folders are populated only when a concept has enough standalone practice to justify a reusable revision file. Daily files remain the complete chronological record.

---

# Progress

| Day | Main Focus | Status |
|---|---|---|
| Day 001 | Dictionary aggregation, missing keys, type hints, mutation vs rebinding, `+=` vs `+` | ✅ Completed |
| Day 002 | OOP, mutable defaults, dictionary behavior, exception handling, numeric edge cases | ✅ Completed |
| Day 003 | Generators, lazy iteration, `yield`, `next()`, `StopIteration` | ✅ Completed |
| Day 004 | Generator execution, shallow copy, deep copy, nested mutability | ✅ Completed |
| Day 005 | Custom sorting, tuple keys, `sorted()` vs `.sort()`, list comprehensions | ✅ Completed |
| Day 006 | Closures, enclosing scope, `nonlocal`, independent closure state, exception types | ✅ Completed |
| Day 007 | Class variables, instance shadowing, `@classmethod`, `@staticmethod`, alternative constructors | ✅ Completed |
| Day 008 | Validation, case-insensitive filtering, decorators, wrappers, function rebinding | ✅ Completed |
| Day 009 | Generator batching, custom exceptions, iterable vs iterator, custom iterators | ✅ Completed |
| Day 010 | File handling, line-by-line processing, file writing, paths, modular `main()` structure | ✅ Completed |
| Day 011 | Sets, string normalization, first-occurrence preservation, tuple sorting, `sorted()` + `lambda` | ✅ Completed |
| Day 012 | Inheritance, `super()`, method overriding, `*args`, `**kwargs` | ✅ Completed |
| Day 013 | Context managers, `__enter__`, `__exit__`, validation, exception types, custom exceptions | ✅ Completed |

---

# Daily Highlights

## Day 001 — Aggregation, Missing Keys, Mutation vs Rebinding

File:

```text
daily/day_001.py
```

### Event Aggregation

The task summarized API-style event records by event type while safely handling missing or empty fields.

Key concepts:

- nested dictionary aggregation
- `dict.get()`
- key existence vs falsy values
- type hints
- single-pass processing
- requirement reading

### Mutation vs Rebinding

```python
a = [10, 20]
b = a
```

Both names reference the same list.

```python
def add_score(scores, value):
    scores += [value]
```

For lists, `+=` normally mutates the existing list.

By contrast:

```python
def add_score(scores, value):
    scores = scores + [value]
```

creates a new list and rebinds only the local name.

Interview vocabulary reinforced:

```text
object reference
shared reference
mutation
rebinding
identity
```

---

## Day 002 — OOP, Mutable Defaults, Exceptions, Numeric Edge Cases

File:

```text
daily/day_002.py
```

### OOP — Model Registry

A class was built to:

- store model scores
- add scores
- return the best score
- handle unknown models
- avoid `max()` as an interview constraint

A hidden edge case showed why:

```python
result = 0
```

can fail for all-negative values.

A safer manual-scan initialization:

```python
result = float("-inf")
```

### Mutable Default Arguments

Unsafe:

```python
def register_model(model, models=[]):
    ...
```

Safer:

```python
def register_model(model, models=None):
    if models is None:
        models = []
```

### Numeric Cleaning

The session reinforced:

```text
TypeError  -> inappropriate type
ValueError -> acceptable type, invalid value
```

and the important fact that:

```python
float("NaN")
float("inf")
```

do not raise `ValueError`.

---

## Day 003 — Generators and Lazy Iteration

File:

```text
daily/day_003.py
```

A generator-based filtering task processed records without collecting all matching values first.

```python
def slow_requests(records, threshold):
    for record in records:
        ...
        if record["latency_ms"] > threshold:
            yield record
```

Key mental model:

```text
yield value
   ↓
produce value
   ↓
pause
   ↓
next()
   ↓
resume
```

A generator is a specific kind of iterator.

### `return` vs `yield`

Inside a generator:

```python
yield 30
```

produces a normal value.

```python
return 30
```

ends the generator and becomes:

```text
StopIteration(30)
```

---

## Day 004 — Generator Reinforcement and Copying

File:

```text
daily/day_004.py
```

### Generator Execution Timing

Calling a generator function creates the generator object, but the body starts only when iteration begins.

### Shallow Copy

```python
x = [[1, 2], [3, 4]]
y = x.copy()
```

The outer list is new, but nested mutable objects remain shared.

```python
x is y
# False

x[0] is y[0]
# True
```

### Deep Copy

```python
import copy

y = copy.deepcopy(x)
```

Nested mutable objects are copied recursively.

---

## Day 005 — Custom Sorting and Pythonic Collections

File:

```text
daily/day_005.py
```

A custom ranking task used tuple-based sort keys.

```python
def get_rank(record):
    score = record.get("score")

    if score is None:
        return (1, 0, record["model"])

    return (0, -score, record["model"])
```

Concepts reinforced:

- `sorted()` returns a new list
- `.sort()` mutates and returns `None`
- tuples can encode multiple sort priorities
- negative values can reverse numeric order
- `append()` mutates in place and returns `None`
- list comprehensions can filter and transform concisely

---

## Day 006 — Closures and `nonlocal`

File:

```text
daily/day_006.py
```

### Closure

A closure is an inner function that retains access to variables from its enclosing scope after the outer function has finished.

```python
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment
```

Different calls create independent state:

```python
c1 = make_counter()
c2 = make_counter()
```

```text
c1 -> independent count
c2 -> independent count
```

Concepts:

- enclosing scope
- closure state
- `nonlocal`
- local rebinding
- independent closure instances

---

## Day 007 — Class Methods, Static Methods, Alternative Constructors

File:

```text
daily/day_007.py
```

### Class Variable

```python
class ModelRun:
    count = 0
```

A class-level counter tracks shared state.

### Instance Shadowing

```python
Model.category = "AI"
m1.category = "NLP"
```

Then:

```text
m1.category    -> NLP
m2.category    -> AI
Model.category -> AI
```

### Method Mental Model

```text
instance method -> self -> object-specific state
class method    -> cls  -> class-level state / alternative construction
static method   -> no automatic self or cls
```

### Alternative Constructor

```python
@classmethod
def from_string(cls, text):
    name, salary = text.split("-")
    return cls(name, int(salary))
```

This provides another way to create an object:

```python
Employee.from_string("Shivam-50000")
```

---

## Day 008 — Decorators and Function Rebinding

File:

```text
daily/day_008.py
```

### Decorator

```python
def log_execution(func):
    def wrapper():
        print("Function started")
        func()
        print("Function finished")

    return wrapper
```

Using:

```python
@log_execution
def train_model():
    print("Training model")
```

is approximately equivalent to:

```python
train_model = log_execution(train_model)
```

After decoration:

```text
train_model
    ↓
 wrapper
    ↓
original function stored in func
```

Important distinction:

```python
return wrapper
```

returns the function object.

```python
return wrapper()
```

would execute it immediately.

---

## Day 009 — Generator Batching, Custom Exceptions, Iterators

File:

```text
daily/day_009.py
```

### Generator Batching

```python
def batch_records(records, batch_size):
    if batch_size <= 0:
        raise ValueError("Batch size must be positive")

    for i in range(0, len(records), batch_size):
        yield records[i:i + batch_size]
```

### Custom Exception

```python
class InsufficientBalanceError(Exception):
    pass
```

Definition and raising are separate actions:

```python
raise InsufficientBalanceError("Insufficient Balance")
```

### Iterable vs Iterator

```text
Iterable -> object from which an iterator can be created
Iterator -> object that produces one value at a time with next()
```

### Custom Iterator

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration

        value = self.current
        self.current -= 1
        return value
```

Key protocol:

```text
__iter__()
__next__()
StopIteration
```

---

## Day 010 — File Handling and Modular Python

File:

```text
daily/day_010.py
```

Day 010 moved into practical file-system coding with two connected exercises.

### 1. Load Valid Scores from a File

```python
def load_scores(file_path: str) -> list[float]:
    result = []

    try:
        with open(file_path, "r") as file:
            for score in file:
                score = score.strip()

                if score == "":
                    continue

                try:
                    converted_score = float(score)
                except ValueError:
                    continue

                result.append(converted_score)

    except FileNotFoundError:
        print("File Not Found")
        return []

    return result
```

The task reinforced:

- `with open(...)`
- line-by-line processing
- `.strip()`
- blank-line handling
- numeric conversion
- `ValueError`
- `FileNotFoundError`

Important distinction:

```python
file.read()
```

reads the complete file into one string.

```python
for line in file:
```

processes the file incrementally, one line at a time.

### 2. Save Errors to a File

```python
def save_errors(file_path: str, errors: list[str]) -> int:
    count = 0

    with open(file_path, "w") as file:
        for error in errors:
            file.write(error + "\n")
            count += 1

    return count
```

The task reinforced:

```text
"r" -> read
"w" -> write / overwrite
```

along with:

```python
os.makedirs("data", exist_ok=True)
os.path.join("data", "errors.txt")
```

### Modular Structure

The final solution used:

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

to keep execution separate from reusable function definitions.

### Day 010 Takeaways

- use `with open(...)` so file resources are managed safely
- prefer line-by-line iteration when the whole file is not needed at once
- `.strip()` returns a cleaned string; `.split()` returns a list
- catch specific exceptions
- `"w"` overwrites existing content
- `os.path.join()` builds portable paths
- `os.makedirs(..., exist_ok=True)` safely creates directories
- modular code becomes easier to test, reuse, and maintain

---

## Day 011 — Sets, Normalization, and Multi-Key Sorting

File:

```text
daily/day_011.py
```

Day 011 focused on using **sets for fast duplicate detection**, normalizing strings safely, preserving first appearance, and sorting tuples with multiple priorities.

### 1. Remove Duplicate Tags While Preserving Order

```python
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
```

Expected output:

```python
["Python", "ML", "FastAPI", "RAG"]
```

Mental model:

```text
raw value
   ↓
strip()
   ↓
cleaned value
   ↓
lower()
   ↓
normalized comparison key
```

### 2. Multi-Key Tuple Sorting

```python
def rank_models(
    models: list[tuple[str, float]]
) -> list[tuple[str, float]]:
    return sorted(models, key=lambda x: (-x[1], x[0]))
```

The key:

```python
(-x[1], x[0])
```

means:

```text
-x[1] -> score descending
 x[0] -> name ascending when scores tie
```

### Day 011 Takeaways

- use a `set` for efficient duplicate membership checks
- normalize strings before comparison
- preserve the cleaned first occurrence
- use `sorted()` when the original list must remain unchanged
- tuple sort keys can encode multiple ordering rules

---

## Day 012 — Inheritance, `super()`, `*args`, and `**kwargs`

File:

```text
daily/day_012.py
```

Day 012 focused on **object-oriented reuse through inheritance**, parent initialization with `super()`, method overriding, and flexible function signatures with `*args` and `**kwargs`.

### 1. Inheritance + `super()`

```python
class Model:
    def __init__(self, name: str):
        self.name = name


class TrainedModel(Model):
    def __init__(self, name: str, score: float):
        super().__init__(name)
        self.score = score

    def is_good(self) -> bool:
        return self.score >= 0.90
```

### 2. Method Overriding

```python
class BaseModel:
    def predict(self) -> str:
        return "Base Prediction"


class FraudModel(BaseModel):
    def predict(self) -> str:
        return "Fraud Prediction"
```

The child method overrides the inherited implementation for child objects.

### 3. Variable Positional Arguments with `*args`

```python
def average(*scores: float) -> float:
    if len(scores) == 0:
        return 0

    return sum(scores) / len(scores)
```

Mental model:

```text
*args
  ↓
variable positional arguments
  ↓
tuple
```

### 4. Variable Keyword Arguments with `**kwargs`

```python
def build_profile(**details):
    return details
```

Mental model:

```text
**kwargs
    ↓
variable keyword arguments
    ↓
dictionary
```

### Day 012 Takeaways

- inheritance lets child classes reuse parent behavior
- `super()` provides a clean way to call parent-class methods
- overriding lets child classes customize inherited behavior
- `*args` collects positional arguments into a tuple
- `**kwargs` collects keyword arguments into a dictionary
- direct boolean expressions are often cleaner than unnecessary `if/else` returns

---

## Day 013 — Context Managers, Validation, and Custom Exceptions

File:

```text
daily/day_013.py
```

Day 013 moved into **resource management and robust validation** using custom context managers, built-in exception types, and domain-specific custom exceptions.

### 1. Custom Context Manager

A custom file context manager was implemented using `__enter__()` and `__exit__()`.

```python
class ManagedFile:
    def __init__(self, mode: str, file_path: str):
        self.mode = mode
        self.file_path = file_path
        self.file = None

    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(exc_type)
            print(exc_value)
            print(traceback)

        self.file.close()
```

Usage:

```python
with ManagedFile("w", "data.txt") as file:
    file.write("Hello Python")
```

Mental model:

```text
__enter__()
    ↓
acquire / prepare resource
    ↓
with block
    ↓
use resource
    ↓
__exit__()
    ↓
cleanup / release resource
```

For files:

```text
__enter__() -> open file
with block  -> read / write
__exit__()  -> close file
```

The value returned by `__enter__()` becomes the value after `as`.

### 2. Exception Information in `__exit__()`

Python passes three exception-related values automatically:

```python
def __exit__(self, exc_type, exc_value, traceback):
    ...
```

If no exception occurs:

```text
exc_type   -> None
exc_value  -> None
traceback  -> None
```

If an exception occurs inside the `with` block, `__exit__()` still runs, allowing cleanup to happen reliably.

Returning `True` from `__exit__()` suppresses the exception. Returning `None` or `False` allows it to propagate.

### 3. Accuracy Validation

```python
def calculate_accuracy(correct, total):
    if not isinstance(correct, (int, float)) or not isinstance(total, (int, float)):
        raise TypeError("correct and total must be numeric")

    if total <= 0 or correct < 0 or correct > total:
        raise ValueError("Enter valid correct and total values")

    return round((correct / total) * 100, 2)
```

This reinforced the difference between:

```text
TypeError  -> inappropriate type
ValueError -> acceptable type, invalid value
```

It also reinforced:

```python
isinstance(value, (int, float))
```

for validating multiple accepted numeric types.

### 4. Custom Exception for Model Confidence

```python
class InvalidConfidenceError(Exception):
    pass
```

Validation:

```python
def validate_confidence(confidence):
    if not isinstance(confidence, (int, float)):
        raise TypeError("Confidence must be a number")

    if confidence < 0 or confidence > 1:
        raise InvalidConfidenceError(
            "Confidence must be between 0 and 1"
        )

    return confidence
```

This separates:

```text
invalid Python type
        ↓
TypeError

invalid domain value
        ↓
InvalidConfidenceError
```

### Day 013 Takeaways

- context managers separate resource management from resource usage
- `__enter__()` performs setup and returns the usable resource
- `__exit__()` performs cleanup
- `__exit__()` still runs when an exception occurs inside the block
- exception metadata is available through `exc_type`, `exc_value`, and `traceback`
- specific exceptions are better than replacing them with generic `Exception`
- `isinstance(value, (int, float))` supports multiple accepted numeric types
- `TypeError` is appropriate for invalid types
- `ValueError` is appropriate for invalid values
- custom exceptions make domain-specific failures easier to understand and handle

---

# Core Interview Lessons

## Requirement Reading Matters

A solution can be close and still lose marks if it misses a specific requirement.

## Edge Cases Matter

Sample input is not enough.

Examples encountered so far:

- missing dictionary keys
- falsy but valid values
- negative values
- nested mutable objects
- invalid numeric strings
- missing files
- exhausted iterators
- invalid resource state
- invalid numeric ranges

## Name the Actual Exception

Instead of:

> "This may give an error."

Prefer:

> "`event['success']` raises `KeyError` if the key is missing."

## Prefer Simple Control Flow

After an early:

```python
return
continue
raise
```

an extra `else` is often unnecessary.

## Understand Object Behavior

Python interviews frequently test:

```text
reference vs copy
identity vs equality
mutation vs rebinding
instance state vs class state
function object vs function call
resource acquisition vs cleanup
```

---

# Practice Coverage Roadmap

The repository is progressively covering the following areas.

## Core Python

- variables and data types
- strings
- lists
- tuples
- sets and frozensets
- dictionaries
- loops and conditions
- functions and scope
- `*args` / `**kwargs`
- comprehensions
- sorting
- identity vs equality
- shallow vs deep copy
- truthy / falsy behavior

## Object-Oriented Python

- classes and objects
- instance attributes
- class attributes
- instance methods
- `@classmethod`
- `@staticmethod`
- alternative constructors
- inheritance
- overriding
- `super()`
- encapsulation
- properties
- polymorphism
- abstraction
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

- file processing
- `requests`
- JSON handling
- BeautifulSoup
- API clients
- FastAPI-oriented Python
- logging
- pytest
- validation
- modular project structure

## Data Python

- NumPy
- Pandas
- vectorization
- indexing
- filtering
- grouping
- merging
- missing-value handling
- performance considerations

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

Clone:

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
python daily/day_005.py
python daily/day_006.py
python daily/day_007.py
python daily/day_008.py
python daily/day_009.py
python daily/day_010.py
python daily/day_011.py
python daily/day_012.py
python daily/day_013.py
```

On Windows, depending on the Python installation:

```bash
py daily/day_013.py
```

---

# Daily Development Workflow

```text
Read Requirement
      ↓
Write Code in VS Code
      ↓
Run Locally
      ↓
Inspect Output / Error
      ↓
Debug
      ↓
Improve Structure
      ↓
Add Edge Cases
      ↓
Document Learning
      ↓
Commit to GitHub
```

Example:

```bash
git status
git add README.md daily/day_013.py
git commit -m "Day 13: context managers and custom exceptions"
git push
```

---

# Why This Repository Exists

Strong Python performance requires more than syntax recall.

```text
READ REQUIREMENTS
      ↓
UNDERSTAND THE DATA
      ↓
CHOOSE THE RIGHT PYTHON TOOL
      ↓
HANDLE FAILURE CASES
      ↓
WRITE CLEAN CODE
      ↓
RUN AND DEBUG
      ↓
EXPLAIN THE DECISION
```

This repository is a public record of that progression through consistent, interview-style and developer-oriented practice.

---

## Status

**Active — Daily Python Interview Practice**

New coding exercises, debugging cases, OOP implementations, generators, decorators, exceptions, file-processing tasks, standard-library exercises, APIs, NumPy/Pandas tasks, tests, and Python internals will be added progressively.
