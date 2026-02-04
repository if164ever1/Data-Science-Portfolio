 # Linear Mapping (Linear Transformation)

## What is it?

A **linear mapping** (or linear transformation) is like a **"machine"** that takes vectors as input and outputs other vectors, following two simple rules:

| Rule | Meaning |
|------|---------|
| **Additivity** | T(u + v) = T(u) + T(v) |
| **Homogeneity** | T(c·v) = c·T(v) |

> In plain words: *"Don't cheat — scaling before or after the machine gives the same result"*

---

## Simple Example

Imagine you have a photo and you:
- **Rotate** it by 90°
- **Stretch** it 2× horizontally
- **Flip** it vertically

These are all **linear transformations**! They keep straight lines straight and the origin stays fixed.

```
Before:        After (stretch 2× horizontally):
    ●───●           ●───────●
    │   │           │       │
    ●───●           ●───────●
```

---

## Why Data Scientists Care

| Use Case | What Linear Mapping Does |
|----------|------------------------|
| **PCA** | Finds best directions to compress data |
| **Neural Networks** | Each layer = linear + non-linear combo |
| **Feature Engineering** | Projects data to better space |
| **Image Processing** | Resizing, rotating, filtering |

---

## The Core Formula

Every linear mapping in finite space can be written as **matrix multiplication**:

$$\mathbf{y} = A\mathbf{x}$$

Where:
- **x** = input vector (n×1)
- **A** = transformation matrix (m×n)  
- **y** = output vector (m×1)

---

## Visual: 2D Transformation

```python
import numpy as np
import matplotlib.pyplot as plt

# Original square
square = np.array([[0,1,1,0,0], [0,0,1,1,0]])

# Stretch matrix: 2x horizontal, 0.5x vertical
A = np.array([[2, 0],
              [0, 0.5]])

# Apply transformation
transformed = A @ square

# Plot both
fig, axes = plt.subplots(1, 2, figsize=(10,5))
axes[0].plot(square[0], square[1], 'b-o'); axes[0].set_title("Original")
axes[1].plot(transformed[0], transformed[1], 'r-o'); axes[1].set_title("Stretched")
```

**Output:**

```
Original (1×1 square)     →     Stretched (2×0.5 rectangle)
    ┌───┐                        ┌───────┐
    │   │                        │       │
    └───┘                        └───────┘
```

---

## Key Properties to Remember

| Property | Check |
|----------|-------|
| T(**0**) = **0** | Always true (origin stays put) |
| Parallel lines stay parallel | No bending or curving |
| Can be reversed? | Yes, if **det(A) ≠ 0** |

---

## Quick Check: Is it Linear?

| Operation | Linear? | Why |
|-----------|---------|-----|
| Scaling | ✅ Yes | T(c·v) = c·T(v) |
| Rotation | ✅ Yes | Lines stay straight |
| Translation (shift) | ❌ No | Moves origin! |
| Adding constant | ❌ No | T(0) ≠ 0 |

---

## In Neural Networks

```
Input → [Linear: W·x + b] → [ReLU] → [Linear] → [Sigmoid] → Output
        ↑_______________↑
             This part is linear mapping
```

The **W·x** is your linear transformation. The **+ b** (bias) makes it *affine*, not strictly linear — but we still call the layer "linear" in DL context.