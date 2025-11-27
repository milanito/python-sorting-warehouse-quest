#!/usr/bin/env bash
set -e

# run_exercise.sh
# Run tests for a single exercise (or all).
#
# Usage:
#   ./run_exercise.sh 3
#   ./run_exercise.sh ex03
#   ./run_exercise.sh all

if [ $# -ne 1 ]; then
  echo "Usage: $0 <1-6 | ex01-ex06 | all>"
  exit 1
fi

ARG="$1"

case "$ARG" in
  1|ex01)
    EX_NAME="ex01"
    PY_CODE='from run_progress import test_ex01, print_progress_bar, c, FG_CYAN, BOX_LINE
print(BOX_LINE)
print(c("   Running tests for ex01_login_id   ", FG_CYAN))
print(BOX_LINE)
print()
passed, total = test_ex01()
print()
print_progress_bar("ex01", passed, total)
print()
if total > 0 and passed == total:
    print("All tests passed for ex01. Nice job!")
else:
    print("Some tests failed for ex01. Check your functions and try again.")
'
    ;;
  2|ex02)
    EX_NAME="ex02"
    PY_CODE='from run_progress import test_ex02, print_progress_bar, c, FG_CYAN, BOX_LINE
print(BOX_LINE)
print(c("   Running tests for ex02_login_boxes   ", FG_CYAN))
print(BOX_LINE)
print()
passed, total = test_ex02()
print()
print_progress_bar("ex02", passed, total)
print()
if total > 0 and passed == total:
    print("All tests passed for ex02. Great!")
else:
    print("Some tests failed for ex02. Use hints if you are stuck.")
'
    ;;
  3|ex03)
    EX_NAME="ex03"
    PY_CODE='from run_progress import test_ex03, print_progress_bar, c, FG_CYAN, BOX_LINE
print(BOX_LINE)
print(c("   Running tests for ex03_min_and_swap   ", FG_CYAN))
print(BOX_LINE)
print()
passed, total = test_ex03()
print()
print_progress_bar("ex03", passed, total)
print()
if total > 0 and passed == total:
    print("All tests passed for ex03. Your min/swap tools are solid.")
else:
    print("Some tests failed for ex03. Focus on index_of_min and swap.")
'
    ;;
  4|ex04)
    EX_NAME="ex04"
    PY_CODE='from run_progress import test_ex04, print_progress_bar, c, FG_CYAN, BOX_LINE
print(BOX_LINE)
print(c("   Running tests for ex04_selection_sort_step   ", FG_CYAN))
print(BOX_LINE)
print()
passed, total = test_ex04()
print()
print_progress_bar("ex04", passed, total)
print()
if total > 0 and passed == total:
    print("All tests passed for ex04. One step of selection sort looks good.")
else:
    print("Some tests failed for ex04. Check how you use index_of_min and swap.")
'
    ;;
  5|ex05)
    EX_NAME="ex05"
    PY_CODE='from run_progress import test_ex05, print_progress_bar, c, FG_CYAN, BOX_LINE
print(BOX_LINE)
print(c("   Running tests for ex05_selection_sort_full   ", FG_CYAN))
print(BOX_LINE)
print()
passed, total = test_ex05()
print()
print_progress_bar("ex05", passed, total)
print()
if total > 0 and passed == total:
    print("All tests passed for ex05. Your selection sort is ready!")
else:
    print("Some tests failed for ex05. Check the main loop over start.")
'
    ;;
  6|ex06)
    EX_NAME="ex06"
    PY_CODE='from run_progress import test_ex06, print_progress_bar, c, FG_CYAN, BOX_LINE
print(BOX_LINE)
print(c("   Running tests for ex06_warehouse_stock   ", FG_CYAN))
print(BOX_LINE)
print()
passed, total = test_ex06()
print()
print_progress_bar("ex06", passed, total)
print()
if total > 0 and passed == total:
    print("All tests passed for ex06. Impressive, this one is harder than the final.")
else:
    print("Some tests failed for ex06. Work step by step: build_stock, check_stock, get_stock, shopping.")
'
    ;;
  all)
    echo "Running full test suite (all exercises)..."
    python3 run_progress.py
    exit 0
    ;;
  *)
    echo "Unknown argument: $ARG"
    echo "Usage: $0 <1-6 | ex01-ex06 | all>"
    exit 1
    ;;
esac

python3 - << PYEOF
$PY_CODE
PYEOF
