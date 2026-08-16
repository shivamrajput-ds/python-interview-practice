"""
Day 003 - Python Interview Practice

Focus:
- generators
- lazy iteration
- yield vs return
- iterators
- next()
- StopIteration
- StopIteration.value
- memory-efficient filtering
"""


# ============================================================
# Q1 - Memory-Efficient Filtering with a Generator
# ============================================================

records = [
    {"model": "fraud_v1", "latency_ms": 120},
    {"model": "fraud_v2", "latency_ms": 310},
    {"model": "fraud_v1", "latency_ms": 180},
    {"model": "fraud_v3", "latency_ms": None},
    {"latency_ms": 90},
    {"model": "fraud_v2", "latency_ms": 150},
]


def slow_requests(records, threshold):
    """
    Yield slow requests one at a time instead of storing
    every matching record in another list.
    """
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


for record in slow_requests(records, 200):
    print(record)

# Expected:
# {'model': 'fraud_v2', 'latency_ms': 310}


# ============================================================
# Generator vs List
# ============================================================

GENERATOR_NOTE = """
List approach:

    result = []
    result.append(...)

stores all matching values in memory.

Generator approach:

    yield value

produces one value at a time.

Flow:

record -> check -> yield -> PAUSE
                         |
next() ------------------+
                         |
                     RESUME

This is useful for large logs, files, API streams,
and other large data sources.
"""

print(GENERATOR_NOTE)


# ============================================================
# iter() vs Generator
# ============================================================

ITER_NOTE = """
iter(existing_list)
    -> creates an iterator over that list

list(iter(existing_list))
    -> creates a list again

So list(iter(result)) does not give the memory-saving
behavior expected from a generator.

A generator is a specific kind of iterator.
A function containing yield is a generator function.
"""

print(ITER_NOTE)


# ============================================================
# Q2 - next(), return, and StopIteration
# ============================================================

def numbers():
    yield 10
    yield 20
    return 30


g = numbers()

assert next(g) == 10
assert next(g) == 20

try:
    next(g)
except StopIteration as exc:
    assert exc.value == 30
else:
    raise AssertionError("Expected StopIteration")


YIELD_RETURN_NOTE = """
Inside a generator:

    yield value
        -> produce value
        -> pause
        -> preserve state
        -> continue on next()

    return value
        -> finish generator
        -> raise StopIteration(value)

Therefore return 30 does NOT yield 30 normally.
"""

print(YIELD_RETURN_NOTE)


# ============================================================
# Final Output Prediction
# ============================================================

def demo():
    yield 1
    yield 2
    return 3


g = demo()

print(next(g))
print(next(g))

try:
    print(next(g))
except StopIteration as exc:
    print("finished:", exc.value)

# Exact output:
#
# 1
# 2
# finished: 3


# ============================================================
# What if return 3 becomes yield 3?
# ============================================================

def demo_with_yield():
    yield 1
    yield 2
    yield 3


g2 = demo_with_yield()

assert next(g2) == 1
assert next(g2) == 2
assert next(g2) == 3

try:
    next(g2)
except StopIteration as exc:
    assert exc.value is None
else:
    raise AssertionError("Expected StopIteration")


COMPARISON_NOTE = """
return 3:

    third next()
        -> StopIteration(3)

yield 3:

    third next()
        -> 3

    fourth next()
        -> StopIteration
"""

print(COMPARISON_NOTE)


# ============================================================
# Mental Model
# ============================================================

GENERATOR_VISUAL = """
GENERATOR MENTAL MODEL

call generator function
        |
        v
generator object created
        |
      next()
        |
        v
run until yield
        |
        v
return one value to caller
        |
      PAUSE
        |
      next()
        |
      RESUME
        |
        v
next yield / return / function end
        |
        v
StopIteration when finished
"""

print(GENERATOR_VISUAL)


# ============================================================
# Day 003 Interview Takeaways
# ============================================================

DAY_003_NOTES = """
1. A function containing yield is a generator function.
2. Calling it returns a generator object.
3. yield returns one value and pauses execution.
4. State is preserved between next() calls.
5. next() resumes execution.
6. Exhausted generators raise StopIteration.
7. return value ends a generator.
8. That value becomes StopIteration.value.
9. iter(list) creates an iterator, not a generator.
10. list(iter(...)) creates a list again.
11. Generators are useful for lazy, memory-efficient processing.
"""

print(DAY_003_NOTES)


# ============================================================
# Self-Checks
# ============================================================

assert list(slow_requests(records, 200)) == [
    {"model": "fraud_v2", "latency_ms": 310}
]

assert list(slow_requests(records, 1000)) == []

extra_records = [
    {"model": "m1", "latency_ms": 250},
    {"model": "m2", "latency_ms": 400},
    {"model": "m3", "latency_ms": 50},
]

assert list(slow_requests(extra_records, 200)) == [
    {"model": "m1", "latency_ms": 250},
    {"model": "m2", "latency_ms": 400},
]

print("\nAll Day 003 self-checks passed.")
