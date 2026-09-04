"""
Day 18 - Python Interview Practice

Topics:
- logging
- model-score validation
- os.listdir()
- os.path
- os.walk()
- direct vs recursive file counting
"""

import logging
import os


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s",
)


def validate_model_score(model_name, score):
    if score < 0 or score > 1:
        logging.error(f"{model_name} has invalid score {score}")
        return False

    if score < 0.80:
        logging.warning(f"{model_name} has low score {score}")
        return False

    logging.info(f"{model_name} accepted with score {score}")
    return True


def count_python_files(folder_path):
    """Count only direct .py files inside folder_path."""
    if not os.path.exists(folder_path):
        return 0

    count = 0

    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)

        if os.path.isfile(full_path):
            if os.path.splitext(item)[1] == ".py":
                count += 1

    return count


def count_python_files_recursive(folder_path):
    """Count .py files in folder_path and all subfolders."""
    if not os.path.exists(folder_path):
        return 0

    count = 0

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if os.path.splitext(file)[1] == ".py":
                count += 1

    return count


def main():
    print(validate_model_score("fraud_v1", 0.94))
    print(validate_model_score("spam_v1", 0.65))
    print(validate_model_score("churn_v1", 1.4))

    print("Direct .py files:", count_python_files("."))
    print("Recursive .py files:", count_python_files_recursive("."))


if __name__ == "__main__":
    main()


"""
DAY 18 NOTES

Logging:
    logging.info(...)
    logging.warning(...)
    logging.error(...)

os.path.exists(path):
    Checks whether a path exists.

os.listdir(path):
    Lists direct items only.
    It does not enter subfolders.

os.path.join(folder, item):
    Builds a full path.

os.path.isfile(path):
    Checks whether the path is a file.

os.path.splitext("app.py"):
    Returns ("app", ".py").

os.walk(path):
    Traverses the directory recursively.

Difference:
    os.listdir() -> current folder only
    os.walk()    -> current folder + nested subfolders

pathlib:
    A modern object-oriented alternative to os.path.
    Day 18 focused on the os-based approach.

Day 18 Takeaways:
- logging gives structured runtime messages
- INFO, WARNING, and ERROR represent different severities
- os.listdir() is non-recursive
- os.walk() is recursive
- os.path.isfile() distinguishes files from folders
- os.path.splitext() helps inspect file extensions
"""
