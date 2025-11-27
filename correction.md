# Sorting Warehouse Quest – Full Corrections

> This document summarizes the intended solutions and reasoning for each exercise.
>
> Code respects the same constraints as the students: no slicing, no list comprehensions, no `min` / `max` / `sum` / `sorted` / `.sort()` in ex01–ex06.

---

## ex01 – Personal login ID

### 1. Constant `MY_LOGIN`

Students must set:

```python
MY_LOGIN = "firstname.lastname"  # their real login
```

You can check that they really changed it.

### 2. Function `login_to_char_list(login)`

**Goal:** Convert a string to a list of characters without using `list(login)`.

**Key idea:** Walk through the string with a `while` loop and build a new list.

```python
def login_to_char_list(login):
    """Convert the login string to a list of characters (no list())."""
    chars = []
    i = 0
    while i < len(login):
        chars.append(login[i])
        i = i + 1
    return chars
```

**Common mistakes:**

* Using `list(login)` (forbidden shortcut).
* Forgetting to increment `i`, causing infinite loops.

### 3. Function `find_dot_position(login)`

**Goal:** Return the index of `'.'` in the string, or `-1` if not found.

**Key idea:** Linear scan with early return.

```python
def find_dot_position(login):
    """Return the index of '.' in the login string, or -1 if not found."""
    i = 0
    while i < len(login):
        if login[i] == '.':
            return i
        i = i + 1
    return -1
```

**Common mistakes:**

* Returning `0` when no dot is found instead of `-1`.
* Using `login.index('.')` (raises exceptions and hides the algorithm).

---

## ex02 – From login to box labels

### 1. Function `char_to_upper(c)`

**Goal:** Convert a lowercase letter to uppercase using `ord`/`chr`. Other characters stay unchanged.

**Key idea:** Distance between `'a'` and `'A'` is constant.

```python
def char_to_upper(c):
    """Convert a single character to uppercase if it is lowercase."""
    if c >= 'a' and c <= 'z':
        diff = ord('a') - ord('A')
        code = ord(c) - diff
        return chr(code)
    return c
```

**Common mistakes:**

* Using `c.upper()` (forbidden shortcut).
* Not handling non-letter characters correctly.

### 2. Function `build_box_labels(login)`

**Goal:** From the login, build a list of uppercase labels, ignoring the dot.

**Key idea:** Reuse `login_to_char_list` and `char_to_upper`.

```python
def build_box_labels(login):
    """Return a list of uppercase letters based on the login, ignoring '.'."""
    chars = login_to_char_list(login)
    labels = []
    i = 0
    while i < len(chars):
        c = chars[i]
        if c != '.':
            labels.append(char_to_upper(c))
        i = i + 1
    return labels
```

**Common mistakes:**

* Forgetting to ignore `'.'`.
* Rebuilding the string and then calling `upper()`.

### 3. Function `split_boxes(box_labels, dot_position)`

**Goal:** Split list of labels into `labels_before` and `labels_after` accordingly.

* `labels_before` contains the first `dot_position` labels.
* `labels_after` contains the remaining labels.

**Constraint:** No slicing (`box_labels[:dot_position]` is forbidden).

```python
def split_boxes(box_labels, dot_position):
    """Split box_labels into two lists based on dot_position."""
    labels_before = []
    labels_after = []

    i = 0
    while i < len(box_labels):
        if i < dot_position:
            labels_before.append(box_labels[i])
        else:
            labels_after.append(box_labels[i])
        i = i + 1

    return labels_before, labels_after
```

**Common mistakes:**

* Using slicing.
* Confusing `dot_position` (from the string) and index in labels (though they match for this construction).

---

## ex03 – Finding the smallest box and swapping

### 1. Function `index_of_min(L, start)`

**Goal:** Return index of the smallest element in `L[start:]`.

**Key idea:** Classic linear search of minimum.

```python
def index_of_min(L, start):
    """Return the index of the smallest element in L[start:]."""
    min_index = start
    i = start + 1
    while i < len(L):
        if L[i] < L[min_index]:
            min_index = i
        i = i + 1
    return min_index
```

**Common mistakes:**

* Writing `min(L[start:])` and then using `.index()` (forbidden + more complex).
* Comparing indices instead of values.

### 2. Function `swap(L, i, j)`

**Goal:** Swap `L[i]` and `L[j]` in place using a temporary variable.

```python
def swap(L, i, j):
    """Swap L[i] and L[j] in place."""
    temp = L[i]
    L[i] = L[j]
    L[j] = temp
```

**Common mistakes:**

* Using `L[i], L[j] = L[j], L[i]` – this is acceptable logically, but you may decide if it fits your constraints.
* Forgetting that lists are mutated in place (no `return` needed).

---

## ex04 – One step of selection sort

### Function `selection_sort_step(L, start)`

**Goal:** Perform one selection sort step:

* find smallest element in `L[start:]`
* swap it into position `start`

```python
from ex03_min_and_swap import index_of_min, swap


def selection_sort_step(L, start):
    """Perform ONE step of selection sort on L starting at index `start`."""
    if start < 0 or start >= len(L):
        return
    min_index = index_of_min(L, start)
    swap(L, start, min_index)
```

**Common mistakes:**

* Trying to implement the full sort here.
* Ignoring the `start` boundary check.

---

## ex05 – Full selection sort

### Function `selection_sort(L)`

**Goal:** Sort `L` in place using selection sort.

**Algorithm:**

For each `start` from `0` to `len(L) - 1`:

* place the smallest of `L[start:]` at position `start`.

```python
from ex04_selection_sort_step import selection_sort_step
from ex02_login_boxes import MY_LOGIN, build_box_labels


def selection_sort(L):
    """Sort the list L in place using selection sort."""
    start = 0
    while start < len(L):
        selection_sort_step(L, start)
        start = start + 1
```

**Common mistakes:**

* Off-by-one in the loop (`<= len(L)` instead of `< len(L)`).
* Forgetting to call `selection_sort_step`.

---

## ex06 – Warehouse stock (exam-style)

### 1. Function `build_stock_from_labels(labels)`

**Goal:** Group identical labels from a sorted list into `(obj, quantity)` pairs.

Example:

* `['A','A','A','D','O','O']` → `[('A', 3), ('D', 1), ('O', 2)]`

```python
def build_stock_from_labels(labels):
    """Build a stock (list of (obj, quantity)) from a sorted list of labels."""
    stock = []
    if len(labels) == 0:
        return stock

    current_obj = labels[0]
    current_count = 1

    i = 1
    while i < len(labels):
        if labels[i] == current_obj:
            current_count = current_count + 1
        else:
            stock.append((current_obj, current_count))
            current_obj = labels[i]
            current_count = 1
        i = i + 1

    stock.append((current_obj, current_count))
    return stock
```

**Common mistakes:**

* Forgetting to append the last group.
* Resetting `current_count` incorrectly.

### 2. Function `check_stock(stock, capacity)`

**Goal:** Return `True` if total quantity in stock is ≤ `capacity`, else `False`.

```python
def check_stock(stock, capacity):
    """Return True if total quantity in stock <= capacity, else False."""
    total = 0
    i = 0
    while i < len(stock):
        obj, qty = stock[i]
        total = total + qty
        i = i + 1
    return total <= capacity
```

**Common mistakes:**

* Using `sum(qty for _, qty in stock)` (list comprehension + sum).

### 3. Function `get_stock(stock, obj, request)`

**Goal:** Remove `request` units of `obj` from stock.

Rules:

* If `obj` not found → return `False`, stock unchanged.
* If `qty <= request` → remove the pair, return `False`.
* If `qty > request` → decrease qty, return `True`.

```python
def get_stock(stock, obj, request):
    """Remove `request` units of `obj` from stock if present."""
    i = 0
    while i < len(stock):
        current_obj, qty = stock[i]
        if current_obj == obj:
            if qty <= request:
                stock.pop(i)
                return False
            else:
                stock[i] = (current_obj, qty - request)
                return True
        i = i + 1
    return False
```

**Common mistakes:**

* Returning `True` when the object is removed (opposite of spec).
* Forgetting to update the list in place.

### 4. Function `shopping(stock, requests)`

**Goal:** Process a list of `(obj, request)` on the stock.

* If any operation removes or fails an object → return `False`.
* If all operations keep objects in stock → return `True`.

```python
def shopping(stock, requests):
    """Process a list of requests (obj, request) on the stock."""
    i = 0
    while i < len(requests):
        obj, req = requests[i]
        still_there = get_stock(stock, obj, req)
        if not still_there:
            return False
        i = i + 1
    return True
```

**Common mistakes:**

* Ignoring the return value of `get_stock`.
* Returning `True` even if something was removed.

---

## ex07 – Warehouse robot console (bonus)

This is optional and mainly for motivation. It uses the functions from ex06.

### 1. Function `build_initial_stock_from_login()`

**Goal:** Build initial stock using the student’s login.

Steps:

* build labels from login
* sort them
* build stock

```python
from ex06_warehouse_stock import build_stock_from_labels
from ex02_login_boxes import MY_LOGIN, build_box_labels
from ex05_selection_sort_full import selection_sort


def build_initial_stock_from_login():
    labels = build_box_labels(MY_LOGIN)
    selection_sort(labels)
    stock = build_stock_from_labels(labels)
    return stock
```

### 2. Command handlers

Commands:

* `ADD <OBJ> <QTY>` – add quantity, keeping stock sorted.
* `TAKE <OBJ> <QTY>` – use `get_stock` to remove.
* `SHOW` – print stock.
* `CHECK <CAPACITY>` – use `check_stock`.
* `HELP` – print help.
* `QUIT` – exit.

Example reference implementation (you can simplify it if needed):

```python
from ex06_warehouse_stock import build_stock_from_labels, check_stock, get_stock


def handle_add(stock, parts):
    if len(parts) != 3:
        print("Usage: ADD <OBJ> <QTY>")
        return

    obj = parts[1]
    try:
        qty = int(parts[2])
    except ValueError:
        print("QTY must be an integer.")
        return

    if qty <= 0:
        print("QTY must be > 0.")
        return

    i = 0
    found_index = -1
    while i < len(stock):
        current_obj, current_qty = stock[i]
        if current_obj == obj:
            found_index = i
            break
        i = i + 1

    if found_index != -1:
        current_obj, current_qty = stock[found_index]
        stock[found_index] = (current_obj, current_qty + qty)
    else:
        stock.append((obj, qty))
        j = len(stock) - 1
        while j > 0 and stock[j][0] < stock[j - 1][0]:
            tmp = stock[j - 1]
            stock[j - 1] = stock[j]
            stock[j] = tmp
            j = j - 1

    print("OK: added", qty, "of", obj)
```

```python
def handle_take(stock, parts):
    if len(parts) != 3:
        print("Usage: TAKE <OBJ> <QTY>")
        return

    obj = parts[1]
    try:
        qty = int(parts[2])
    except ValueError:
        print("QTY must be an integer.")
        return

    if qty <= 0:
        print("QTY must be > 0.")
        return

    still_there = get_stock(stock, obj, qty)
    if still_there:
        print("OK: took", qty, "of", obj, "(still in stock)")
    else:
        print("OK: took", qty, "of", obj, "(removed or not found)")
```

```python
def handle_show(stock):
    if len(stock) == 0:
        print("(empty stock)")
        return
    print("Current stock:")
    i = 0
    while i < len(stock):
        obj, qty = stock[i]
        print(" -", obj, ":", qty)
        i = i + 1
```

```python
def handle_check(stock, parts):
    if len(parts) != 2:
        print("Usage: CHECK <CAPACITY>")
        return
    try:
        capacity = int(parts[1])
    except ValueError:
        print("CAPACITY must be an integer.")
        return
    if capacity < 0:
        print("CAPACITY must be >= 0.")
        return
    ok = check_stock(stock, capacity)
    if ok:
        print("OK: stock fits in capacity", capacity)
    else:
        print("KO: stock exceeds capacity", capacity)
```

```python
def handle_help():
    print("Available commands:")
    print("  ADD <OBJ> <QTY>   - add quantity of an object")
    print("  TAKE <OBJ> <QTY>  - remove quantity of an object")
    print("  SHOW              - show current stock")
    print("  CHECK <CAPACITY>  - check if stock fits in capacity")
    print("  HELP              - show this help")
    print("  QUIT              - exit the program")
```

### 3. Main loop

```python
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
```

