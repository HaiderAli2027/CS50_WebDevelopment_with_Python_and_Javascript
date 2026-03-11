# 🐍 Python

---

## 📦 Data Structures

| Structure | Definition                     | Mutable | Ordered   | Duplicates |
| --------- | ------------------------------ | ------- | --------- | ---------- |
| `list`    | Sequential collection of items | ✅      | ✅        | ✅         |
| `tuple`   | Sequential collection of items | ❌      | ✅        | ✅         |
| `set`     | Collection of unique items     | ✅      | ❌        | ❌         |
| `dict`    | Collection of key-value pairs  | ✅      | ✅ (3.7+) | Keys: ❌   |

```python
my_list  = [1, 2, 3]        # mutable sequence
my_tuple = (1, 2, 3)        # immutable sequence
my_set   = {1, 2, 3}        # unique values only
my_dict  = {"key": "value"} # key-value pairs
```

---

## 🏗️ Object-Oriented Programming (OOP)

### 1. Class

> A **blueprint** that defines the attributes and behaviors shared by all objects of that type.

```python
class Car:
    brand = "Toyota"
```

### 2. Object

> An **instance** of a class — the actual entity created from the blueprint.

```python
car1 = Car()
print(car1.brand)  # Toyota
```

### 3. Constructor (`__init__`)

> A **special method** automatically invoked on object creation, used to initialize instance attributes. `self` refers to the current object.

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

car1 = Car("Toyota")
```

### 4. Encapsulation

> **Bundling data and methods** inside a class while restricting direct access to internal state using access modifiers (`_protected`, `__private`).

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private — cannot be accessed directly outside
```

**Interview tip:** Encapsulation protects data integrity. Python uses name mangling (`__attr` → `_ClassName__attr`) rather than hard enforcement.

### 5. Inheritance

> A child class **acquires properties and methods** of a parent class, enabling code reuse and hierarchical modeling.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    pass

Dog().speak()  # Animal speaks
```

### 6. Polymorphism

> The ability for **different classes to share the same method name** but implement it differently — "one interface, many forms."

```python
class Dog:
    def sound(self): print("Bark")

class Cat:
    def sound(self): print("Meow")

for animal in [Dog(), Cat()]:
    animal.sound()  # Each behaves differently
```

### 7. Abstraction

> **Hiding implementation details** and exposing only the essential interface. Enforced in Python using `ABC` (Abstract Base Class).

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass  # Subclasses MUST implement this
```

**Interview tip:** Abstraction defines _what_ to do; implementation defines _how_ to do it.

### 8. Method vs `__init__` vs `self`

| Term       | Description                                                             |
| ---------- | ----------------------------------------------------------------------- |
| **Method** | A function defined inside a class that describes object behavior        |
| `__init__` | Special constructor method; auto-called when an object is created       |
| `self`     | Refers to the current instance of the class; always the first parameter |

---

## 🎨 Decorators

> A **decorator** is a function that wraps another function to extend or modify its behavior — without altering the original function's code.

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def greet(name):
    print(f"Hello, {name}")

greet("Haider")
# Output:
# Calling greet
# Hello, Haider
```

**Common use cases:**

- Logging
- Authentication & access control
- Caching / memoization
- Timing / performance monitoring

---

## ⚙️ Functional Programming (FP)

> A paradigm that treats computation as **evaluation of pure functions** — avoiding shared state and side effects.

| Utility    | Purpose                                       | Example                            |
| ---------- | --------------------------------------------- | ---------------------------------- |
| `map()`    | Apply a function to every item in an iterable | `map(str, [1, 2, 3])`              |
| `filter()` | Keep items that satisfy a condition           | `filter(lambda x: x > 0, nums)`    |
| `reduce()` | Aggregate items into a single value           | `reduce(lambda a, b: a + b, nums)` |

```python
from functools import reduce

nums = [1, 2, 3, 4, 5]

doubled  = list(map(lambda x: x * 2, nums))       # [2, 4, 6, 8, 10]
evens    = list(filter(lambda x: x % 2 == 0, nums)) # [2, 4]
total    = reduce(lambda a, b: a + b, nums)         # 15
```

### Lambda Functions

> An **anonymous, single-expression function** — ideal for short, throwaway logic.

```python
square = lambda x: x ** 2
print(square(5))  # 25
```

**Interview tip:** Lambdas are syntactic sugar; prefer named functions for anything complex or reused.

---

## 🚨 Exception Handling (`try / except`)

> A mechanism to **gracefully handle runtime errors** without crashing the program.

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError) as e:
    print(f"Type or Value error: {e}")
else:
    print("No errors occurred")   # runs if no exception
finally:
    print("Always runs")          # cleanup — always executes
```

| Block     | When It Runs                                                  |
| --------- | ------------------------------------------------------------- |
| `try`     | Code that might raise an exception                            |
| `except`  | If a specific exception occurs                                |
| `else`    | If **no** exception occurred                                  |
| `finally` | **Always** — used for cleanup (closing files, DB connections) |

**Custom Exception:**

```python
class InsufficientFundsError(Exception):
    pass

raise InsufficientFundsError("Balance too low")
```

---

## 🧠 Quick Recall — Interview One-Liners

| Concept               | One-liner                                        |
| --------------------- | ------------------------------------------------ |
| **List**              | Mutable, ordered sequence                        |
| **Tuple**             | Immutable, ordered sequence — use for fixed data |
| **Set**               | Unordered, unique values — O(1) lookup           |
| **Dict**              | Key-value store — O(1) average access            |
| **Class**             | Blueprint for objects                            |
| **Encapsulation**     | Data hiding inside a class                       |
| **Inheritance**       | Child reuses parent's code                       |
| **Polymorphism**      | Same method, different behavior                  |
| **Abstraction**       | Expose interface, hide implementation            |
| **Decorator**         | Wraps a function to add behavior                 |
| **Lambda**            | Anonymous one-line function                      |
| **map/filter/reduce** | FP tools for transforming iterables              |
| **try/except**        | Handle runtime errors gracefully                 |

---
