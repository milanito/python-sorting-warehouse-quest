#!/usr/bin/env python3
"""visual_selection_sort.py

Small ASCII visualizer for your selection sort.

It uses your implementation of selection_sort from ex05 to sort
some example lists, and prints the list as bars of different height.

This is OPTIONAL and only for understanding/debugging.
"""

from ex05_selection_sort_full import selection_sort


def show_bars(L):
    """Print a simple bar representation of a list of integers."""
    # Normalize values to max height 10 for display
    if not L:
        print("(empty list)")
        return

    max_val = max(L)
    if max_val <= 0:
        max_val = 1

    heights = []
    for x in L:
        h = int(10 * x / max_val)
        if h < 1 and x > 0:
            h = 1
        heights.append(h)

    lines = []
    for h in heights:
        lines.append("█" * h)

    print("Values:", L)
    print("Bars:  ", end="")
    for s in lines:
        if s == "":
            print(".", end=" ")
        else:
            print(s, end=" ")
    print()


def demo_once(L):
    print("==============================")
    print("Original list:")
    show_bars(L)
    print()

    # We want to show intermediate steps. We will copy the list
    # and re implement a step by step loop calling selection_sort
    # idea, but since selection_sort does everything at once,
    # here we just call it and then show the final result.
    #
    # If you want step by step visualization, you can modify
    # ex04 or ex05 to print the list at each step.

    selection_sort(L)

    print("Sorted:")
    show_bars(L)
    print("==============================")
    print()


def main():
    print("Visual selection sort demo")
    print("(Using your own selection_sort implementation.)")
    print()

    demo_once([5, 2, 9, 1, 5, 6])
    demo_once([3, 1, 4, 1, 5, 9, 2])


if __name__ == "__main__":
    main()
