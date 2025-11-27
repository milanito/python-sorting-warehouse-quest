"""
ex03 – Finding the smallest box and swapping

Goal:
- Implement the basic operations needed for selection sort:
  - finding the index of the smallest element in a list
  - swapping two elements in a list

These functions are used in the next exercises.
"""


def index_of_min(L, start):
    """Return the index of the smallest element in L[start:].

    Pre-conditions:
    - 0 <= start < len(L)
    - L is not empty

    You must use a loop and comparisons, no min().
    """
    # TODO:
    # 1) set min_index = start
    # 2) scan the list from start+1 to end
    # 3) if L[i] < L[min_index], update min_index
    # 4) return min_index
    pass


def swap(L, i, j):
    """Swap L[i] and L[j] in place.

    Use a temporary variable. Do not return anything.
    """
    # TODO:
    # temp = ...
    # L[i] = ...
    # L[j] = ...
    pass


def main():
    boxes = ['D', 'A', 'C', 'B']
    print("Original boxes:", boxes)
    print("index_of_min from 0:", index_of_min(boxes, 0))
    print("index_of_min from 2:", index_of_min(boxes, 2))
    swap(boxes, 0, 3)
    print("After swap(0,3):", boxes)


if __name__ == "__main__":
    main()
