"""
ex04 – One step of selection sort

Goal:
- Implement a single step of the selection sort algorithm.

Reminder:
At step `start`:
- Find the smallest element in L[start:]
- Swap it with L[start]
"""

from ex03_min_and_swap import index_of_min, swap


def selection_sort_step(L, start):
    """Perform ONE step of selection sort on L starting at index `start`.

    If start is out of range, do nothing.
    """
    # TODO:
    # 1) check if start is in [0, len(L)-1]
    # 2) find index of minimum in L[start:] using index_of_min
    # 3) swap that element with L[start]
    pass


def main():
    boxes = ['D', 'A', 'C', 'B']
    print("Before step from 0:", boxes)
    selection_sort_step(boxes, 0)
    print("After step from 0:", boxes)


if __name__ == "__main__":
    main()
