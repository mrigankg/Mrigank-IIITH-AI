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

slope = model.coef_[0] # its an array hence used index 0 as there can be multiple intercept for each feature. Here we have only 1 feature.#Mean squar error
intercept = model.intercept_

predict = model.predict(x)

print("Slope: ", slope)
print("Intercept: ", intercept)

plt.plot(df['x'], df['y'], color = "green")
plt.plot(df['x'], predict , color='red')
# plt.show();

# mean square error

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y, predict)
print("Mean Squared Error: ", mse)
print("Round MSE : ", round(mse, 2))

print(model.score(x,y)) #In summary, you use the actual values in model.score to evaluate how well the model's predictions match the real data.
