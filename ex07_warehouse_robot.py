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
