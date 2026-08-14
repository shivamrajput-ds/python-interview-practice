"""
Day 001 - Python Interview Practice
===================================

Focus:
1. Nested dictionary aggregation
2. Missing dictionary keys and safe handling
3. Type hints
4. Mutable objects and shared references
5. In-place mutation vs rebinding
6. += vs + with Python lists

This file is based on today's live interview attempts and corrections.
"""


# ---------------------------------------------------------------------------
# Question 1: Event Summary
# ---------------------------------------------------------------------------

def summarize_events(
    events: list[dict[str, object]],
) -> dict[str, dict[str, int]]:
    """
    Summarize valid event records by event type.

    Rules:
    - Skip records where "type" is missing.
    - Skip records where "type" is an empty string.
    - Count every valid event in "total".
    - Treat a missing "success" key as False.
    """
    result: dict[str, dict[str, int]] = {}

    for event in events:
        event_type = event.get("type")

        if not event_type:
            continue

        if event_type not in result:
            result[event_type] = {
                "total": 0,
                "success": 0,
            }

        result[event_type]["total"] += 1

        if event.get("success", False):
            result[event_type]["success"] += 1

    return result


events = [
    {"type": "login", "success": True},
    {"type": "login", "success": False},
    {"type": "purchase", "success": True},
    {"success": True},
    {"type": "", "success": True},
    {"type": "purchase", "success": False},
    {"type": "login"},  # Missing "success" -> treated as False
]


print("QUESTION 1 - EVENT SUMMARY")
print(summarize_events(events))


# ---------------------------------------------------------------------------
# Question 2: Mutation vs Rebinding
# ---------------------------------------------------------------------------

def mutate_with_iadd(scores: list[int], value: int) -> None:
    """
    += on a list normally mutates the existing list object in place.
    """
    scores += [value]


a = [10, 20]
b = a

print("\nQUESTION 2A - USING +=")
print("Before:")
print("a ----┐")
print("      ├──> [10, 20]")
print("b ----┘")

mutate_with_iadd(b, 30)

print("\nAfter mutate_with_iadd(b, 30):")
print("a ----┐")
print("      ├──> [10, 20, 30]")
print("b ----┘")
print(f"a = {a}")
print(f"b = {b}")
print(f"a is b -> {a is b}")


def rebind_with_addition(scores: list[int], value: int) -> None:
    """
    scores + [value] creates a NEW list.

    Assigning that new list back to `scores` only rebinds the local variable
    inside this function. The caller's original list is not changed.
    """
    scores = scores + [value]

    print("\nInside function after rebinding:")
    print(f"local scores = {scores}")


a = [10, 20]
b = a

print("\nQUESTION 2B - USING scores = scores + [value]")
print("Before:")
print("a ----┐")
print("      ├──> [10, 20]")
print("b ----┘")

rebind_with_addition(b, 30)

print("\nAfter function returns:")
print("a ----┐")
print("      ├──> [10, 20]")
print("b ----┘")
print()
print("Temporary local reference:")
print("scores ------> [10, 20, 30]   # local reference only")
print()
print(f"a = {a}")
print(f"b = {b}")
print(f"a is b -> {a is b}")


# ---------------------------------------------------------------------------
# Key Interview Notes
# ---------------------------------------------------------------------------

INTERVIEW_NOTES = """
KEY TAKEAWAYS

1. Dictionary key access:
   event["success"]
   - Raises KeyError if the key does not exist.

   event.get("success", False)
   - Safely returns False when the key is missing.

2. Key existence vs value checking:
   if "type" not in event:
       ...
   checks whether the key exists.

   if not event.get("type"):
       ...
   checks whether the resulting value is falsy.

3. Shared references:
   b = a
   does NOT copy the list.
   Both names refer to the same list object.

4. List +=:
   scores += [30]
   normally mutates the existing list in place.

5. List +:
   scores = scores + [30]
   creates a new list and rebinds the local variable `scores`.

6. Important interview vocabulary:
   - mutation
   - rebinding
   - object reference
   - shared reference
   - KeyError
   - dict.get()
"""

print("\n" + INTERVIEW_NOTES)


# ---------------------------------------------------------------------------
# Lightweight Self-Checks
# ---------------------------------------------------------------------------

assert summarize_events(
    [
        {"type": "login", "success": True},
        {"type": "login", "success": False},
        {"type": "purchase", "success": True},
        {"success": True},
        {"type": "", "success": True},
        {"type": "purchase", "success": False},
    ]
) == {
    "login": {"total": 2, "success": 1},
    "purchase": {"total": 2, "success": 1},
}

assert summarize_events(
    [
        {"type": "login"},
    ]
) == {
    "login": {"total": 1, "success": 0},
}

print("All Day 001 self-checks passed.")
