## Eigenvalues and Eigenvectors

### 1. What are they? (The Simple Idea)

Imagine you have a square matrix  (which represents a transformation, like stretching or rotating data).

Most vectors will change their direction when you multiply them by $A$. However, there are special vectors that **do not change their direction**. They only get longer or shorter (scaled).

* **Eigenvector:** The vector that keeps its original direction after the transformation.
* **Eigenvalue:** The number (scalar) that tells us how much the eigenvector was stretched or squashed.

### 2. The Mathematical Formula

For a square matrix $A$, a non-zero vector  is an **eigenvector** if:
                                $$A\mathbf{v} = \lambda\mathbf{v}$$
Where:

*  $A$ is the matrix.
*  $\mathbf{v}$ is the **eigenvector**.
*  $\lambda$  (lambda) is the **eigenvalue**.

To find these values, we solve the **characteristic equation**:
                                $$\det(A - \lambda I) = 0$$

(Here, $I$ is the identity matrix and $\det$ is the determinant).

---

### 3. Why Data Scientists need this?

#### Principal Component Analysis (PCA)

In Data Science, we often have too many columns (features). PCA uses eigenvectors to find the "directions" where the data varies the most.

* The **eigenvector** with the highest **eigenvalue** is the most important direction in your data.
* By keeping only these directions, we can reduce 100 features down to 3 without losing much information.

#### Google PageRank

The algorithm that made Google famous uses eigenvectors to determine the importance of a website. A website is important if it is linked to by other important websites.

#### Image Compression

Eigenvalues help identify which parts of an image are essential and which parts can be removed to save space.

---

### 4. Simple Python Implementation

You can easily find these using the `numpy` library:

```python
import numpy as np

# Define a 2x2 matrix
A = np.array([[4, 2],
              [1, 3]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

```

---

### Key Vocabulary to Remember

* **Scalar:** A simple number (unlike a vector which has direction).
* **Transformation:** A process that changes a vector (like scaling or rotating).
* **Dimensionality Reduction:** The process of reducing the number of variables in a dataset.
* **Identity Matrix ():** A special square matrix with 1s on the diagonal and 0s elsewhere.

---

> **Task:** Take a 2x2 matrix  and calculate the eigenvalues manually using , then verify it using the Python code above.

Would you like me to show you the step-by-step math for solving that specific 2x2 matrix problem so you can add the solution to your repository?