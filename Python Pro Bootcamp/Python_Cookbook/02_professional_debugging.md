# Professional Debugging: The Systemic Approach

In production, "guessing" is not a strategy. Debugging is the process of testing hypotheses about why your code's reality differs from your expectations.

## 1. The Traceback: Reading from Bottom to Top
When Python crashes, the most relevant information is at the **bottom**.
* **Exception Type**: (e.g., `TypeError`, `KeyError`) tells you *what* happened.
* **Error Message**: Tells you *why* it happened.
* **File Path & Line Number**: Tells you *where* it happened.

## 2. Advanced `print()` Debugging
If you aren't using a debugger yet, make your prints professional. Use identifiers to track variable states.
```python
# Bad: confusing output
print(data) 

# Pro: Descriptive, formatted debugging
print(f"DEBUG | UserID: {user_id} | Raw Data Type: {type(data)} | Value: {data}")
```

## 3. The assert Statement
### Use assertions to catch bugs early by defining what must be true. If the condition is False, the program stops immediately.
```python
def divide(a, b):
    assert b != 0, "Divisor cannot be zero"
    return a / b
```
## 4. Basic Error Handling: try-except
### A professional script doesn't just crash; it fails gracefully.
```python
try:
    with open("data.csv", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The configuration file is missing. Defaulting to empty state.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

## 5. The Pro Checklist (F.A.I.L.)
### Formulate a hypothesis: Why is this happening?
### Analyze the state: Use type(), len(), and dir() to inspect objects.
### Isolate: Comment out code until the error disappears to find the exact line.
### Log: Keep track of what you changed so you can revert if needed.
