### Basics of Machine Learning (ML)

#### 1. **Steps in Machine Learning**:

---

**1.1 Problem Definition**

-   Clearly define the task to solve (e.g., predict house prices or classify emails as spam).
-   Identify whether it's a **supervised task** (with labeled data) or **unsupervised task** (without labels).

---

**1.2 Data Collection**

-   Gather data from various sources (databases, APIs, web scraping).
-   Ensure the data is sufficient in quantity and quality for the task.

---

**1.3 Data Preparation**

-   **Cleaning**: Handle missing values, remove duplicates, and fix incorrect data.
-   **Feature Engineering**: Create and transform features to make the data more meaningful for models.
-   **Splitting Datasets**: Divide data into:
    -   **Training set**: Used to train the model (e.g., 80% of data).
    -   **Test set**: Used to evaluate the model's performance (e.g., 20% of data).

---

**1.4 Model Selection and Training**

-   Choose a suitable algorithm (e.g., linear regression, decision tree).
-   Train the model by fitting it to the training data.

---

**1.5 Model Evaluation**

-   Assess the model using the test data and metrics like accuracy, MSE, or R² score.

---

**1.6 Model Tuning and Deployment**

-   **Tuning**: Optimize hyperparameters (e.g., learning rate, tree depth).
-   **Deployment**: Use the model in real-world applications (e.g., in a web app).

---

#### 2. **Classification vs. Regression**:

---

| **Aspect**     | **Classification**                       | **Regression**                         |
| -------------- | ---------------------------------------- | -------------------------------------- |
| **Definition** | Predicts discrete labels or categories.  | Predicts continuous numeric values.    |
| **Examples**   | Email spam detection, image recognition. | Predicting house prices, stock prices. |
| **Algorithms** | Logistic Regression, Decision Trees.     | Linear Regression, Ridge Regression.   |
| **Metrics**    | Accuracy, Precision, Recall, F1 Score.   | MSE, RMSE, R² Score.                   |

---

#### 3. **Evaluation Metrics**:

**For Regression**:

-   **Mean Squared Error (MSE)**: Measures average squared error between true and predicted values.  
    Formula:  
    \( \text{MSE} = \frac{1}{n} \sum*{i=1}^n (y*{\text{true}} - y\_{\text{pred}})^2 \)  
    Lower MSE = better model.

-   **R² Score**: Measures how well the model explains the variance in the data.  
    \( R^2 = 1 - \frac{\text{SSR}}{\text{SST}} \), where SSR = residual sum of squares, SST = total sum of squares.  
    R² closer to 1 = better model.

---

**For Classification**:

-   **Accuracy**: Percentage of correct predictions.  
    Formula:  
    \( \text{Accuracy} = \frac{\text{Correct Predictions}}{\text{Total Predictions}} \).

---

#### 4. **Purpose of Splitting Data (train_test_split)**:

-   Splitting ensures the model is trained on one set of data and evaluated on unseen data (test set), reducing the risk of overfitting (i.e., the model performs well on training data but poorly on new data).
-   Python Example:
    ```python
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    ```

---

#### 5. **Cross-Validation**:

-   Splits the data into **k-folds** (e.g., 5 folds).
-   The model is trained and evaluated on different folds iteratively.
-   Provides a more robust performance estimate by using the entire dataset for training and validation.
