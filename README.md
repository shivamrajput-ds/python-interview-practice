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
│   ├── day_013.py
│   └── day_014.py
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
| Day 001 | Dictionary aggregation, missing keys, type hints, mutation vs rebinding | ✅ Completed |
| Day 002 | OOP, mutable defaults, dictionary behavior, exceptions, numeric edge cases | ✅ Completed |
| Day 003 | Generators, lazy iteration, `yield`, `next()`, `StopIteration` | ✅ Completed |
| Day 004 | Generator execution, shallow copy, deep copy, nested mutability | ✅ Completed |
| Day 005 | Custom sorting, tuple keys, `sorted()` vs `.sort()`, comprehensions | ✅ Completed |
| Day 006 | Closures, enclosing scope, `nonlocal`, independent closure state | ✅ Completed |
| Day 007 | Class variables, instance shadowing, `@classmethod`, `@staticmethod`, alternative constructors | ✅ Completed |
| Day 008 | Validation, case-insensitive filtering, decorators, wrappers, function rebinding | ✅ Completed |
| Day 009 | Generator batching, custom exceptions, iterable vs iterator, custom iterators | ✅ Completed |
| Day 010 | File handling, line-by-line processing, paths, modular `main()` structure | ✅ Completed |
| Day 011 | Sets, normalization, first-occurrence preservation, tuple sorting, `lambda` | ✅ Completed |
| Day 012 | Inheritance, `super()`, method overriding, `*args`, `**kwargs` | ✅ Completed |
| Day 013 | Context managers, `__enter__`, `__exit__`, validation, custom exceptions | ✅ Completed |
| Day 014 | Generic decorators, argument forwarding, packing/unpacking, `@property`, setters | ✅ Completed |

---

# Daily Highlights

## Day 001 — Aggregation, Missing Keys, Mutation vs Rebinding

File:

```text
daily/day_001.py
```

Key lessons:

- safe dictionary access with `dict.get()`
- missing keys vs falsy values
- shared object references
- mutation vs rebinding
- `+=` vs `+` for lists

```python
a = [10, 20]
b = a
```

Both names reference the same list.

```python
def add_score(scores, value):
    scores += [value]
```

For lists, `+=` normally mutates the existing object.

---

## Day 002 — OOP, Mutable Defaults, Exceptions, Numeric Edge Cases

File:

```text
daily/day_002.py
```

Key lessons:

- model-registry style OOP
- mutable default argument danger
- manual max logic
- handling all-negative values
- `TypeError` vs `ValueError`
- `NaN` / infinity edge cases

Safer mutable-default pattern:

```python
def register_model(model, models=None):
    if models is None:
        models = []
```

---

## Day 003 — Generators and Lazy Iteration

File:

```text
daily/day_003.py
```

Mental model:

```text
yield
  ↓
produce one value
  ↓
pause
  ↓
next()
  ↓
resume
```

Important distinction:

```python
yield 30
```

produces a value, while:

```python
return 30
```

inside a generator terminates iteration.

---

## Day 004 — Generator Reinforcement and Copying

File:

```text
daily/day_004.py
```

Covered:

- generator execution timing
- shallow copy
- deep copy
- nested mutable state

```python
x = [[1, 2], [3, 4]]
y = x.copy()

x is y
# False

x[0] is y[0]
# True
```

---

## Day 005 — Custom Sorting and Pythonic Collections

File:

```text
daily/day_005.py
```

Covered:

- multi-key sorting
- tuple sort keys
- descending numeric + ascending text ordering
- `sorted()` vs `.sort()`
- mutation behavior
- comprehensions

```python
sorted(models, key=lambda x: (-x[1], x[0]))
```

---

## Day 006 — Closures and `nonlocal`

File:

```text
daily/day_006.py
```

A closure keeps access to variables from its enclosing scope.

```python
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment
```

Different calls create independent closure state.

---

## Day 007 — Class Methods, Static Methods, Alternative Constructors

File:

```text
daily/day_007.py
```

Mental model:

```text
instance method -> self -> object-specific state
class method    -> cls  -> class-level state / alternative construction
static method   -> no automatic self or cls
```

Alternative constructor:

```python
@classmethod
def from_string(cls, text):
    name, salary = text.split("-")
    return cls(name, int(salary))
```

---

## Day 008 — Decorators and Function Rebinding

File:

```text
daily/day_008.py
```

Using:

```python
@log_execution
def train_model():
    ...
```

is roughly equivalent to:

```python
train_model = log_execution(train_model)
```

Important distinction:

```python
return wrapper
```

returns a function object, while:

```python
return wrapper()
```

executes it immediately.

---

## Day 009 — Generator Batching, Custom Exceptions, Iterators

File:

```text
daily/day_009.py
```

Covered:

- batch generators
- custom exceptions
- iterable vs iterator
- `__iter__()`
- `__next__()`
- `StopIteration`

Custom iterator mental model:

```text
iter(obj)
   ↓
__iter__()
   ↓
next(obj)
   ↓
__next__()
   ↓
StopIteration
```

---

## Day 010 — File Handling and Modular Python

File:

```text
daily/day_010.py
```

Covered:

- `with open(...)`
- line-by-line processing
- `.strip()`
- numeric conversion
- `FileNotFoundError`
- writing files
- `os.path.join()`
- `os.makedirs(..., exist_ok=True)`
- modular `main()` structure

```python
if __name__ == "__main__":
    main()
```

---

## Day 011 — Sets, Normalization, and Multi-Key Sorting

File:

```text
daily/day_011.py
```

Deduplication pattern:

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

Key idea: compare normalized values while preserving the cleaned first occurrence.

---

## Day 012 — Inheritance, `super()`, `*args`, and `**kwargs`

File:

```text
daily/day_012.py
```

Covered:

- inheritance
- parent initialization with `super()`
- method overriding
- variable positional arguments
- variable keyword arguments

Mental model:

```text
*args    -> positional arguments -> tuple
**kwargs -> keyword arguments    -> dictionary
```

---

## Day 013 — Context Managers, Validation, and Custom Exceptions

File:

```text
daily/day_013.py
```

Custom context-manager mental model:

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
__enter__() -> open
with block  -> read/write
__exit__()  -> close
```

Python roughly turns:

```python
with ManagedFile("w", "data.txt") as file:
    file.write("Hello")
```

into:

```python
manager = ManagedFile("w", "data.txt")
file = manager.__enter__()

try:
    file.write("Hello")
finally:
    manager.__exit__(None, None, None)
```

Also covered:

- `TypeError`
- `ValueError`
- `isinstance(value, (int, float))`
- domain-specific custom exceptions

---

## Day 014 — Generic Decorators and Controlled Attributes

File:

```text
daily/day_014.py
```

Day 014 strengthened two important Python ideas:

1. **generic decorators that preserve arguments and return values**
2. **controlled attribute access using `@property` and setters**

### 1. Generic Decorator with `*args` and `**kwargs`

```python
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}")

        result = func(*args, **kwargs)

        print(f"Exiting {func.__name__}")
        return result

    return wrapper
```

Decorated function:

```python
@log_execution
def predict(model_name: str, score: float) -> bool:
    print(f"{model_name}: {score}")
    return score > 0.90
```

The original function keeps a meaningful signature while the wrapper stays generic.

### 2. Packing vs Unpacking

This was a key mental-model improvement.

Function definition:

```python
def wrapper(*args, **kwargs):
```

means **pack incoming arguments**:

```text
*args    -> tuple
**kwargs -> dictionary
```

Function call:

```python
func(*args, **kwargs)
```

means **unpack and forward them**.

Example:

```python
predict("fraud_v1", score=0.94)
```

Inside the wrapper:

```python
args == ("fraud_v1",)
kwargs == {"score": 0.94}
```

Then:

```python
func(*args, **kwargs)
```

becomes roughly:

```python
func("fraud_v1", score=0.94)
```

Memory rule:

```text
def f(*args, **kwargs) -> PACK
f(*args, **kwargs)     -> UNPACK
```

### 3. `@property`

A property lets method logic run behind normal-looking attribute access.

```python
class ModelConfig:
    def __init__(self, threshold):
        self.threshold = threshold

    @property
    def threshold(self):
        return self._threshold
```

Usage:

```python
config.threshold
```

looks like normal attribute access, but Python calls the getter.

### 4. Property Setter

```python
@threshold.setter
def threshold(self, new_value):
    if not 0 <= new_value <= 1:
        raise ValueError("Invalid threshold")

    self._threshold = new_value
```

Now:

```python
config.threshold = 0.95
```

automatically calls the setter.

### 5. Constructor Validation Through the Setter

This:

```python
self.threshold = threshold
```

is intentionally used inside `__init__`.

It routes the initial value through the setter:

```text
ModelConfig(0.85)
      ↓
self.threshold = 0.85
      ↓
setter runs
      ↓
validation
      ↓
self._threshold = 0.85
```

Using:

```python
self._threshold = threshold
```

inside the constructor would bypass setter validation.

### 6. Backing Attribute

The public interface is:

```python
config.threshold
```

while the real stored value is:

```python
self._threshold
```

This separation prevents recursive setter calls and gives controlled access to internal state.

### Day 014 Takeaways

- a generic decorator should accept `*args` and `**kwargs`
- wrappers should forward original arguments
- wrappers should preserve original return values
- function definitions pack arguments
- function calls with `*args` / `**kwargs` unpack arguments
- `@property` exposes controlled getter behavior through attribute syntax
- `@property_name.setter` intercepts assignments
- setters are useful for validation
- constructor assignments can be routed through setters
- `_attribute` can act as the internal backing value
- validation should cover the complete allowed range

---

# Core Interview Lessons

## Requirement Reading Matters

A solution can be close and still lose marks if it misses a specific requirement.

## Edge Cases Matter

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
- positional vs keyword argument forwarding
- constructor validation bypass

## Name the Actual Exception

Instead of:

> "This may give an error."

Prefer:

> "`event['success']` raises `KeyError` if the key is missing."

## Prefer Simple Control Flow

After:

```python
return
continue
raise
```

an extra `else` is often unnecessary.

## Understand Python Protocols

Several Python features look like special syntax, but are built on protocols:

```text
with obj
    -> __enter__()
    -> block
    -> __exit__()

next(obj)
    -> __next__()

@decorator
    -> function = decorator(function)

config.threshold
    -> property getter

config.threshold = value
    -> property setter
```

Understanding these transformations makes advanced Python easier to reason about.

---

# Practice Coverage Roadmap

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
- properties
- setters
- encapsulation
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
python daily/day_014.py
```

On Windows:

```bash
py daily/day_014.py
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

Latest example:

```bash
git status
git add README.md daily/day_014.py
git commit -m "Day 14: generic decorators and property validation"
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
