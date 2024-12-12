
### 1. **Evaluation Metrics for Regression** (Linear Regression Example)

#### **Mean Squared Error (MSE)**:

**MSE** measures how far the predictions are from the actual values. It's the average of the squared differences between the predicted values and the actual values. MSE is used for **regression** problems where the target variable is continuous.

**Formula for MSE**:
\[
\text{MSE} = \frac{1}{n} \sum\_{i=1}^{n} (y_i - \hat{y}\_i)^2
\]
Where:

-   \(y_i\) = actual value
-   \(\hat{y}\_i\) = predicted value
-   \(n\) = number of data points

#### **R² Score** (Coefficient of Determination):

The **R² score** measures the proportion of the variance in the target variable that is explained by the model. R² ranges from 0 to 1:

-   **1**: Perfect fit (model explains all the variance).
-   **0**: The model explains none of the variance (it performs no better than the mean model).

**Formula for R²**:
\[
R^2 = 1 - \frac{\sum*{i=1}^{n} (y_i - \hat{y}\_i)^2}{\sum*{i=1}^{n} (y_i - \bar{y})^2}
\]
Where:

-   \(y_i\) = actual value
-   \(\hat{y}\_i\) = predicted value
-   \(\bar{y}\) = mean of actual values

---

### Example: **Linear Regression** Evaluation Using MSE and R²

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import load_boston
import pandas as pd

# Load the Boston housing dataset (regression problem)
boston = load_boston()
X = pd.DataFrame(boston.data, columns=boston.feature_names)
y = pd.Series(boston.target)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
linear_model = LinearRegression()

# Train the model
linear_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = linear_model.predict(X_test)

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)

# Calculate R² Score
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R² Score: {r2:.2f}")
```

### Output:

```
Mean Squared Error (MSE): 24.29
R² Score: 0.82
```

**Interpretation**:

-   **MSE**: The lower the MSE, the better the model. A value of 24.29 means the average squared error between predicted and actual housing prices is 24.29.
-   **R² Score**: The model explains **82%** of the variance in the housing prices.

---

### 2. **Evaluation Metrics for Classification** (Decision Tree Classifier Example)

#### **Accuracy**:

**Accuracy** is the most common evaluation metric for **classification** problems. It measures the percentage of correctly predicted instances out of all predictions made.

**Formula for Accuracy**:
\[
\text{Accuracy} = \frac{\text{Number of Correct Predictions}}{\text{Total Number of Predictions}} \times 100
\]

#### Example: **Decision Tree Classifier** Evaluation Using Accuracy

Let’s use the **Iris dataset** for a classification task with a **DecisionTreeClassifier**.

```python
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
import pandas as pd

# Load the Iris dataset (classification problem)
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Decision Tree Classifier model
dt_model = DecisionTreeClassifier(random_state=42)

# Train the model
dt_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = dt_model.predict(X_test)

# Calculate Accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy*100:.2f}%")
```

### Output:

```
Accuracy: 100.00%
```

**Interpretation**:

-   **Accuracy**: This means the model correctly classified **100%** of the test samples, which is ideal.

---

### Summary of Key Evaluation Metrics

1. **For Regression (Linear Regression)**:

    - **MSE**: Measures how much the predicted values deviate from the true values. Lower MSE means better model.
    - **R² Score**: Measures how well the model explains the variance in the data. Ranges from 0 to 1, where 1 is perfect.

2. **For Classification (Decision Tree Classifier)**:
    - **Accuracy**: Percentage of correct predictions made by the model. The higher the accuracy, the better the model.

