

### **Complex Test Questions**

#### **Exercise 1: Advanced Pandas Data Manipulation**
You are given a dataset `sales.csv` with the following columns:  
`[OrderID, Product, Quantity, Price, OrderDate, CustomerID]`.

1. Load the dataset into a Pandas DataFrame.
2. Create a new column `TotalPrice` by multiplying `Quantity` and `Price`.
3. Extract the month from `OrderDate` and create a new column called `Month`.
4. Group the data by `Month` and calculate:
   - Total revenue (`TotalPrice`) for each month.
   - Average revenue per order for each month.
5. Find the top 3 customers by total spending.

---

#### **Exercise 2: Statistics with Outliers**
You are analyzing a dataset with the following columns:  
`[Temperature, Sales, Holiday]`.  

| Temperature | Sales | Holiday |
|-------------|-------|---------|
| 25          | 200   | No      |
| 30          | 250   | No      |
| 22          | 180   | No      |
| 40          | 1000  | Yes     |
| 20          | 160   | No      |
| 35          | 300   | No      |

1. Calculate the mean and median for `Sales`.  
2. Identify if there are any outliers in `Sales` using the IQR method.  
3. Calculate the correlation between `Temperature` and `Sales`, ignoring rows with `Holiday = Yes`.  

---

#### **Exercise 3: Machine Learning with Feature Engineering**
You are working with a dataset to predict housing prices. The dataset contains the following columns:  
`[Area, Bedrooms, Bathrooms, Age, Price]`.

1. Handle missing values in the `Bedrooms` column by filling them with the column mean.
2. Create a new feature `PricePerSqFt` by dividing `Price` by `Area`.
3. Split the data into training (80%) and testing (20%) sets.
4. Train a decision tree regressor to predict `Price` using all other columns as features.
5. Evaluate the model using the Mean Absolute Error (MAE) and R² score on the test set.

---

### **Solutions**

#### **Exercise 1: Advanced Pandas Data Manipulation**

```python
import pandas as pd

# 1. Load the dataset
df = pd.read_csv("sales.csv")

# 2. Create 'TotalPrice'
df['TotalPrice'] = df['Quantity'] * df['Price']

# 3. Extract 'Month' from 'OrderDate'
df['Month'] = pd.to_datetime(df['OrderDate']).dt.month

# 4. Group by 'Month' and calculate total and average revenue
monthly_revenue = df.groupby('Month')['TotalPrice'].sum()
avg_revenue_per_order = df.groupby('Month')['TotalPrice'].mean()

# 5. Find top 3 customers by total spending
top_customers = df.groupby('CustomerID')['TotalPrice'].sum().nlargest(3)

print("Monthly Revenue:\n", monthly_revenue)
print("Average Revenue Per Order:\n", avg_revenue_per_order)
print("Top 3 Customers:\n", top_customers)
```

---

#### **Exercise 2: Statistics with Outliers**

```python
import numpy as np
import pandas as pd

data = {
    "Temperature": [25, 30, 22, 40, 20, 35],
    "Sales": [200, 250, 180, 1000, 160, 300],
    "Holiday": ["No", "No", "No", "Yes", "No", "No"]
}
df = pd.DataFrame(data)

# 1. Calculate mean and median for 'Sales'
mean_sales = df['Sales'].mean()
median_sales = df['Sales'].median()

# 2. Identify outliers using IQR method
q1 = df['Sales'].quantile(0.25)
q3 = df['Sales'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = df[(df['Sales'] < lower_bound) | (df['Sales'] > upper_bound)]

# 3. Correlation between 'Temperature' and 'Sales' excluding holidays
filtered_df = df[df['Holiday'] == "No"]
correlation = filtered_df['Temperature'].corr(filtered_df['Sales'])

print(f"Mean Sales: {mean_sales}")
print(f"Median Sales: {median_sales}")
print(f"Outliers:\n{outliers}")
print(f"Correlation (Temperature vs Sales): {correlation}")
```

---

#### **Exercise 3: Machine Learning with Feature Engineering**

```python
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Sample dataset
data = {
    "Area": [1500, 2000, 2500, 1800, 2200],
    "Bedrooms": [3, None, 4, 2, 3],
    "Bathrooms": [2, 3, 3, 2, 4],
    "Age": [10, 15, 5, 8, 12],
    "Price": [300000, 400000, 500000, 350000, 450000]
}
df = pd.DataFrame(data)

# 1. Handle missing values in 'Bedrooms'
df['Bedrooms'].fillna(df['Bedrooms'].mean(), inplace=True)

# 2. Create 'PricePerSqFt'
df['PricePerSqFt'] = df['Price'] / df['Area']

# 3. Split the data
X = df.drop(columns=['Price'])
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train a decision tree regressor
model = DecisionTreeRegressor()
model.fit(X_train, y_train)

# 5. Evaluate the model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error: {mae}")
print(f"R² Score: {r2}")
```