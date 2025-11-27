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
