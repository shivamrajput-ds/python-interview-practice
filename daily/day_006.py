"""
Day 006 - Python Interview Practice

Focus:
- TypeError vs ValueError
- closures
- local vs enclosing scope
- nonlocal
- independent closure state
- stateful counters
"""

# Q1 - Practical closure

def make_score_filter(threshold: float):
    def check(scores):
        result = []

        for score in scores:
            if score is None or score == "":
                continue

            try:
                converted_value = float(score)
            except ValueError:
                continue

            if converted_value >= threshold:
                result.append(converted_value)

        return result

    return check


filter_high = make_score_filter(0.80)
scores = ["0.91", "bad", 0.75, None, "0.85", ""]
assert filter_high(scores) == [0.91, 0.85]


# TypeError vs ValueError

TYPE_ERROR_VS_VALUE_ERROR = """
TypeError:
    wrong/inappropriate type for the operation.

Examples:
    float(None)
    float([1, 2])
    len(10)

ValueError:
    acceptable type, but invalid value.

Examples:
    float("bad")
    float("")
    int("hello")
"""


# Q2 - Closure reads enclosing binding

def outer_value():
    x = 10

    def inner():
        return x

    x = 20
    return inner


f = outer_value()
assert f() == 20


# Q3 - Local variable inside inner function

def local_scope_example():
    x = 10
    result = []

    def inner():
        x = 50
        result.append(x)

    inner()
    result.append(x)
    return result


assert local_scope_example() == [50, 10]


# Q4 - nonlocal modifies enclosing variable

def nonlocal_example():
    x = 10
    result = []

    def inner():
        nonlocal x
        x = 50
        result.append(x)

    inner()
    result.append(x)
    return result


assert nonlocal_example() == [50, 50]


# Q5 - Independent closure instances

def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


c1 = make_counter()
c2 = make_counter()

assert c1() == 1
assert c1() == 2
assert c2() == 1
assert c1() == 3


# Q6 - Closure counter with step

def make_step_counter():
    count = 0

    def increment(step=1):
        nonlocal count
        count += step
        return count

    return increment


counter = make_step_counter()

assert counter() == 1
assert counter(5) == 6
assert counter() == 7


CLOSURE_NOTE = """
Closure:
    an inner function that retains access to variables
    from its enclosing scope even after the outer
    function has finished.

Without nonlocal:
    assignment creates a new local variable.

With nonlocal:
    assignment rebinds the nearest enclosing variable.

Different outer-function calls create independent
closure state.
"""

DAY_006_NOTES = """
DAY 006 - KEY TAKEAWAYS

1. TypeError = inappropriate type.
2. ValueError = acceptable type, invalid value.
3. Closures retain access to enclosing variables.
4. Closures keep bindings, not frozen snapshots.
5. Inner assignment normally creates a local variable.
6. nonlocal lets an inner function modify enclosing state.
7. Separate closure instances have separate state.
8. Closures are useful for filters, counters, callbacks,
   decorators, and function factories.
"""

print(TYPE_ERROR_VS_VALUE_ERROR)
print(CLOSURE_NOTE)
print(DAY_006_NOTES)
print("\nAll Day 006 self-checks passed.")
