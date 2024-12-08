import matplotlib.pyplot as plt

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