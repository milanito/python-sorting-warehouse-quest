#!/usr/bin/env python3
"""show_hint.py

Usage:
    python3 show_hint.py N

where N is the exercise number (1 to 6).

Prints a few progressive hints to help you unblock yourself
without giving the full solution.
"""

import sys


HINTS = {
    1: [
        "Use a while loop with an index i to walk through the string.",
        "To build the list of characters, start with an empty list and append login[i].",
        "To find the dot position, return i as soon as login[i] == '.'. If you reach the end, return -1.",
    ],
    2: [
        "Use ord and chr to convert lowercase letters to uppercase (distance between 'a' and 'A').",
        "Ignore '.' when building labels. Only convert letters.",
        "In split_boxes, the number of labels before the dot is equal to dot_position.",
    ],
    3: [
        "index_of_min: start with min_index = start, then scan the rest of the list.",
        "If L[i] < L[min_index], update min_index.",
        "swap: use a temporary variable to exchange L[i] and L[j].",
    ],
    4: [
        "Use index_of_min(L, start) to find the position of the smallest element.",
        "Then call swap(L, start, that_min_index).",
        "selection_sort_step does not need a loop: it is one single operation.",
    ],
    5: [
        "selection_sort: loop on start from 0 to len(L)-1.",
        "At each step, call selection_sort_step(L, start).",
        "After each step, the prefix L[:start+1] is sorted.",
    ],
    6: [
        "build_stock_from_labels: labels are already sorted, so equal letters are grouped.",
        "Walk once through labels, count how many times the current letter repeats, then append (letter, count).",
        "check_stock: sum all quantities and compare with capacity.",
        "get_stock: find the object; if qty <= request, remove it (pop); otherwise, reduce the quantity.",
        "shopping: for each request, call get_stock and stop with False if something fails.",
    ],
}


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 show_hint.py N  (with N from 1 to 6)")
        return

    try:
        num = int(sys.argv[1])
    except ValueError:
        print("N must be a number between 1 and 6.")
        return

    if num not in HINTS:
        print("No hints for this exercise number. Use a value between 1 and 6.")
        return

    print(f"Hints for exercise ex0{num}:")
    print("----------------------------")
    for i, hint in enumerate(HINTS[num], start=1):
        print(f"Hint {i}: {hint}")


if __name__ == "__main__":
    main()
