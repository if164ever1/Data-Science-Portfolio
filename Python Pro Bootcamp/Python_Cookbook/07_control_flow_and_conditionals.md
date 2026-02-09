# Control Flow: The "Flat" Logic Architecture

In professional Python, deep nesting (an `if` inside an `if` inside an `if`) is considered technical debt. We strive for "Flat" logic.

## 1. The Guard Clause Pattern (The "Return Early" Rule)
Instead of wrapping your core logic inside a giant `if` block, check for failure cases first and return immediately. This reduces indentation levels.

**Junior Pattern (Nested/Hard to Read):**
```python
def process_order(order):
    if order.is_valid:
        if order.has_stock:
            if order.payment_success:
                ship_item()
            else:
                return "Payment Failed"
        else:
            return "No Stock"
    else:
        return "Invalid Order"
```
### Senior Pattern (Flat/Clean):
```python
def process_order(order):
    if not order.is_valid:
        return "Invalid Order"
    if not order.has_stock:
        return "No Stock"
    if not order.payment_success:
        return "Payment Failed"
    
    # Core logic stays at the root indentation level
    ship_item()
    return "Order Processed Successfully"
```

## 2. Truthiness (Pythonic Checks)
Python objects have implicit boolean values. Don't write redundant checks.

Falsy values: None, False, 0, 0.0, "" (empty string), [] (empty list), {} (empty dict).

Truthy values: Everything else.

```python
users = []

# Bad
if len(users) > 0:
    process(users)

# Pro (Implicit check)
if users:
    process(users)
```

## 3. The Ternary Operator (One-Line Conditionals)
Use this for simple value assignments, never for complex flow control. 
value_if_true if condition else value_if_false

```python
status = "Adult" if age >= 18 else "Minor"
```

## 4. Modern Control: match / case (Python 3.10+)
For Data Science and complex logic, if-elif-elif chains are obsolete. Use Structural Pattern Matching.
```python
# The modern way to handle API responses or data states
http_code = 404

match http_code:
    case 200:
        print("Success")
    case 400 | 404: # Logic OR
        print("Client Error")
    case 500:
        print("Server Error")
    case _: # Default case (Wildcard)
        print("Unknown Status")
```

## 5. Short-Circuit Evaluation
Python stops evaluating boolean expressions as soon as the result is known. We use this for "Default Value" logic.
```python
# If 'user_name' is None or Empty, it defaults to "Guest"
name = user_name or "Guest"
```

## 6. Summary for the "Pro"
Flatten your logic: Use Guard Clauses to exit functions early.

Use Implicit Truthiness: if my_list: is better than if len(my_list) > 0:.

Upgrade to match: If you have more than 3 elif blocks, refactor to a match statement.
