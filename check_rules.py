#!/usr/bin/env python3
"""
check_rules.py

Static checker for forbidden Python patterns in the exercises.

Usage:
    python3 check_rules.py

It will inspect:
    ex01_login_id.py
    ex02_login_boxes.py
    ex03_min_and_swap.py
    ex04_selection_sort_step.py
    ex05_selection_sort_full.py
    ex06_warehouse_stock.py
    ex07_warehouse_robot.py  (if present)

And report:
    - slicing: L[1:3]
    - list comprehensions: [x for x in L]
    - shortcuts: min, max, sum, sorted, .sort

It ignores:
    - lines that are comments (# ...)
    - lines inside triple-quoted strings (docstrings / big comments)
"""

import re
from pathlib import Path

FILES = [
    "ex01_login_id.py",
    "ex02_login_boxes.py",
    "ex03_min_and_swap.py",
    "ex04_selection_sort_step.py",
    "ex05_selection_sort_full.py",
    "ex06_warehouse_stock.py",
    "ex07_warehouse_robot.py",
]

RULES = [
    ("Slicing (L[...:...])", re.compile(r"\[[^]]*:[^]]*\]")),
    ("List comprehension ([... for ... in ...])", re.compile(r"\[[^]]*for[^]]*in[^]]*\]")),
    ("Built-in shortcut min(", re.compile(r"\bmin\s*\(")),
    ("Built-in shortcut max(", re.compile(r"\bmax\s*\(")),
    ("Built-in shortcut sum(", re.compile(r"\bsum\s*\(")),
    ("Built-in shortcut sorted(", re.compile(r"\bsorted\s*\(")),
    ("List sort method .sort(", re.compile(r"\.sort\s*\(")),
]

RESET = "\033[0m"
FG_RED = "\033[31m"
FG_GREEN = "\033[32m"
FG_YELLOW = "\033[33m"


def c(text, code):
    try:
        import sys
        if not sys.stdout.isatty():
            return text
    except Exception:
        return text
    return f"{code}{text}{RESET}"


def check_file(path: Path):
    issues = []
    if not path.exists():
        return issues

    in_triple_string = False

    with path.open("r", encoding="utf-8") as f:
        for lineno, raw_line in enumerate(f, start=1):
            line = raw_line.rstrip("\n")
            stripped = line.lstrip()

            # Count triple-quote markers on this line
            triple_count = line.count('"""') + line.count("'''")

            if in_triple_string:
                # We are inside a docstring / big comment: skip scanning
                # but we still need to see if we leave it on this line.
                if triple_count % 2 == 1:
                    in_triple_string = False
                continue

            # Not currently in a triple-quoted string
            if triple_count > 0:
                # This line starts/ends a triple-quoted string.
                # Skip scanning this line as well (it is part of the docstring).
                if triple_count % 2 == 1:
                    in_triple_string = True
                # If triple_count is even, opening and closing on same line,
                # we still skip scanning it.
                continue

            # Ignore # comments
            if stripped.startswith("#"):
                continue

            # Now scan for forbidden patterns in real code lines
            for rule_name, pattern in RULES:
                if pattern.search(line):
                    issues.append((lineno, rule_name, line.rstrip("\n")))
    return issues


def main():
    all_issues = []
    print("Checking forbidden patterns in exercises...")
    print()

    for fname in FILES:
        path = Path(fname)
        if not path.exists():
            continue

        issues = check_file(path)
        if not issues:
            print(c(f"[OK ] {fname}", FG_GREEN))
        else:
            print(c(f"[WARN] {fname}", FG_YELLOW))
            for lineno, rule_name, text in issues:
                print(
                    "  "
                    + c(f"line {lineno}:", FG_RED),
                    c(rule_name + " ->", FG_RED),
                    text.strip(),
                )
            all_issues.extend((fname, *issue) for issue in issues)

    print()
    if not all_issues:
        print(c("No forbidden patterns detected. Nice job keeping it algorithmic.", FG_GREEN))
    else:
        print(c("Some forbidden patterns were found. Please fix them before the exam.", FG_RED))


if __name__ == "__main__":
    main()
