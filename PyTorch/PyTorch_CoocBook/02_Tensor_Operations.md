# Tensor Operations & Shape Manipulation

## Overview
Understanding how to manipulate tensor shapes is the most critical skill in Deep Learning. A neural network is essentially a pipeline of shape transformations. If you understand `view`, `reshape`, and `permute`, you can debug 90% of model errors.

## 1. Aggregation (Stats & Selection)

When a model outputs a prediction, it usually outputs a probability distribution. We use `argmax` to find the "winner."

```python
import torch

# Simulate a model prediction for 3 classes (Cat, Dog, Bird)
# Shape: [1 batch, 3 classes]
preds = torch.tensor([[0.1, 0.8, 0.1]])

# 1. Get the maximum value
max_val = preds.max() 
print(f"Confidence: {max_val.item()}") # 0.8

# 2. Get the INDEX of the maximum value (The Class ID)
# This is crucial for calculating accuracy.
pred_class_index = preds.argmax() 
print(f"Predicted Class Index: {pred_class_index}") # 1 (Dog)
```
## 2. Reshaping: View vs. Reshape
Changing the dimensions of a tensor without changing the data.

### view(): Fast. Returns a new view of the same memory. Requires data to be contiguous (stored sequentially).

```python
# Example: Flatten a 2D image (3 channels, 4x4)
image = torch.randn(3, 4, 4)
print(image.shape)  # torch.Size([3, 4, 4])

# View: Reshape without copying data (requires contiguous memory)
flattened = image.view(3, -1)  # -1 infers the size (16)
print(flattened.shape)  # torch.Size([3, 16])
```

### reshape(): Safer. Returns a view if possible, copies data if necessary.
```python
# Example: Permute dimensions (3, 4, 4) -> (4, 4, 3)
image = torch.randn(3, 4, 4)
print(image.shape)  # torch.Size([3, 4, 4])

# Reshape: Permute dimensions without changing data
permuted = image.reshape(4, 4, 3)
print(permuted.shape)  # torch.Size([4, 4, 3])
```
## 3. Permute (Swapping Dimensions)
PyTorch models expect images in format (Channels, Height, Width) (CHW). Most image files (JPG/PNG) load as (Height, Width, Channels) (HWC).

We use permute to swap these axes.
```python
# Example: Permute dimensions (3, 4, 4) -> (4, 4, 3)
image = torch.randn(3, 4, 4)
print(image.shape)  # torch.Size([3, 4, 4])

# Permute: Swap axes 0 and 2 (Height and Width)
permuted = image.permute(0, 2, 1)
print(permuted.shape)  # torch.Size([3, 4, 4])
```

## 4. In-Place Operations (The Danger Zone)
Any method ending with an underscore _ changes the tensor in memory.

x.add(y) -> Returns a new tensor. (Safe for gradients).

x.add_(y) -> Overwrites x. (Saves memory, but breaks gradients).
```python
x = torch.tensor([10.0])

# Safe
y = x.log2() 
print(x) # Still 10.0

# In-Place (Destructive)
# Only use this during data loading/preprocessing, rarely during training.
x.log2_() 
print(x) # Now 3.32...
```