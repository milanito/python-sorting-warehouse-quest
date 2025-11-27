#!/usr/bin/env bash
set -e

# make_student_skeletons.sh
# Run this script from the ROOT of the repo.
# It will OVERWRITE ex01..ex07 with *student versions* (no solutions).
#
# Each exercise keeps:
#   - story
#   - docstrings
#   - function signatures
# And removes:
#   - actual algorithm code
#   - subtle hidden solutions
#
# The difficulty is slightly higher than before: fewer cloze lines,
# more real thinking required, especially from ex03 onward.

########################################
# ex01_login_id.py
########################################
cat << 'EOF' > ex01_login_id.py
"""
ex01 – Personal login ID

Goal:
- Start from your EPITA login (for example: "matthieu.rondeau").
- Extract useful information to create your warehouse engineer ID.

Story:
The warehouse system wants a stable ID for each engineer, based on their login.
We decide to use:
- the whole login as a string
- the list of characters of the login (without any shortcut)
- the position of the dot '.' separating first name and last name

Tasks:
1) Set the constant MY_LOGIN to your own login as a string.
   Example: MY_LOGIN = "firstname.lastname"

2) Complete the functions below.

Rules:
- Use only basic Python: while, if, len, range, append, pop.
- No slicing, no list(), no enumerate, no fancy tricks.
"""

# TODO: change this to your real login
MY_LOGIN = "firstname.lastname"


def login_to_char_list(login):
    """Convert the login string to a list of characters.

    Example:
    >>> login_to_char_list("abc")
    ['a', 'b', 'c']

    Implement this WITHOUT using list(login).
    """
    # TODO: create an empty list of characters
    # TODO: use a while loop with an index i
    # TODO: append login[i] at each step
    # TODO: return the list
    pass


def find_dot_position(login):
    """Return the index of '.' in the login string, or -1 if not found.

    Example:
    >>> find_dot_position("john.doe")
    4
    >>> find_dot_position("johndoe")
    -1
    """
    # TODO: scan the string with a while loop
    # if login[i] == '.', return i
    # if you reach the end, return -1
    pass


def main():
    print("MY_LOGIN =", MY_LOGIN)
    print("Characters of login:", login_to_char_list(MY_LOGIN))
    print("Position of '.' in login:", find_dot_position(MY_LOGIN))


if __name__ == "__main__":
    main()
EOF

########################################
# ex02_login_boxes.py
########################################
cat << 'EOF' > ex02_login_boxes.py
"""
ex02 – From login to box labels

Goal:
- Use the functions from ex01 to create box labels for your personal lane.

Story:
Each engineer has a personal lane in the warehouse.
The lane is identified by a list of box labels derived from their login.

We will use:
- the characters of the login
- the position of '.' between first name and last name

You must:
- convert lowercase letters to uppercase using ord/chr
- ignore the '.' character
- split box labels into two parts (before and after the dot)
"""

from ex01_login_id import MY_LOGIN, login_to_char_list, find_dot_position


def char_to_upper(c):
    """Convert a single character to uppercase if it is lowercase.

    Use ord() and chr().
    If c is not a lowercase letter, return it unchanged.
    """
    # Hint:
    #   - lowercase letters go from 'a' to 'z'
    #   - uppercase letters go from 'A' to 'Z'
    #   - distance between 'a' and 'A' is always the same
    # TODO: implement this function
    pass


def build_box_labels(login):
    """Return a list of uppercase letters based on the login, ignoring '.'.

    Example:
    >>> build_box_labels("ab.cd")
    ['A', 'B', 'C', 'D']
    """
    # TODO:
    # 1) get characters using login_to_char_list(login)
    # 2) loop over them
    # 3) if char is not '.', convert with char_to_upper and append to labels
    pass


def split_boxes(box_labels, dot_position):
    """Split the box labels into two lists:
      - labels_before: labels from characters before '.'
      - labels_after: labels from characters after '.'

    The number of labels before the dot is equal to dot_position.

    DO NOT use slicing. Use a while loop and append.
    """
    # TODO: create labels_before and labels_after, fill them with a while loop
    pass


def main():
    print("MY_LOGIN =", MY_LOGIN)
    dot_pos = find_dot_position(MY_LOGIN)
    print("Dot position =", dot_pos)

    labels = build_box_labels(MY_LOGIN)
    print("Box labels =", labels)

    if dot_pos != -1:
        before, after = split_boxes(labels, dot_pos)
        print("Labels before dot:", before)
        print("Labels after dot:", after)
    else:
        print("No '.' in login, no split performed.")


if __name__ == "__main__":
    main()
EOF

########################################
# ex03_min_and_swap.py
########################################
cat << 'EOF' > ex03_min_and_swap.py
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
    # temp = L[i]
    # L[i] = L[j]
    # L[j] = temp
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
EOF

########################################
# ex04_selection_sort_step.py
########################################
cat << 'EOF' > ex04_selection_sort_step.py
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
EOF

########################################
# ex05_selection_sort_full.py
########################################
cat << 'EOF' > ex05_selection_sort_full.py
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
EOF

########################################
# ex06_warehouse_stock.py
########################################
cat << 'EOF' > ex06_warehouse_stock.py
"""
ex06 – Warehouse stock (harder, exam-style)

Goal:
- Combine your own sorting algorithm with stock management.

You will:
1) sort labels using selection_sort
2) build a stock: list of (object, quantity)
3) implement operations on that stock

This is close to the exam difficulty (slightly harder).
"""

from ex05_selection_sort_full import selection_sort
from ex02_login_boxes import MY_LOGIN, build_box_labels


def build_stock_from_labels(labels):
    """Build a stock (list of (obj, quantity)) from a sorted list of labels.

    Example:
    ['A','A','A','D','O','O'] -> [('A',3), ('D',1), ('O',2)]

    Precondition: labels is sorted.
    """
    # TODO:
    # Walk once through labels, count identical letters in a row,
    # and append (letter, count) to stock.
    pass


def check_stock(stock, capacity):
    """Return True if total quantity in stock <= capacity, else False.

    stock: list of (obj, quantity)
    capacity: integer >= 0
    """
    # TODO:
    # sum quantities with a loop (no sum()) and compare to capacity
    pass


def get_stock(stock, obj, request):
    """Remove `request` units of `obj` from stock if present.

    - If obj not found: return False, stock unchanged.
    - If quantity <= request: remove (obj, quantity) from stock, return False.
    - If quantity > request: decrease quantity, return True.

    Stock is modified in place.
    """
    # TODO:
    # 1) search for obj in stock
    # 2) apply the rules above using pop and tuple replacement
    pass


def shopping(stock, requests):
    """Process a list of requests (obj, request) on the stock.

    Return False as soon as an object was not present or removed.
    Return True if all operations keep requested objects in stock.

    Stock is modified in place.
    """
    # TODO:
    # Loop over requests, call get_stock, and stop early if needed.
    pass


def demo_with_login():
    """Small demo using the student's login.

    1) Build labels from login
    2) Sort them
    3) Build stock
    """
    labels = build_box_labels(MY_LOGIN)
    selection_sort(labels)
    stock = build_stock_from_labels(labels)
    print("Stock from login:", stock)


def main():
    demo_with_login()


if __name__ == "__main__":
    main()
EOF

########################################
# ex07_warehouse_robot.py (BONUS, harder)
########################################
cat << 'EOF' > ex07_warehouse_robot.py
"""
ex07 – Warehouse robot console (BONUS)

Goal:
- Use your stock functions from ex06 in a small interactive console.
- Practice reading input, splitting commands, and looping.

Commands (strings typed by the user):

  ADD <OBJ> <QTY>
      Add QTY units of OBJ to the stock.

  TAKE <OBJ> <QTY>
      Remove QTY units of OBJ using get_stock.

  SHOW
      Print the current stock.

  CHECK <CAPACITY>
      Check if the total quantity in stock <= CAPACITY.

  HELP
      Show the list of commands.

  QUIT
      Exit the program.

This exercise is optional but very good training.
"""

from ex06_warehouse_stock import build_stock_from_labels, check_stock, get_stock
from ex02_login_boxes import MY_LOGIN, build_box_labels
from ex05_selection_sort_full import selection_sort


def build_initial_stock_from_login():
    """Build an initial stock based on the student's login.

    Steps:
    - build labels from login
    - sort them
    - build stock from labels
    """
    # TODO: implement this function using the imported helpers
    pass


def handle_add(stock, parts):
    """Handle command: ADD <OBJ> <QTY>.

    - If OBJ already in stock, increase its quantity.
    - Otherwise, insert it keeping stock sorted by OBJ.
    """
    # TODO: parse parts, convert QTY to int, and update stock
    # You can create helper functions if you want.
    pass


def handle_take(stock, parts):
    """Handle command: TAKE <OBJ> <QTY>.

    Use get_stock to update stock.
    """
    # TODO: parse parts, call get_stock, print a message depending on result
    pass


def handle_show(stock):
    """Print the current stock in a readable way."""
    # TODO: loop over stock and print each (obj, qty)
    pass


def handle_check(stock, parts):
    """Handle command: CHECK <CAPACITY>."""
    # TODO: parse capacity, call check_stock, print result
    pass


def handle_help():
    """Print the list of available commands."""
    # TODO: just print the commands and a short description
    pass


def main():
    print("=== ex07 – Warehouse robot console (BONUS) ===")
    print("Type HELP for the list of commands.")
    print()

    stock = build_initial_stock_from_login()
    print("Initial stock:", stock)
    print()

    while True:
        try:
            line = input("robot> ")
        except EOFError:
            print()
            break

        line = line.strip()
        if line == "":
            continue

        parts = line.split()
        cmd = parts[0].upper()

        if cmd == "ADD":
            handle_add(stock, parts)
        elif cmd == "TAKE":
            handle_take(stock, parts)
        elif cmd == "SHOW":
            handle_show(stock)
        elif cmd == "CHECK":
            handle_check(stock, parts)
        elif cmd == "HELP":
            handle_help()
        elif cmd == "QUIT":
            print("Goodbye, warehouse engineer.")
            break
        else:
            print("Unknown command. Type HELP if you are lost.")


if __name__ == "__main__":
    main()
EOF


echo "Student skeletons written for ex01..ex07 (no solutions)."