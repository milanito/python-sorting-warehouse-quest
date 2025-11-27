#!/usr/bin/env python3
"""
run_progress.py

Lightweight test runner for the "Sorting Warehouse Quest" exercises.

- No external libraries needed.
- Runs small tests for ex01..ex06.
- Shows colored progress bars per exercise and a global score.
- Prints a congrats message and a trophy when everything passes.
"""

import sys

# ------------------------------
# ANSI colors and styles
# ------------------------------

RESET = "\033[0m"
BOLD = "\033[1m"

FG_GREEN = "\033[32m"
FG_RED = "\033[31m"
FG_YELLOW = "\033[33m"
FG_BLUE = "\033[34m"
FG_CYAN = "\033[36m"
FG_MAGENTA = "\033[35m"

BOX_LINE = FG_BLUE + "=" * 38 + RESET


def color(text, code):
    return f"{code}{text}{RESET}"


def supports_color():
    return sys.stdout.isatty()


COLOR_ENABLED = supports_color()


def c(text, code):
    if COLOR_ENABLED:
        return color(text, code)
    return text


# ------------------------------
# Small helpers
# ------------------------------

def run_test_case(desc, fn):
    """Run a single test case function fn() -> bool.
    Print result and return True if passed, False otherwise.
    """
    try:
        ok = fn()
    except Exception as e:
        print(f"    {c('[FAIL]', FG_RED)} {desc} (error: {e})")
        return False

    if ok:
        print(f"    {c('[ OK ]', FG_GREEN)} {desc}")
        return True
    else:
        print(f"    {c('[FAIL]', FG_RED)} {desc}")
        return False


def print_progress_bar(label, passed, total, width=20):
    """Simple colored ASCII progress bar."""
    if total <= 0:
        ratio = 0.0
    else:
        ratio = passed / float(total)

    filled = int(width * ratio)
    bar_filled = "█" * filled
    bar_empty = "·" * (width - filled)

    if ratio == 1.0:
        bar_color = FG_GREEN
    elif ratio >= 0.5:
        bar_color = FG_YELLOW
    else:
        bar_color = FG_RED

    bar = c(bar_filled + bar_empty, bar_color)
    percent = int(ratio * 100)

    print(f"{label:10} [{bar}] {passed}/{total} ({percent}%)")


# ------------------------------
# Tests for each exercise
# ------------------------------


def test_ex01():
    print(c("=== ex01_login_id ===", FG_MAGENTA))
    try:
        import ex01_login_id as ex01
    except Exception as e:
        print(f"Import error: {e}")
        return 0, 3

    passed = 0
    total = 0

    total += 1
    def t1():
        return ex01.login_to_char_list("abc") == ['a', 'b', 'c']
    if run_test_case("login_to_char_list('abc')", t1):
        passed += 1

    total += 1
    def t2():
        return ex01.login_to_char_list("") == []
    if run_test_case("login_to_char_list('')", t2):
        passed += 1

    total += 1
    def t3():
        return (ex01.find_dot_position("john.doe") == 4 and
                ex01.find_dot_position("johndoe") == -1)
    if run_test_case("find_dot_position", t3):
        passed += 1

    return passed, total



def test_ex02():
    print(c("=== ex02_login_boxes ===", FG_MAGENTA))
    try:
        import ex02_login_boxes as ex02
    except Exception as e:
        print(f"Import error: {e}")
        return 0, 4

    passed = 0
    total = 0

    total += 1
    def t1():
        return (ex02.char_to_upper("a") == "A" and
                ex02.char_to_upper("z") == "Z" and
                ex02.char_to_upper("A") == "A")
    if run_test_case("char_to_upper on letters", t1):
        passed += 1

    total += 1
    def t2():
        return ex02.char_to_upper("!") == "!"
    if run_test_case("char_to_upper on non letter", t2):
        passed += 1

    total += 1
    def t3():
        return ex02.build_box_labels("ab.cd") == ["A", "B", "C", "D"]
    if run_test_case("build_box_labels('ab.cd')", t3):
        passed += 1

    total += 1
    def t4():
        labels = ["A", "B", "C", "D"]
        before, after = ex02.split_boxes(labels, 2)
        return before == ["A", "B"] and after == ["C", "D"]
    if run_test_case("split_boxes([...], 2)", t4):
        passed += 1

    return passed, total



def test_ex03():
    print(c("=== ex03_min_and_swap ===", FG_MAGENTA))
    try:
        import ex03_min_and_swap as ex03
    except Exception as e:
        print(f"Import error: {e}")
        return 0, 3

    passed = 0
    total = 0

    total += 1
    def t1():
        L = ["D", "A", "C", "B"]
        return ex03.index_of_min(L, 0) == 1
    if run_test_case("index_of_min from 0", t1):
        passed += 1

    total += 1
    def t2():
        L = ["D", "A", "C", "B"]
        return ex03.index_of_min(L, 2) == 3
    if run_test_case("index_of_min from 2", t2):
        passed += 1

    total += 1
    def t3():
        L = ["A", "B", "C"]
        ex03.swap(L, 0, 2)
        return L == ["C", "B", "A"]
    if run_test_case("swap", t3):
        passed += 1

    return passed, total



def test_ex04():
    print(c("=== ex04_selection_sort_step ===", FG_MAGENTA))
    try:
        import ex04_selection_sort_step as ex04
    except Exception as e:
        print(f"Import error: {e}")
        return 0, 2

    passed = 0
    total = 0

    total += 1
    def t1():
        L = ["D", "A", "C", "B"]
        ex04.selection_sort_step(L, 0)
        return L == ["A", "D", "C", "B"]
    if run_test_case("selection_sort_step from 0", t1):
        passed += 1

    total += 1
    def t2():
        L = ["D", "A", "C", "B"]
        ex04.selection_sort_step(L, 0)
        ex04.selection_sort_step(L, 1)
        return L == ["A", "B", "C", "D"]
    if run_test_case("selection_sort_step from 1", t2):
        passed += 1

    return passed, total



def test_ex05():
    print(c("=== ex05_selection_sort_full ===", FG_MAGENTA))
    try:
        import ex05_selection_sort_full as ex05
    except Exception as e:
        print(f"Import error: {e}")
        return 0, 2

    passed = 0
    total = 0

    total += 1
    def t1():
        L = [5, 2, 9, 1, 5, 6]
        ex05.selection_sort(L)
        return L == sorted([5, 2, 9, 1, 5, 6])
    if run_test_case("selection_sort on numbers", t1):
        passed += 1

    total += 1
    def t2():
        L = ["D", "A", "C", "B"]
        ex05.selection_sort(L)
        return L == ["A", "B", "C", "D"]
    if run_test_case("selection_sort on strings", t2):
        passed += 1

    return passed, total



def test_ex06():
    print(c("=== ex06_warehouse_stock ===", FG_MAGENTA))
    try:
        import ex06_warehouse_stock as ex06
    except Exception as e:
        print(f"Import error: {e}")
        return 0, 4

    passed = 0
    total = 0

    total += 1
    def t1():
        labels = ["A", "A", "A", "D", "O", "O"]
        stock = ex06.build_stock_from_labels(labels)
        return stock == [("A", 3), ("D", 1), ("O", 2)]
    if run_test_case("build_stock_from_labels", t1):
        passed += 1

    total += 1
    def t2():
        stock = [("B", 4), ("M", 5), ("O", 1)]
        return ex06.check_stock(stock, 10) and not ex06.check_stock(stock, 9)
    if run_test_case("check_stock", t2):
        passed += 1

    total += 1
    def t3():
        stock = [("B", 4), ("M", 5), ("O", 1)]
        ok1 = ex06.get_stock(stock, "M", 3)
        ok2 = ex06.get_stock(stock, "O", 2)
        return (ok1 is True and ok2 is False and
                stock == [("B", 4), ("M", 2)])
    if run_test_case("get_stock", t3):
        passed += 1

    total += 1
    def t4():
        stock = [("B", 4), ("M", 5), ("O", 1)]
        ok = ex06.shopping(stock, [("M", 1), ("B", 2)])
        return ok is True and stock == [("B", 2), ("M", 4), ("O", 1)]
    if run_test_case("shopping", t4):
        passed += 1

    return passed, total


# ------------------------------
# Trophy
# ------------------------------


def print_trophy():
    print()
    print(c("        .-=========-.", FG_YELLOW))
    print(c("        \'-=======-'/", FG_YELLOW))
    print(c("        _|   .=.   |_", FG_YELLOW))
    print(c("       ((|  {{1}}  |))", FG_YELLOW))
    print(c("        \\   /|\\   |/", FG_YELLOW))
    print(c("         \\__ '`' __/", FG_YELLOW))
    print(c("           _`) (`_", FG_YELLOW))
    print(c("         _/_______\\_", FG_YELLOW))
    print(c("        /___________\\", FG_YELLOW))
    print()
    print(c("You cleared all the tests, champion of the warehouse.", FG_YELLOW))


# ------------------------------
# Overall runner
# ------------------------------


def main():
    print(BOX_LINE)
    print(c("   Sorting Warehouse Quest Tests   ", BOLD + FG_CYAN))
    print(BOX_LINE)
    print()

    exercise_tests = [
        ("ex01", test_ex01),
        ("ex02", test_ex02),
        ("ex03", test_ex03),
        ("ex04", test_ex04),
        ("ex05", test_ex05),
        ("ex06", test_ex06),
    ]

    total_passed = 0
    total_tests = 0
    last_full_ex = 0

    for idx, (name, fn) in enumerate(exercise_tests, start=1):
        print(c(f"[🤖] Checking {name}...", FG_CYAN))
        passed, total = fn()
        print()
        print_progress_bar(name, passed, total)

        total_passed += passed
        total_tests += total

        if total > 0 and passed == total:
            last_full_ex = idx

        print("-" * 40)
        print()

    print(c("============== SUMMARY =============", FG_CYAN))
    print_progress_bar("TOTAL", total_passed, total_tests, width=30)
    print(c("====================================", FG_CYAN))
    print()

    if total_tests == 0:
        print("No tests were run. Check that all exercise files exist.")
        return

    ratio = total_passed / float(total_tests)

    if total_passed == 0:
        print("You have not passed any test yet.")
        print("This is just the starting point. Try to complete ex01 first, step by step.")
    elif ratio < 0.3:
        print("Good start. You already solved some tests.")
        print("Focus on ex01 and ex02. Once they are solid, the rest will be easier.")
    elif ratio < 0.7:
        print("Nice progress. You are on your way.")
        print("Try to stabilize selection sort in ex03 to ex05. It will help a lot for the final.")
    elif ratio < 1.0:
        print("Great job. You passed most of the tests.")
        print("Take a moment to re read your code, clean it up, and push yourself on ex06.")
    else:
        print(c("Amazing. You passed ALL the tests.", FG_GREEN))
        print_trophy()

    if last_full_ex >= 1:
        print()
        print(f"You have completely validated exercises up to ex0{last_full_ex}. Keep going.")


if __name__ == "__main__":
    main()
