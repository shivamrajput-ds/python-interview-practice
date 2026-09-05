"""
Day 19 - Python Interview Practice

Focus:
- iterable vs iterator
- custom iterator protocol
- __iter__()
- __next__()
- iterator state
- StopIteration
- batching records without generators
"""

class BatchIterator:
    def __init__(self, records, batch_size):
        if not isinstance(batch_size, int) or batch_size <= 0:
            raise ValueError("batch_size must be a positive integer")

        self.records = records
        self.batch_size = batch_size
        self.curr_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_index >= len(self.records):
            raise StopIteration

        result = self.records[
            self.curr_index:self.curr_index + self.batch_size
        ]
        self.curr_index += self.batch_size
        return result


def main():
    records = ["a", "b", "c", "d", "e"]
    batcher = BatchIterator(records, 2)

    print(iter(batcher) is batcher)
    print(next(batcher))
    print(next(batcher))
    print(next(batcher))

    # Uncomment to observe StopIteration:
    # print(next(batcher))


if __name__ == "__main__":
    main()


"""
DAY 19 NOTES

Iterable:
    Object that can provide an iterator.

Iterator:
    Object that remembers state and returns the next value.

Python mappings:

    iter(obj) -> obj.__iter__()
    next(obj) -> obj.__next__()

Why __iter__ returns self:

    def __iter__(self):
        return self

BatchIterator is already the iterator because it owns:
- records
- batch_size
- curr_index
- __next__ logic

So:

    iter(batcher) is batcher
    # True

Do NOT write:

    def __iter__(self):
        return iter(self)

because that causes recursion:

    iter(batcher)
      -> __iter__()
      -> iter(self)
      -> __iter__()
      -> ...

Do NOT return iter(self.records) either, because that creates
a separate list iterator that returns individual elements instead
of batches.

Iterator state:

    curr_index = 0
    next() -> records[0:2] -> ["a", "b"]
    curr_index = 2

    next() -> records[2:4] -> ["c", "d"]
    curr_index = 4

    next() -> records[4:6] -> ["e"]
    curr_index = 6

When curr_index >= len(records):

    raise StopIteration

Mental model:

    __init__()  -> what state should I remember?
    __iter__()  -> who will provide next values? -> self
    __next__()  -> what is the next batch?
    StopIteration -> no data remains

A for-loop roughly does:

    iterator = iter(obj)

    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break

Day 19 takeaway:
A custom iterator is a stateful object that implements
__iter__() and __next__().
"""
