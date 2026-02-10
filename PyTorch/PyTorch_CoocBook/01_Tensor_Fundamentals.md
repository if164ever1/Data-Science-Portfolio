### Think of a Tensor not just as a "container for numbers," but as a view onto a block of memory.

### 1. The Three Pillars of a Tensor Every time you debug a tensor, you must check these three attributes. 99% of bugs happen because one of these is wrong:

- `tensor.shape`: The dimensions. (e.g., [64, 3, 224, 224] for a batch of images).

- `tensor.dtype`: The precision. Neural networks usually train in float32 or bfloat16. Indices (labels) are always int64 (Long).

- `tensor.device`: Where the data physically lives. You cannot add a CPU tensor to a GPU tensor. It will throw a RuntimeError.

### 2. Memory Layout (Stride) Tensors are stored as a 1D line of numbers in RAM. 
- `tensor.stride`: The steps to move to the next element in each dimension. (e.g., [224*224*3, 224*3, 3, 1] for a batch of images).
The "shape" is just a math trick (stride) telling the computer how many steps to skip to get to the next row. When you reshape a tensor, you aren't moving memory; you are just changing the math trick. This makes PyTorch incredibly fast.

### 3. The GPU Bottleneck The text mentions .to(). 
Moving data from CPU (RAM) to GPU (VRAM) is the slowest operation in Deep Learning. It is like driving a Ferrari (GPU) but stopping every 5 feet to check a map (CPU transfer). We optimize our code to move data to the GPU once and keep it there.

# PyTorch Fundamentals: Tensors

## Overview
In Deep Learning, the **Tensor** is the fundamental data structure. While conceptually similar to NumPy arrays, Tensors have two critical capabilities that make them suitable for AI:
1.  **Hardware Acceleration:** They can run on GPUs (CUDA) or TPUs/MPS for massive parallel computation.
2.  **Automatic Differentiation (Autograd):** They track the history of operations applied to them to calculate gradients for backpropagation.

## 1. Creating Tensors (The Professional Way)

We rarely create tensors manually from lists. We usually initialize them with specific constraints.

```python
import torch

# 1. Standard creation with explicit Data Type (CRITICAL)
# Always define dtype to avoid precision errors later.
# float32 is the standard for weights/biases.
x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)

# 2. Initialization for Model Weights
# Creating a matrix of shape (Rows, Columns)
weights = torch.randn((3, 5))  # Random numbers from a normal distribution
zeros   = torch.zeros((2, 2))  # Useful for bias initialization
ones    = torch.ones((2, 2))   # Useful for masking

print(f"Shape: {weights.shape}") # e.g., torch.Size([3, 5])
print(f"Type:  {weights.dtype}") # e.g., torch.float32
```

## 2. Indexing and Slicing
Avoid standard Python chaining x[0][0]. Use comma-separated indexing for performance and clarity.
```python
x = torch.tensor([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# INCORRECT / INEFFICIENT:
# val = x[0][1] 

# CORRECT (The PyTorch Way):
# Access row 0, column 1
val = x[0, 1] 

# Slicing: Get all rows, but only column 1
column_1 = x[:, 1] 

# Modification
x[0, 0] = 999  # In-place modification
```
## 3. Tensor Operations
PyTorch supports thousands of mathematical operations. They operate element-wise by default.
```python
a = torch.ones(2, 2)
b = torch.ones(2, 2) * 5

# Element-wise addition
result = a + b 

# Matrix Multiplication (The heart of Deep Learning)
# (2x2) @ (2x2)
matmul_result = torch.matmul(a, b)
```

## 4. Hardware Acceleration (Device Management)
Deep Learning models require GPUs for speed. You must explicitly move tensors to the correct device. Operations cannot occur between tensors on different devices.

Production Pattern: Do not hardcode "cuda". Write code that works on any machine (Linux Server, MacBook, or Laptop).
```python
# 1. Detect the best available hardware
device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
print(f"Using device: {device}")

# 2. Create tensor on CPU (default)
x = torch.tensor([10, 20])

# 3. Move to GPU (This moves data across the PCIe bus - expensive!)
x_gpu = x.to(device)

# 4. Move back to CPU (Required for printing with numpy or plotting)
x_cpu = x_gpu.cpu()

print(x_gpu.device)
```

## 5. Scalars
If a tensor has only one value (0-dimensions), use .item() to extract it as a standard Python number.
```python
x = torch.tensor(42.0)
print(x.item())  # Output: 42.0
```
