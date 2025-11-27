# 🎒 Sorting Warehouse Quest

### *A fun algorithm adventure for mastering Python before the exam*

Welcome, engineer, your first day in the **Sorting Warehouse** has just begun.
The place is a mess: mislabeled boxes, broken stock lists, confused robots…
And guess who’s been hired to fix it?

**You.**

Don’t panic, this quest is built step-by-step, from easy warmups to exam-level mastery.
Each exercise is small, focused, and pushes your skills just a tiny bit further.

If you follow the order and use the tools provided, you’ll be ready for the final **without fear**.

---

# 🚀 What you will learn

By the end of this quest, you will be able to:

* manipulate strings and lists *manually*, without shortcuts
* build your own tools: `index_of_min`, `swap`, and others
* understand **selection sort** so deeply you could implement it blindfolded
* manage a sorted warehouse stock (very similar to the exam)
* even control a tiny warehouse robot in the bonus exercise

Everything uses **only simple Python**, loops, indices, `append`, no magic tricks.

---

# 🧭 Your mission roadmap

Each file represents a “chapter” of the quest.
Complete them **in order**, each chapter unlocks the next.

> **Do not modify the `main()` function in each file !**

## **1. `ex01_login_id.py`, Enter the warehouse**

Warm up:

* use your login (`firstname.lastname`)
* build a list of characters (no shortcuts)
* find the dot `.`
  You get used to loops, indices, and basic list building.

## **2. `ex02_login_boxes.py`, Forge your box labels**

Your login becomes warehouse **box labels**:

* uppercase conversion using `ord`/`chr`
* ignore `.`
* split into two halves around the dot

## **3. `ex03_min_and_swap.py`, Learn the warehouse tools**

You build:

* `index_of_min(L, start)`
* `swap(L, i, j)`
  These tools are *essential* for sorting (and the exam).

## **4. `ex04_selection_sort_step.py`, Train the sorting robot**

One move of selection sort:

* find the smallest in the unsorted part
* swap it into position

## **5. `ex05_selection_sort_full.py`, Become the Sorting Master**

Use your previous work to sort the whole list.
This is the moment your brain “clicks” on the algorithm.

## **6. `ex06_warehouse_stock.py`, Manage the warehouse (exam-style)**

You build a **stock list**:

* group objects
* count quantities
* simulate shop requests
* check capacities

This resembles the **final exam question**, but slightly harder because you manage the sorting yourself.

## **7. `ex07_warehouse_robot.py` (bonus), Command your own robot**

Optional, but very fun:

```
ADD A 2
TAKE B 1
SHOW
CHECK 20
```

A small interactive console using your own algorithms.

---

# 🔧 Python rules (IMPORTANT – same rules as final exam)

To train your algorithmic thinking, you must use **only basic Python**:

### ✔ Allowed

* `for` / `while`
* `if / elif / else`
* integers, booleans
* list indexing (`L[i]`)
* `len`, `range`
* `append`, `pop()` *(no arguments)*
* `print` (for debugging)

### ❌ Forbidden (these will break your training)

* slicing → `L[1:]`, `s[:-1]`
* list comprehensions → `[x for x in L]`
* `in` on lists → `if x in L`
* shortcuts → `min`, `max`, `sum`, `sorted`, `.sort()`
* any trick not seen in class

We give you tools to **detect forbidden patterns automatically**.

---

# 🕹 Essential tools for your journey

## **1. Run all tests**

```bash
python3 run_progress.py
```

Shows progress bars, explanations, and even a **trophy** if you complete everything.

## **2. Run tests for one exercise**

```bash
./run_exercise.sh 3
```

or

```bash
./run_exercise.sh ex03
```

Perfect when you're focused on one part.

## **3. Need help? Ask for hints**

```bash
python3 show_hint.py 2
```

Hints are gentle nudges, not answers.
Use them *after trying for real*.

## **4. Visualize your sorting algorithm**

```bash
python3 visual_selection_sort.py
```

This lets you “see” selection sort’s progress with cute ASCII bars.

## **5. Check if you broke the rules**

```bash
python3 check_rules.py
```

This script checks that you didn’t accidentally use:

* slicing
* comprehensions
* shortcuts (`min`, `sorted`, etc.)
  It **ignores comments and docstrings**, so examples are allowed.

---

# 🕒 Recommended strategy (2-hour support session)

To get the most out of your session:

### **Step 1, Warm up (~15 min)**

Finish ex01 and ex02
(These build your foundation.)

### **Step 2, Core tools (~20 min)**

Implement `index_of_min` and `swap` (ex03)
(Try them with `run_exercise.sh 3`)

### **Step 3, Understand sorting (~25 min)**

Do ex04 + ex05
(You’ll feel the algorithm suddenly make sense.)

### **Step 4, Exam prep (~40 min)**

Start ex06, even partial progress helps A LOT for the exam.

### **Step 5, Bonus fun (optional)**

Try ex07 when everything else is working.

Run tests regularly:

```bash
python3 run_progress.py
```

---

# 🎉 Final words

You don’t need to finish everything perfectly.
You just need to **improve**, step by step.

Treat this like a small adventure,
every exercise is a room in the warehouse,
and every function you write is a new tool in your toolbox.

You’ve got this.
Let’s sort this warehouse together. 💪📦🤖
