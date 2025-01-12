import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt


df = pd.DataFrame({'x':[0,1,2,3,5,],'y':[ 0.99, 3.02, 9.0 , 18.98 , 33.01]})
print(df)

# 2D Array for x:

#[x = df[['x']]](http://vscodecontentref/1) creates a DataFrame with a single column 'x'. 
# This results in a 2D array (or matrix) where each row represents a different data point 
# and each column represents a different feature. Even if there's only one feature, it's still 
# treated as a 2D array because many machine learning libraries expect the input features to be 
# in this format.
x = df[['x']] #input is always 2D array 

# y = df['y'] creates a Series (or 1D array) with the target variable 'y'. 
# This is because the target variable is a single value for each data point, not a set of 
# features.
y = df['y']

model = LinearRegression();
model.fit(x, y);

slope = model.coef_[0]
intercept = model.intercept_

predict = model.predict(x)

print("Slope: ", slope)
print("Intercept: ", intercept)

plt.plot(df['x'], df['y'], color = "green")
plt.plot(df['x'], predict , color='red')
plt.show();

abc = np.array([6, 7, 8, 9, 10]).reshape(-1, 1)
print(abc)