# Type Integrity: Handling Errors, Checking, and Conversion

In dynamic languages like Python, "Type Safety" is the developer's responsibility. If you fail to manage types, your Data Science pipeline will crash mid-way through a 10-hour processing job.

## 1. (`Type Error`): The Production Killer
A `TypeError` occurs when an operation is applied to an object of an inappropriate type.
* **Pro Insight**: Never just "fix" a TypeError. Trace back to *why* the wrong type reached that function. It usually points to a failure in your data ingestion layer.

## 2. Professional Type Checking
We use **Runtime Verification**. Don't guess; verify.

### The `type()` vs `isinstance()` Debate
* **Junior**: Uses `type(x) == int`.
* **Senior**: Uses `isinstance(x, int)`. 
**Why?** `isinstance()` supports inheritance (checking if an object is a subclass), which is critical for scalable Object-Oriented Programming.

```python
# Professional Validation Pattern
def calculate_growth(value: float):
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected numeric input, got {type(value).__name__}")
    return value * 1.05
```

## 3. Type Conversion (Casting) with Safety
Converting data (e.g., String from an API to a Float for a Model) is dangerous.

### Implicit vs Explicit
Python does some "Coercion" (e.g., int + float = float), but you should always be explicit.
```python
# Safe Casting
try:
    user_input = float(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a number.")
```

## 4. Static Type Analysis
We use tools like mypy or pyre (Facebook's tool) to check types before the code ever runs.

Rule: Always use Type Hints for function signatures. It serves as live documentation.
```python
# Example with mypy
def add_numbers(a: int, b: int) -> int:
    return a + b
```

## 5. Summary for the "Pro"
Prefer isinstance(): It's more robust and handles complex class hierarchies.

Defensive Conversion: Always wrap int() or float() conversions in try-except blocks when dealing with external data.

Type Hinting: It’s not optional in professional teams. It’s the difference between readable code and a "black box."
