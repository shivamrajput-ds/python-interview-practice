"""
Day 10 - Python Interview Practice

Topics:
- File reading and writing
- Line-by-line processing
- FileNotFoundError and ValueError
- os.path.join and os.makedirs
- Modular main() structure
"""

import os


def load_scores(file_path: str) -> list[float]:
    result = []

    try:
        with open(file_path, "r") as file:
            for score in file:
                score = score.strip()

                if score == "":
                    continue

                try:
                    converted_score = float(score)
                except ValueError:
                    continue

                result.append(converted_score)

    except FileNotFoundError:
        print("File Not Found")
        return []

    return result


def save_errors(file_path: str, errors: list[str]) -> int:
    count = 0

    with open(file_path, "w") as file:
        for error in errors:
            file.write(error + "\n")
            count += 1

    return count


def main():
    os.makedirs("data", exist_ok=True)

    scores_file_path = os.path.join("data", "scores.txt")
    errors_file_path = os.path.join("data", "errors.txt")

    scores = load_scores(scores_file_path)
    print("Valid Scores:", scores)

    errors = [
        "Invalid score",
        "Model not found",
        "Timeout",
    ]

    count = save_errors(errors_file_path, errors)
    print("Errors Written:", count)


if __name__ == "__main__":
    main()


"""
DAY 10 NOTES

- file.read() reads the whole file as one string.
- for line in file processes one line at a time.
- strip() removes whitespace/newline characters.
- split() returns a list; strip() returns a string.
- "r" = read mode.
- "w" = write mode and replaces existing content.
- FileNotFoundError handles a missing file.
- ValueError can occur for float("bad").
- os.makedirs(..., exist_ok=True) safely creates a directory.
- os.path.join() builds file paths cleanly.
"""
