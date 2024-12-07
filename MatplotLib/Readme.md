
# **Matplotlib Cheat Sheet**

### **1. Quick Overview**
- **Matplotlib** is a Python library for creating static, animated, and interactive visualizations.
- Core Object: `pyplot` (imported as `plt`).
- Figure -> Axes -> Plots (hierarchical structure).

---

### **2. Basic Plot Anatomy**
```python
import matplotlib.pyplot as plt

# Basic Plot
plt.plot([1, 2, 3], [4, 5, 6]) # x = [1, 2, 3], y = [4, 5, 6]
plt.title('Title')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True) # Add grid
plt.show()
```

---

### **3. Subplots for Multiple Graphs**
```python
# Multiple Plots in a Single Figure
fig, ax = plt.subplots(2, 2, figsize=(8, 6)) # 2x2 grid
ax[0, 0].plot([1, 2], [3, 4], color='blue') # Top-left
ax[1, 1].scatter([1, 2], [3, 4], color='red') # Bottom-right
plt.tight_layout() # Prevent overlap
plt.show()
```

---

### **4. Plot Types**
#### 1. **Line Plot**
```python
plt.plot([1, 2, 3], [4, 5, 6], linestyle='--', color='g', marker='o')
plt.show()
```

#### 2. **Scatter Plot**
```python
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.scatter(x, y, color='red', s=100, alpha=0.5) # s = marker size
plt.show()
```

#### 3. **Bar Plot**
```python
categories = ['A', 'B', 'C']
values = [10, 20, 15]
plt.bar(categories, values, color=['blue', 'orange', 'green'])
plt.show()
```

#### 4. **Histogram**
```python
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(data, bins=4, color='purple', edgecolor='black')
plt.show()
```

#### 5. **Pie Chart**
```python
labels = ['Python', 'Java', 'C++']
sizes = [50, 30, 20]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.show()
```

#### 6. **Box Plot**
```python
data = [7, 8, 9, 10, 10, 11, 12, 13]
plt.boxplot(data)
plt.show()
```

#### 7. **Heatmap (via `imshow`)**
```python
import numpy as np
data = np.random.rand(5, 5) # Random 5x5 matrix
plt.imshow(data, cmap='coolwarm', interpolation='nearest')
plt.colorbar() # Add color legend
plt.show()
```

---

### **5. Advanced Customizations**
#### 1. **Legends**
```python
plt.plot([1, 2, 3], label='Line 1')
plt.plot([3, 2, 1], label='Line 2')
plt.legend(loc='upper right') # or 'lower left'
plt.show()
```

#### 2. **Customizing Axes**
```python
plt.plot([1, 2, 3], [4, 5, 6])
plt.xlim(0, 4) # X-axis range
plt.ylim(3, 7) # Y-axis range
plt.xticks([1, 2, 3], ['One', 'Two', 'Three']) # Custom ticks
plt.show()
```

#### 3. **Annotations**
```python
plt.plot([1, 2, 3], [4, 5, 6])
plt.annotate('Important Point', xy=(2, 5), xytext=(2.5, 6),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.show()
```

#### 4. **Logarithmic Scales**
```python
plt.plot([1, 10, 100], [1, 2, 3])
plt.xscale('log') # Set X-axis to log scale
plt.yscale('log') # Set Y-axis to log scale
plt.show()
```

---

### **6. Working with Multiple Figures**
```python
# Multiple Figures
plt.figure(1) # First figure
plt.plot([1, 2, 3])
plt.figure(2) # Second figure
plt.plot([3, 2, 1])
plt.show()
```

---

### **7. Combining with pandas**
```python
import pandas as pd

# Example DataFrame
data = {'A': [10, 20, 30], 'B': [15, 25, 35]}
df = pd.DataFrame(data)

# Line Plot
df.plot(kind='line', title='Line Plot')

# Bar Plot
df.plot(kind='bar', title='Bar Plot')

# Box Plot
df.plot(kind='box', title='Box Plot')

plt.show()
```

---

### **8. Save Figures**
```python
plt.plot([1, 2, 3], [4, 5, 6])
plt.savefig('plot.png', dpi=300, bbox_inches='tight') # High-res save
plt.show()
```

---

### **9. Tips for Better Plots**
- Use `figsize=(width, height)` to control figure size.
- Always use `tight_layout()` to prevent overlaps.
- Use `sns.set()` if working with Seaborn for consistent aesthetics.
- Explore `cmap` (colormap) options for better visuals (`'viridis'`, `'plasma'`, etc.).

---

### **10. Recommended Libraries to Enhance**
- **Seaborn**: High-level API for prettier visualizations.
- **Plotly**: Interactive and dynamic visualizations.
- **Altair**: Declarative statistical visualization.

