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
