
# **Mastering pandas: The Ultimate Guide**

### 1. **Introduction to pandas**

-   pandas is a Python library for data manipulation and analysis.
-   Two main data structures:
    -   `Series`: One-dimensional array with labels (like a column in a spreadsheet).
    -   `DataFrame`: Two-dimensional tabular data structure with rows and columns.

### 2. **Basic Operations**

```python
import pandas as pd

# Creating a Series
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print(s)

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)

# Reading & Writing Files
df = pd.read_csv('file.csv')            # CSV
df.to_csv('output.csv', index=False)    # Write CSV
df = pd.read_excel('file.xlsx')         # Excel
df.to_excel('output.xlsx', index=False) # Write Excel
```

---

### 3. **Data Inspection**

```python
# Quick Look
print(df.head())     # First 5 rows
print(df.tail())     # Last 5 rows
print(df.info())     # DataFrame info (types, non-null values)
print(df.describe()) # Summary stats (numeric columns)

# Shape & Index
print(df.shape)      # (rows, columns)
print(df.columns)    # Column names
print(df.index)      # Row index
```

---

### 4. **Selection & Indexing**

```python
# Selecting Columns
print(df['Name'])          # Single column (Series)
print(df[['Name', 'Age']]) # Multiple columns (DataFrame)

# Selecting Rows
print(df.loc[0])           # By index label
print(df.iloc[0])          # By position
print(df[0:2])             # Slicing rows

# Boolean Filtering
print(df[df['Age'] > 25])  # Rows where Age > 25
```

---

### 5. **Data Cleaning**

```python
# Handling Missing Data
df.fillna(0, inplace=True)       # Fill missing values with 0
df.dropna(inplace=True)          # Drop rows with missing values

# Renaming Columns
df.rename(columns={'Name': 'Full Name'}, inplace=True)

# Replacing Values
df['Age'].replace(30, 99, inplace=True)

# Duplicates
df.drop_duplicates(inplace=True) # Drop duplicate rows

# Changing Data Types
df['Age'] = df['Age'].astype('float') # Convert Age to float
```

---

### 6. **Data Manipulation**

```python
# Adding New Columns
df['Salary'] = [50000, 60000, 70000]  # New column with data

# Modifying Columns
df['Age'] = df['Age'] * 2            # Double the Age

# Dropping Columns/Rows
df.drop('Salary', axis=1, inplace=True)  # Drop column
df.drop([0, 1], axis=0, inplace=True)    # Drop rows

# Sorting
df.sort_values('Age', ascending=False, inplace=True)

# Grouping
grouped = df.groupby('Age').mean()  # Group by 'Age' and calculate mean
print(grouped)

# Aggregation
df['Age'].sum()   # Sum of Age column
df['Age'].mean()  # Mean of Age column
df['Age'].max()   # Maximum value
```

---

### 7. **Advanced Indexing**

```python
# Setting and Resetting Index
df.set_index('Name', inplace=True) # Set 'Name' as index
df.reset_index(inplace=True)       # Reset to default integer index

# MultiIndex (Hierarchical Indexing)
data = pd.DataFrame({
    'City': ['Paris', 'Paris', 'London', 'London'],
    'Year': [2020, 2021, 2020, 2021],
    'Population': [2.1, 2.2, 8.9, 9.0]
})
df = data.set_index(['City', 'Year'])
print(df)
```

---

### 8. **Merging, Joining, and Concatenation**

```python
# Merging (like SQL JOIN)
left = pd.DataFrame({'ID': [1, 2], 'Name': ['Alice', 'Bob']})
right = pd.DataFrame({'ID': [1, 2], 'Age': [25, 30]})
merged = pd.merge(left, right, on='ID', how='inner') # Merge on ID
print(merged)

# Concatenation
df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'A': [3, 4]})
concat = pd.concat([df1, df2], ignore_index=True) # Append rows
print(concat)

# Joining
left = left.set_index('ID')
right = right.set_index('ID')
joined = left.join(right) # Join on index
print(joined)
```

---

### 9. **Time Series**

```python
# Date Range
dates = pd.date_range('2023-01-01', periods=5)
df = pd.DataFrame({'Date': dates, 'Value': [10, 20, 30, 40, 50]})
print(df)

# Convert to Datetime
df['Date'] = pd.to_datetime(df['Date'])

# Filter by Date
print(df[df['Date'] > '2023-01-03'])

# Resampling
df.set_index('Date', inplace=True)
print(df.resample('D').sum()) # Resample daily and sum
```

---

### 10. **Visualization with pandas**

```python
import matplotlib.pyplot as plt

# Line Plot
df['Value'].plot()
plt.show()

# Bar Plot
df.plot(kind='bar', x='Date', y='Value')
plt.show()
```

---

### 11. **Performance Tips**

-   Use `df.iterrows()` or `df.itertuples()` only if necessary; vectorized operations are faster.
-   Use `dask` for large datasets that don't fit in memory.
-   Specify `dtype` when loading data for better memory efficiency.

---

### 12. **Pandas Tricks**

```python
# Applying Functions
df['Age'] = df['Age'].apply(lambda x: x * 2) # Apply function to column

# Conditional Column
df['Category'] = df['Age'].apply(lambda x: 'Adult' if x >= 18 else 'Child')

# Query API
print(df.query('Age > 20'))  # Filter rows where Age > 20

# Pivot Tables
pivot = df.pivot_table(values='Salary', index='Department', columns='Gender', aggfunc='mean')
print(pivot)
```

---

### 13. **Resources to Learn More**

-   **Official Documentation**: [pandas.pydata.org](https://pandas.pydata.org/)
-   **Books**: _Python for Data Analysis_ by Wes McKinney.
-   **Cheat Sheets**: Search for "pandas cheat sheet" (e.g., from DataCamp or Towards Data Science).

