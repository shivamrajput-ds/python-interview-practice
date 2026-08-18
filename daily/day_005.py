"""
Day 005 - Python Interview Practice

Focus:
- custom sorting with sorted()
- key functions and tuple-based sorting
- sorted() vs list.sort()
- in-place methods and None return values
- list.append()
- list comprehensions
- safe dictionary access with dict.get()
"""


# ============================================================
# Q1 - Custom Sorting with Multiple Rules
# ============================================================

results = [
    {"model": "beta", "score": 0.91},
    {"model": "alpha", "score": 0.91},
    {"model": "gamma", "score": 0.78},
    {"model": "delta", "score": None},
    {"model": "epsilon"},
]


def rank_models(results):
    """
    Return a new ranked list without mutating the original.
    """

    def get_rank(record):
        score = record.get("score")

        if score is None:
            return (1, 0, record["model"])

        return (0, -score, record["model"])

    return sorted(results, key=get_rank)


expected_ranking = [
    {"model": "alpha", "score": 0.91},
    {"model": "beta", "score": 0.91},
    {"model": "gamma", "score": 0.78},
    {"model": "delta", "score": None},
    {"model": "epsilon"},
]

assert rank_models(results) == expected_ranking
assert results[0]["model"] == "beta"


# ============================================================
# Q2 - sorted() vs list.sort()
# ============================================================

a = [3, 1, 2]
b = sorted(a)

assert a == [3, 1, 2]
assert b == [1, 2, 3]

c = [3, 1, 2]
d = c.sort()

assert c == [1, 2, 3]
assert d is None


# ============================================================
# Q3 - append() Mutates and Returns None
# ============================================================

nums = [10, 20, 30]
result = nums.append(40)

assert nums == [10, 20, 30, 40]
assert result is None


# ============================================================
# Q4 - List Comprehension with Safe Dictionary Access
# ============================================================

users = [
    {"name": "A", "age": 24},
    {"name": "B", "age": 19},
    {"name": "C"},
    {"name": "D", "age": 30},
    {"name": "E", "age": None},
]


def adult_names(users):
    """
    Return names of users whose valid age is at least 21.
    """
    return [
        user["name"]
        for user in users
        if user.get("age") is not None and user["age"] >= 21
    ]


assert adult_names(users) == ["A", "D"]


# ============================================================
# Interview Notes
# ============================================================

SORTING_NOTE = """
CUSTOM SORTING
--------------

Python compares tuple keys left to right.

Valid score:
    (0, -score, model)

Missing/None score:
    (1, 0, model)

The first field separates valid and missing scores.
The negative score puts higher scores first.
The model name breaks ties alphabetically.
"""

SORT_VS_SORTED_NOTE = """
sorted(iterable)
    -> returns a new sorted list
    -> does not mutate the original order

list.sort()
    -> sorts the existing list in place
    -> returns None
"""

APPEND_NOTE = """
list.append(value)
    -> mutates the existing list
    -> returns None

So:

    result = nums.append(40)

leaves the modified list in nums,
while result becomes None.
"""

COMPREHENSION_NOTE = """
List comprehension:

    [expression for item in iterable if condition]

For adult_names():

    expression -> user["name"]
    iterable   -> users
    condition  -> valid age and age >= 21
"""

COPY_NOTE = """
No deepcopy was required for rank_models().

sorted(results, key=...) already creates a new outer list
without reordering the original list.

A deep copy would only be relevant if nested records themselves
also needed to be independently mutated.
"""

DAY_005_NOTES = """
DAY 005 - KEY TAKEAWAYS

1. sorted() returns a new sorted list.
2. list.sort() mutates the list and returns None.
3. key= controls custom sorting behavior.
4. Tuple keys support multiple sorting rules.
5. Negative numeric keys can reverse numeric ordering.
6. append() mutates in place and returns None.
7. List comprehensions combine transformation and filtering.
8. dict.get() safely handles potentially missing keys.
9. deepcopy() should not be used when it is unnecessary.
"""

print(SORTING_NOTE)
print(SORT_VS_SORTED_NOTE)
print(APPEND_NOTE)
print(COMPREHENSION_NOTE)
print(COPY_NOTE)
print(DAY_005_NOTES)


# ============================================================
# Final Self-Checks
# ============================================================

assert rank_models(results) == expected_ranking
assert adult_names(users) == ["A", "D"]

temporary = [3, 2, 1]
sort_return = temporary.sort()

assert temporary == [1, 2, 3]
assert sort_return is None

print("\nAll Day 005 self-checks passed.")
