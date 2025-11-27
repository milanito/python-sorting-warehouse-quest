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
