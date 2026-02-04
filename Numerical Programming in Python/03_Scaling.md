 # Scaling

## What is it?

**Scaling** is the simplest linear transformation — you just **stretch** or **squeeze** vectors along each axis. No rotation, no bending — just resizing.

```
Before scaling:        After scaling (2× x, 0.5× y):
    ●───●                  ●───────●
    │   │    ──→           │       │
    ●───●                  ●───────●
        ↑ stretched          ↑ squeezed
```

---

## Two Types of Scaling

### **Uniform Scaling** (Same factor in all directions)
$$S = s \cdot I = \begin{bmatrix} s & 0 \\ 0 & s \end{bmatrix}$$
Keeps the shape, just resizes uniformly.

### **Non-uniform Scaling** (Different factors per axis)
$$S = \begin{bmatrix} s_x & 0 \\ 0 & s_y \end{bmatrix}$$
Changes the shape by stretching different axes differently.

---

## The Formula

The scaling transformation applies a diagonal matrix to your vector:

$$\mathbf{y} = S \cdot \mathbf{x}$$

Where:
$$S = \begin{bmatrix} s_x & 0 \\ 0 & s_y \end{bmatrix}, \quad \mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$$

This gives:
$$\mathbf{y} = \begin{bmatrix} s_x \cdot x_1 \\ s_y \cdot x_2 \end{bmatrix}$$

**Key insight:** Each component gets multiplied independently — that's why the matrix is **diagonal**.

---

## Visual Examples

```
Uniform scaling (s = 2):     Non-uniform scaling (sx=2, sy=0.5):
    
    ┌───┐                      ┌───────┐
    │ ○ │    ──→               │   ●   │
    └───┘   stays square       └───────┘
                              becomes rectangle
    1×1  →  2×2                1×1  →  2×0.5
```

---

## Python Code for Your GitHub

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

def plot_scaling(ax, matrix, title, color='blue'):
    # Unit square
    square = np.array([
        [0, 1, 1, 0, 0],  # x coordinates
        [0, 0, 1, 1, 0]   # y coordinates
    ])
    
    # Apply scaling
    transformed = matrix @ square
    
    # Plot original (dashed)
    ax.plot(square[0], square[1], 'k--', alpha=0.5, label='Original')
    ax.fill(square[0], square[1], 'gray', alpha=0.2)
    
    # Plot transformed (solid)
    ax.plot(transformed[0], transformed[1], color=color, linewidth=2, label='Scaled')
    ax.fill(transformed[0], transformed[1], color=color, alpha=0.3)
    
    # Add arrows for basis vectors
    origin = np.array([0, 0])
    ax.annotate('', xy=matrix @ [1,0], xytext=origin,
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.annotate('', xy=matrix @ [0,1], xytext=origin,
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
    
    ax.set_xlim(-0.5, 3)
    ax.set_ylim(-0.5, 3)
    ax.set_aspect('equal')
    ax.set_title(title)
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)

# Create figure
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 1. Uniform scaling (enlarge)
S_uniform = np.array([[2, 0],
                      [0, 2]])
plot_scaling(axes[0], S_uniform, 'Uniform: 2× everywhere', 'blue')

# 2. Non-uniform: stretch X, squeeze Y
S_nonuniform = np.array([[2, 0],
                         [0, 0.5]])
plot_scaling(axes[1], S_nonuniform, 'Non-uniform: 2× X, 0.5× Y', 'orange')

# 3. Squeeze (shrink)
S_squeeze = np.array([[0.5, 0],
                      [0, 0.5]])
plot_scaling(axes[2], S_squeeze, 'Uniform: 0.5× (shrink)', 'green')

plt.tight_layout()
plt.savefig('scaling_transformations.png', dpi=150, bbox_inches='tight')
plt.show()
```

**Output:**

```
┌─────────────────┬─────────────────┬─────────────────┐
│   Uniform 2×    │  Stretch X      │   Shrink 0.5×   │
│                 │  Squeeze Y      │                 │
│  ┌───────┐      │  ┌───────────┐  │    ┌───┐        │
│  │       │      │  │     ●     │  │    │ ● │        │
│  │   ○   │      │  └───────────┘  │    └───┘        │
│  │       │      │                 │                 │
│  └───────┘      │                 │                 │
└─────────────────┴─────────────────┴─────────────────┘
```

---

## Why Data Scientists Need This

| Application | How Scaling Helps |
|-------------|-----------------|
| **Feature Normalization** | Scale all features to [0,1] or $\mu=0, \sigma=1$ for fair comparison |
| **Gradient Descent** | Prevents "elongated" loss landscapes, enables faster training |
| **Image Preprocessing** | Resize images to fixed input size for CNN models |
| **PCA / SVD** | Standardization needed before decomposition for accuracy |
| **Distance-based ML** | Prevents features with large values from dominating (KNN, K-means) |

---

## The Scaling Trap ⚠️

```
Bad:  Salary = $50,000      Age = 25
       ↓
       Model thinks salary is "more important" just because numbers are bigger!

Good:  Salary = 0.7          Age = 0.4   (both in [0,1] range)
       ↓
       Model compares fairly
```

---

## Key Formulas for Your Notes

| Concept | Formula |
|---------|---------|
| **2D Scaling Matrix** | $$S = \begin{bmatrix} s_x & 0 \\ 0 & s_y \end{bmatrix}$$ |
| **n-D Scaling Matrix** | $$S = \text{diag}(s_1, s_2, \ldots, s_n)$$ |
| **Determinant (Area Change)** | $$\det(S) = s_x \cdot s_y$$ |
| **Inverse (Undo Scaling)** | $$S^{-1} = \begin{bmatrix} \frac{1}{s_x} & 0 \\ 0 & \frac{1}{s_y} \end{bmatrix}$$ |

### Understanding the Determinant

The determinant tells you how the area/volume changes:

$$\det(S) = s_x \cdot s_y$$

- $\det(S) = 4$ → Area becomes **4× bigger**
- $\det(S) = 0.25$ → Area becomes **4× smaller**  
- $\det(S) = 0$ → Collapses to a line or point (⚠️ no inverse!)

---

## Mini Exercise (for your repo!)

```python
# Check: does scaling preserve straight lines?
import numpy as np

def is_linear(T, v1, v2, alpha):
    """Test: T(α·v1 + v2) == α·T(v1) + T(v2)"""
    left = T(alpha * v1 + v2)
    right = alpha * T(v1) + T(v2)
    return np.allclose(left, right)

# Scaling "machine"
S = np.array([[2, 0], [0, 3]])
T = lambda x: S @ x

# Random test
v1, v2 = np.random.rand(2), np.random.rand(2)
print(f"Scaling is linear: {is_linear(T, v1, v2, 2.5)}")
# Output: True ✓
```

---

Want **rotation** next? Or **feature scaling methods in sklearn** (StandardScaler, MinMaxScaler)?