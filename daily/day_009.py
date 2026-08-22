"""
Day 9 - Python Interview Practice

Focus:
- Generators and lazy batching
- Validation with ValueError
- Custom exceptions
- OOP with validation
- Iterable vs iterator
- __iter__(), __next__(), StopIteration
- Custom iterator implementation
"""


def batch_records(records, batch_size):
    if batch_size <= 0:
        raise ValueError("Batch Size must be a positive number")

    for i in range(0, len(records), batch_size):
        yield records[i:i + batch_size]


records = [10, 20, 30, 40, 50, 60, 70]

for batch in batch_records(records, 3):
    print(batch)


class InsufficientBalanceError(Exception):
    pass


class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")

        if amount > self.balance:
            raise InsufficientBalanceError(
                "Insufficient Balance in your Account"
            )

        self.balance -= amount
        return self.balance


wallet = Wallet(1000)
print(wallet.withdraw(300))

try:
    wallet.withdraw(900)
except InsufficientBalanceError as exc:
    print(exc)


nums = [10, 20, 30]
iterator = iter(nums)

print(next(iterator))
print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))
except StopIteration:
    print("Iterator exhausted")


class MyIterator:
    def __init__(self, values):
        self.values = values
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.values):
            raise StopIteration

        value = self.values[self.index]
        self.index += 1
        return value


values = [1, 2, 3, 4, 5]

for value in MyIterator(values):
    print(value)

print(values)


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


for value in Countdown(3):
    print(value)


"""
DAY 9 NOTES

Generator
---------
A function with yield produces values one at a time.

Custom exception
----------------
class MyError(Exception):
    pass

Raise it only when the actual problem occurs:
    raise MyError("message")

Iterable vs Iterator
--------------------
Iterable:
    An object from which an iterator can be created.

Iterator:
    An object that produces one value at a time with next().

Example:
    nums = [1, 2, 3]
    it = iter(nums)
    next(it)

Iterator protocol
-----------------
__iter__()
    Returns the iterator object.

__next__()
    Returns the next value.
    Raises StopIteration when finished.

A for loop roughly does:

    it = iter(object)

    while True:
        try:
            value = next(it)
        except StopIteration:
            break

Important:
Avoid mutating the original input unnecessarily while implementing
an iterator. Using an index is often cleaner than pop(0).

Retry later:
- iterable vs iterator
- iter()
- next()
- __iter__()
- __next__()
- StopIteration
- generator vs iterator
"""
