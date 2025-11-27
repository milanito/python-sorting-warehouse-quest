"""
ex05 – Full selection sort

Goal:
- Use selection_sort_step to fully sort a list.

Algorithm idea:
For start from 0 to len(L)-1:
    - put the smallest element of L[start:] at position start

You must modify the list in place.
"""

from ex04_selection_sort_step import selection_sort_step
from ex02_login_boxes import MY_LOGIN, build_box_labels


def selection_sort(L):
    """Sort the list L in place using selection sort.

    Use a while or for loop and selection_sort_step.
    """
    # TODO:
    # for start in range(...):
    #     selection_sort_step(L, start)
    pass


def main():
    print("=== Sorting box labels from login ===")
    labels = build_box_labels(MY_LOGIN)
    print("Before sort:", labels)
    selection_sort(labels)
    print("After sort: ", labels)

    print()
    print("=== Sorting a list of numbers ===")
    nums = [5, 2, 9, 1, 5, 6]
    print("Before sort:", nums)
    selection_sort(nums)
    print("After sort: ", nums)


if __name__ == "__main__":
    main()
