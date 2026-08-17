"""
Day 004 - Python Interview Practice

Focus:
- generator retry and reinforcement
- yield vs print
- generator execution timing
- next() and pause/resume behavior
- return inside generators
- shallow copy
- deep copy
- nested mutability
- copy.deepcopy()
"""

import copy


# ============================================================
# Q1 - Generator Retry: Valid Numeric Scores
# ============================================================

values = ["0.91", "bad", None, "0", "0.78", ""]


def valid_scores(values):
    """
    Convert valid numeric strings to floats and yield them one at a time.

    Rules:
    - skip None
    - skip empty strings
    - skip invalid numeric strings
    - keep valid zero
    - do not build a result list
    """
    for value in values:
        if value is None or value == "":
            continue

        try:
            converted_value = float(value)
        except ValueError:
            continue

        yield converted_value


assert list(valid_scores(values)) == [0.91, 0.0, 0.78]


# ============================================================
# Q2 - Generator Execution Timing
# ============================================================

def test_execution():
    print("A")
    yield 10
    print("B")
    yield 20
    print("C")


g = test_execution()

print("start")
print(next(g))
print("middle")
print(next(g))

# Exact output:
#
# start
# A
# 10
# middle
# B
# 20
#
# "C" is not printed because a third next() was never called.


# ============================================================
# Q3 - return Inside a Generator
# ============================================================

def generator_with_return():
    print("A")
    yield 10
    print("B")
    return 99


g_return = generator_with_return()

assert next(g_return) == 10

try:
    next(g_return)
except StopIteration as exc:
    assert exc.value == 99
else:
    raise AssertionError("Expected StopIteration")


# ============================================================
# Q4 - Assignment vs Shallow Copy
# ============================================================

x = [1, 2, 3]
y = x
z = x.copy()

x.append(4)

assert y == [1, 2, 3, 4]
assert z == [1, 2, 3]
assert x is y
assert x is not z


# ============================================================
# Q5 - Shallow Copy with Nested Mutable Objects
# ============================================================

nested = [[1, 2], [3, 4]]
shallow = nested.copy()

nested[0].append(99)

assert nested == [[1, 2, 99], [3, 4]]
assert shallow == [[1, 2, 99], [3, 4]]

assert nested is not shallow
assert nested[0] is shallow[0]


# ============================================================
# Q6 - Deep Copy
# ============================================================

deep_source = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(deep_source)

deep_source[0].append(99)

assert deep_source == [[1, 2, 99], [3, 4]]
assert deep_copy == [[1, 2], [3, 4]]

assert deep_source is not deep_copy
assert deep_source[0] is not deep_copy[0]


# ============================================================
# Q7 - Practical Nested Copy Function
# ============================================================

data = {
    "user": {
        "name": "Shivam",
        "skills": ["Python", "SQL"],
    }
}


def add_skill(data, skill):
    """
    Return an independent updated copy without mutating the original data.
    """
    updated_data = copy.deepcopy(data)
    updated_data["user"]["skills"].append(skill)
    return updated_data


updated = add_skill(data, "FastAPI")

assert data["user"]["skills"] == ["Python", "SQL"]
assert updated["user"]["skills"] == ["Python", "SQL", "FastAPI"]

assert data is not updated
assert data["user"] is not updated["user"]
assert data["user"]["skills"] is not updated["user"]["skills"]


# ============================================================
# Visual Mental Model
# ============================================================

COPY_VISUAL = """
COPYING MENTAL MODEL
--------------------

1. Assignment

x = [[1, 2]]
y = x

x -----+
       +----> outer list ----> inner list
y -----+


2. Shallow copy

y = x.copy()

x ----------> outer list A ----+
                               +----> same inner list
y ----------> outer list B ----+


3. Deep copy

y = copy.deepcopy(x)

x ----------> outer list A ----> inner list A

y ----------> outer list B ----> inner list B

Both levels are independent.
"""

print(COPY_VISUAL)


# ============================================================
# Day 004 Interview Takeaways
# ============================================================

DAY_004_NOTES = """
DAY 004 - KEY TAKEAWAYS

1. print() inside a function is not the same as yielding a value.
2. yield makes a function a generator function.
3. Calling a generator function returns a generator object.
4. Generator code starts when iteration begins, not at creation time.
5. next() resumes execution until the next yield.
6. return value inside a generator ends iteration.
7. That value becomes StopIteration.value.
8. y = x does not create a copy.
9. x.copy() creates a shallow copy.
10. Shallow copies still share nested mutable objects.
11. copy.deepcopy() recursively creates independent nested objects.
12. Deep copy is useful when the returned nested structure must not share
    mutable state with the original.
"""

print(DAY_004_NOTES)


# ============================================================
# Final Self-Checks
# ============================================================

assert list(valid_scores(["0", "1.5", "bad", None, ""])) == [0.0, 1.5]

test_data = {
    "user": {
        "name": "Test",
        "skills": ["Python"],
    }
}

test_updated = add_skill(test_data, "SQL")

assert test_data["user"]["skills"] == ["Python"]
assert test_updated["user"]["skills"] == ["Python", "SQL"]
assert test_data["user"]["skills"] is not test_updated["user"]["skills"]

print("\nAll Day 004 self-checks passed.")
