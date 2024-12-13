
### **Test Questions**

#### **Exercise 1: Pandas Data Manipulation**
You are given a dataset `students.csv` with the following columns:  
`[StudentID, Name, Age, Gender, Grade, Attendance]`.

1. Load the dataset into a Pandas DataFrame.
2. Filter the dataset to include only students whose `Grade` is greater than or equal to 70 and who have `Attendance` greater than 85%.
3. Add a new column `Performance`:
   - Set it to "Excellent" if `Grade` is above 85, otherwise "Good."
4. Rename the `Grade` column to `FinalGrade`.

---

#### **Exercise 2: Descriptive Statistics**
Given the following dataset:

| Age  | Grade | StudyHours |
|------|-------|------------|
| 20   | 85    | 10         |
| 21   | 90    | 12         |
| 19   | 78    | 8          |
| 22   | 92    | 15         |
| 20   | 88    | 9          |

1. Calculate the mean, median, and standard deviation for the `Grade` column.
2. Determine the interquartile range (IQR) for the `StudyHours` column.
3. Calculate the correlation between `Grade` and `StudyHours`.

---

#### **Exercise 3: Basics of Machine Learning**
You are working on a dataset to predict student performance based on `StudyHours` and `Attendance`.  

1. Split the dataset into training (80%) and testing (20%) sets.  
2. Train a simple linear regression model using `StudyHours` as the independent variable and `Grade` as the dependent variable.  
3. Calculate the Mean Squared Error (MSE) of the model on the test set.

---

### **Solutions**

#### **Exercise 1: Pandas Data Manipulation**

```python
import pandas as pd

# 1. Load the dataset
df = pd.read_csv("students.csv")

# 2. Filter students with Grade >= 70 and Attendance > 85
filtered_df = df[(df['Grade'] >= 70) & (df['Attendance'] > 85)]

# 3. Add a new column 'Performance'
filtered_df['Performance'] = filtered_df['Grade'].apply(lambda x: "Excellent" if x > 85 else "Good")

# 4. Rename the column 'Grade' to 'FinalGrade'
filtered_df = filtered_df.rename(columns={"Grade": "FinalGrade"})

print(filtered_df)
```

---

#### **Exercise 2: Descriptive Statistics**

```python
import numpy as np
import pandas as pd

data = {
    "Age": [20, 21, 19, 22, 20],
    "Grade": [85, 90, 78, 92, 88],
    "StudyHours": [10, 12, 8, 15, 9]
}
df = pd.DataFrame(data)

# 1. Calculate mean, median, and standard deviation for 'Grade'
mean_grade = df['Grade'].mean()
median_grade = df['Grade'].median()
std_dev_grade = df['Grade'].std()

# 2. Determine the interquartile range (IQR) for 'StudyHours'
q1 = df['StudyHours'].quantile(0.25)
q3 = df['StudyHours'].quantile(0.75)
iqr = q3 - q1

# 3. Calculate the correlation between 'Grade' and 'StudyHours'
correlation = df['Grade'].corr(df['StudyHours'])

print(f"Mean Grade: {mean_grade}")
print(f"Median Grade: {median_grade}")
print(f"Standard Deviation Grade: {std_dev_grade}")
print(f"IQR StudyHours: {iqr}")
print(f"Correlation (Grade vs StudyHours): {correlation}")
```

---

#### **Exercise 3: Basics of Machine Learning**

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Sample dataset
data = {
    "StudyHours": [10, 12, 8, 15, 9],
    "Attendance": [90, 92, 85, 95, 88],
    "Grade": [85, 90, 78, 92, 88]
}
df = pd.DataFrame(data)

# 1. Split the dataset
X = df[['StudyHours']]
y = df['Grade']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 3. Calculate the MSE
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
```
