## 1. Min-Max Scaling (Normalization)

This technique re-scales the data to a fixed range, usually **0 to 1**.

* **Formula:** 
* **Best use case:** Use this when you need your data to be bounded (e.g., in Image Processing where pixel intensity is 0-255) or when using algorithms like **Neural Networks** and **K-Nearest Neighbors (KNN)**.
* **Python Tool:** `sklearn.preprocessing.MinMaxScaler`

## 2. Standardization (Z-score Normalization)

This transforms the data so that it has a **mean of 0** and a **standard deviation of 1**.

* **Formula:** 
* **Best use case:** This is the most common method. It is preferred for algorithms that assume a Gaussian (Normal) distribution, such as **Logistic Regression**, **Linear Regression**, and **Support Vector Machines (SVM)**.
* **Python Tool:** `sklearn.preprocessing.StandardScaler`

## 3. Robust Scaling

Standardization can fail if your data has many **outliers** (extreme values). Robust Scaling uses the median and the Interquartile Range (IQR), making it "robust" to those outliers.

* **Best use case:** Use this when your dataset contains extreme values that you don't want to remove but don't want to ruin your scaling.
* **Python Tool:** `sklearn.preprocessing.RobustScaler`

---

### Summary Table for your Notes

| Feature | Min-Max Scaling | Standardization | Robust Scaling |
| --- | --- | --- | --- |
| **Range** | Strictly  or  | Not bounded | Not bounded |
| **Mean** | Varies | Always  | Varies (Median is ) |
| **Outliers** | Very sensitive | Sensitive | **Not sensitive** |

---

### Quick Python Example (Scikit-Learn)

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd

# Sample Data
data = {'Salary': [45000, 54000, 120000, 31000]}
df = pd.DataFrame(data)

# Apply Standardization
scaler = StandardScaler()
df['Salary_Standardized'] = scaler.fit_transform(df[['Salary']])

print(df)

```