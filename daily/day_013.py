"""
Day 13 - Python Interview Practice

Topics:
- Custom context manager
- __enter__() / __exit__()
- TypeError / ValueError validation
- Custom exceptions
- isinstance()
"""


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


def calculate_accuracy(correct, total):
    if not isinstance(correct, (int, float)) or not isinstance(total, (int, float)):
        raise TypeError("correct and total must be numeric")

    if total <= 0 or correct < 0 or correct > total:
        raise ValueError("Enter valid correct and total values")

    return round((correct / total) * 100, 2)


class InvalidConfidenceError(Exception):
    pass


def validate_confidence(confidence):
    if not isinstance(confidence, (int, float)):
        raise TypeError("Confidence must be a number")

    if confidence < 0 or confidence > 1:
        raise InvalidConfidenceError("Confidence must be between 0 and 1")

    return confidence


if __name__ == "__main__":
    print(calculate_accuracy(85, 100))
    print(calculate_accuracy(85.5, 100.0))
    print(validate_confidence(0.85))


"""
DAY 13 NOTES

1. Context Manager
   __enter__() -> setup / acquire resource
   with block  -> use resource
   __exit__()  -> cleanup / release resource

   The value returned by __enter__() becomes the value after `as`.

2. __exit__ Exception Information
   __exit__(self, exc_type, exc_value, traceback)

   No exception:
       exc_type = None
       exc_value = None
       traceback = None

   If an exception occurs, __exit__() still runs.

   Returning True suppresses the exception.
   Returning None or False allows it to propagate.

3. TypeError vs ValueError
   TypeError  -> inappropriate type
   ValueError -> acceptable type, invalid value

4. isinstance()
   isinstance(value, (int, float))
   accepts both integer and float values.

5. Custom Exception
   class InvalidConfidenceError(Exception):
       pass

   Defining an exception and raising it are separate actions.
"""
