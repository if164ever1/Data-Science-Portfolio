# Primitive Data Types: Precision and Memory

In Python, everything is an object, but "Primitives" (Integers, Floats, Strings, Booleans) are the building blocks. Choosing the wrong type leads to memory leaks or calculation errors.

## 1. Integers (`int`): Arbitrary Precision
Unlike C++ or Java, Python integers have **arbitrary precision**. This means they can be as large as your RAM allows.
* **Pro Use Case**: Great for cryptography and large-scale ID tracking.
* **Memory Note**: Because integers are objects, even a small number takes up about 28 bytes.

## 2. Floating-Point Numbers (`float`): The Binary Trap
Python floats are double-precision (64-bit). They are **approximations**, not exact values.
```python
# The Classic Interview Question
print(0.1 + 0.2 == 0.3) # Output: False
print(0.1 + 0.2)        # Output: 0.30000000000000004
```
Pro Tip: In Data Science/Finance, never compare floats using ==. Use math.isclose() or the decimal module for high-precision financial calculations.

## 3. (`Strings (str)`): The Immutable Sequence
### Strings are immutable sequences of Unicode characters.

The "Joining" Trap: Every time you modify a string, Python creates a new one.
```python
# Junior way (Slow/Heavy memory)
s = "Data" + " " + "Science"

# Senior way (Fast/Memory efficient)
parts = ["Data", "Science"]
s = " ".join(parts)
```

## 4. (`Booleans (bool)`): The Logic Gate
Booleans are actually a subclass of integers. True is 1, False is 0.

Pro Tip: You can actually sum booleans. sum([True, False, True]) equals 2. This is used in Data Science to quickly count how many rows meet a certain condition.
```python
# Counting Trues in a List
data = [True, False, True, True, False]
true_count = sum(data)
print(true_count) # Output: 3
```
## 5. Type Hinting (Professional Standard)
We always use Type Hints. It makes code readable and allows tools to catch bugs before the code runs.
```python
def add_numbers(a: int, b: int) -> int:
    return a + b
```
Pro Tip: Type Hints are not enforced by Python. They are just a way to document your code. Tools like mypy can check your code for type errors.

## 6. Summary for the "Pro"
Floats are lies: Use round() or math.isclose() for comparisons.

Strings are fixed: Use lists and .join() for heavy string manipulation.

Type Hints are mandatory: Always define what your data types are to prevent production crashes.
