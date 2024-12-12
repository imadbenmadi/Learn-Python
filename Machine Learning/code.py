# Import necessary libraries
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Data Collection: Load the Iris dataset
iris = datasets.load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Display the first few rows of the data
print("First 5 rows of the dataset:")
print(df.head())

# 2. Data Preparation: Split data into features (X) and target (y)
X = df.drop('target', axis=1)  # Features
y = df['target']              # Target variable

# 3. Train-test Split: Split the data into training and test sets (80% training, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Model Selection and Training: Use Decision Tree Classifier
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)  # Train the model

# 5. Model Evaluation: Evaluate the model with accuracy score and confusion matrix
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy of the model: {accuracy*100:.2f}%")

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 6. Cross-validation: Perform 5-fold cross-validation
cv_scores = cross_val_score(model, X, y, cv=5)
print(f"\nCross-validation scores (5-fold): {cv_scores}")
print(f"Mean cross-validation score: {cv_scores.mean():.2f}")

# 7. Model Tuning (optional): Hyperparameter tuning can be done here if needed.
# For simplicity, we won't do it here, but we can explore that using GridSearchCV.

# Example of calculating Mean Squared Error (MSE) for a regression task (Not used here, but just for demonstration):
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

# Create a regression dataset for demonstration
regression_data = datasets.load_boston()
X_reg = pd.DataFrame(regression_data.data, columns=regression_data.feature_names)
y_reg = regression_data.target

# Train-test split for regression
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

# Train a Linear Regression model
reg_model = LinearRegression()
reg_model.fit(X_train_reg, y_train_reg)

# Predict and calculate MSE
y_pred_reg = reg_model.predict(X_test_reg)
mse = mean_squared_error(y_test_reg, y_pred_reg)
print(f"\nMean Squared Error (MSE) for regression model: {mse:.2f}")

