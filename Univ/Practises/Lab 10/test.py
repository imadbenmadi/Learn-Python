import pandas as pd

# Data: Hours studied vs. exam score
data = {
    'Hours_Studied': [1, 2, 3, 4, 5],
    'Exam_Score': [50, 55, 60, 65, 70]
}
df = pd.DataFrame(data)

# Find the correlation
print(df.corr())
