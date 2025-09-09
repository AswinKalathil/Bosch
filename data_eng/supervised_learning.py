# supervised learning
# regression and classification
# regression predicts numerical values

import pandas as pd                 # pip install pandas
import numpy as np                  # pip install numpy
import matplotlib.pyplot as plt     # pip install matplotlib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv('sl.csv')

# data frame is similar to RDBMS Table , stored in memory with rows and columns
print(data.head())    # prints top 5 records
print(data.shape)     # prints no of rows and columns

# Independent and dependent variables
x = data[['GPA']]   # X is independent variable
y = data[['SAT']]   # y is dependent variable

# Split data
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=0
)

# Train model
model = LinearRegression()
model.fit(x_train, y_train)

# Predictions
y_pred = model.predict(x_test)
x_pred = model.predict(x_train)

# Visualizing the Training set results
plt.scatter(x_train, y_train, color="blue")
plt.plot(x_train, x_pred, color="red")
plt.title("SAT vs GPA (Training Dataset)")
plt.xlabel("SAT SCORE")
plt.ylabel("GPA")
plt.savefig("train_plot.png")   # ✅ Save instead of show
plt.close()

# Visualizing the Test set results
plt.scatter(x_test, y_test, color="blue")
plt.plot(x_test, y_pred, color="red")
plt.title("SAT vs GPA (Test Dataset)")
plt.xlabel("SAT")
plt.ylabel("GPA")
plt.savefig("test_plot.png")    # ✅ Save instead of show
plt.close()

# Model accuracy (R^2 score)
print("Model Accuracy:", model.score(x_test, y_test))
