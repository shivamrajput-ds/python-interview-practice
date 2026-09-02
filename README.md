# Python Interview Practice

> Coding-first Python practice for Data Science, Machine Learning, AI/ML, Applied AI, Generative AI, RAG, and junior Python engineering roles.

This repository documents my daily effort to become stronger at **writing, debugging, reviewing, and explaining Python under interview and real-development constraints**.

The goal is not to finish another Python course or collect isolated syntax examples. The goal is to build the ability to:

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
│   ├── day_014.py
│   ├── day_015.py
│   └── day_016.py
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
| Day 015 | Generator filtering, sets, validation, duplicate control, lazy iteration | ✅ Completed |
| Day 016 | Dunder methods, `__len__`, `__contains__`, `__str__`, natural object behavior | ✅ Completed |

---

# Daily Highlights

## Day 001 — Aggregation, Missing Keys, Mutation vs Rebinding

File: `daily/day_001.py`

Key lessons:

- safe dictionary access with `dict.get()`
- missing keys vs falsy values
- shared object references
- mutation vs rebinding
- `+=` vs `+` for lists

---

## Day 002 — OOP, Mutable Defaults, Exceptions, Numeric Edge Cases

File: `daily/day_002.py`

Covered:

- model-registry style OOP
- mutable default argument danger
- manual max logic
- all-negative edge cases
- `TypeError` vs `ValueError`
- `NaN` and infinity behavior

---

## Day 003 — Generators and Lazy Iteration

File: `daily/day_003.py`

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
yield 30   # produce a value
return 30  # terminate the generator
```

---

## Day 004 — Generator Reinforcement and Copying

File: `daily/day_004.py`

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

File: `daily/day_005.py`

Covered:

- multi-key sorting
- tuple sort keys
- descending numeric + ascending text ordering
- `sorted()` vs `.sort()`
- comprehensions

```python
sorted(models, key=lambda x: (-x[1], x[0]))
```

---

## Day 006 — Closures and `nonlocal`

File: `daily/day_006.py`

A closure retains access to variables from its enclosing scope.

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

File: `daily/day_007.py`

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

File: `daily/day_008.py`

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

Key distinction:

```python
return wrapper    # return function object
return wrapper()  # execute immediately
```

---

## Day 009 — Generator Batching, Custom Exceptions, Iterators

File: `daily/day_009.py`

Covered:

- generator batching
- custom exceptions
- iterable vs iterator
- `__iter__()`
- `__next__()`
- `StopIteration`

Mental model:

```text
iter(obj) -> __iter__()
next(obj) -> __next__()
end       -> StopIteration
```

---

## Day 010 — File Handling and Modular Python

File: `daily/day_010.py`

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

File: `daily/day_011.py`

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

File: `daily/day_012.py`

Covered:

- inheritance
- parent initialization with `super()`
- method overriding
- variable positional arguments
- variable keyword arguments

```text
*args    -> positional arguments -> tuple
**kwargs -> keyword arguments    -> dictionary
```

---

## Day 013 — Context Managers, Validation, and Custom Exceptions

File: `daily/day_013.py`

Context-manager mental model:

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
- custom domain exceptions

---

## Day 014 — Generic Decorators and Controlled Attributes

File: `daily/day_014.py`

### Generic Decorator

```python
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Exiting {func.__name__}")
        return result

    return wrapper
```

### Packing vs Unpacking

```text
def f(*args, **kwargs) -> PACK
f(*args, **kwargs)     -> UNPACK
```

### `@property` and Setter

```python
class ModelConfig:
    def __init__(self, threshold):
        self.threshold = threshold

    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, new_value):
        if not 0 <= new_value <= 1:
            raise ValueError("Invalid threshold")

        self._threshold = new_value
```

Key lesson: using `self.threshold = threshold` inside `__init__` routes initial values through setter validation.

---

## Day 015 — Generator Filtering, Sets, and Validation

File: `daily/day_015.py`

Day 015 combined multiple fundamentals in one practical task.

The goal was to lazily yield only trusted model names while:

- validating confidence values
- applying a confidence threshold
- preventing duplicate model output
- preserving input order
- avoiding an unnecessary result list

```python
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
```

Important correction:

```python
0.0 > score > 1.0
```

does **not** mean "outside the range". It means:

```text
score < 0.0 AND score > 1.0
```

which can never be true.

Correct validation:

```python
score < 0.0 or score > 1.0
```

### Day 015 Takeaways

- generators support lazy output with `yield`
- sets are useful for duplicate detection
- `continue` keeps filtering logic simple
- input order can be preserved while removing duplicates
- chained comparisons must be interpreted carefully

---

## Day 016 — Dunder Methods and Natural Python Object Behavior

File: `daily/day_016.py`

Day 016 focused on how custom classes integrate with normal Python syntax through dunder methods.

### `__len__()`

```python
def __len__(self):
    return len(self.models)
```

Python mapping:

```text
len(obj)
   ↓
obj.__len__()
```

### `__contains__()`

```python
def __contains__(self, model_name):
    return model_name in self.models
```

Python mapping:

```text
"fraud_v1" in registry
        ↓
registry.__contains__("fraud_v1")
```

### `__str__()`

```python
def __str__(self):
    return f"Model(name={self.name}, score={self.score})"
```

Python mapping:

```text
print(obj)
   ↓
str(obj)
   ↓
obj.__str__()
```

### Combined `ScoreBoard`

```python
class ScoreBoard:
    def __init__(self):
        self.models = {}

    def add(self, name, score):
        self.models[name] = score

    def __len__(self):
        return len(self.models)

    def __contains__(self, model_name):
        return model_name in self.models

    def __str__(self):
        return f"ScoreBoard({len(self)} models)"
```

Usage:

```python
board = ScoreBoard()

board.add("fraud_v1", 0.91)
board.add("spam_v1", 0.84)
board.add("churn_v1", 0.95)

print(len(board))
# 3

print("fraud_v1" in board)
# True

print(board)
# ScoreBoard(3 models)
```

### Day 016 Takeaways

- dunder methods connect custom objects to Python built-in syntax
- `len(obj)` uses `__len__()`
- `x in obj` can use `__contains__()`
- `print(obj)` uses `__str__()`
- sets automatically handle duplicate values
- dictionaries fit key-value storage such as model → score
- direct boolean returns are cleaner than unnecessary `if/else`
- custom classes can be designed to feel natural and Pythonic

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
- duplicate handling
- invalid chained comparisons

## Prefer Specific Exceptions

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

Several Python features look magical at first, but map to concrete protocols:

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

len(obj)
    -> __len__()

value in obj
    -> __contains__()

print(obj)
    -> __str__()
```

Understanding these mappings makes advanced Python much easier to reason about.

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
python daily/day_015.py
python daily/day_016.py
```

On Windows:

```bash
py daily/day_016.py
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

Latest commit example:

```bash
git status
git add README.md daily/day_015.py daily/day_016.py
git commit -m "Days 15-16: generators, validation and dunder methods"
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
