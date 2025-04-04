# The dataset chosen for this experiment is a handmade fruits dataset. The dataset contains 60 records. Each record represents the following details of fruits :

# Weight - It is the mass of an object. With respect to this dataset, we have calculated the weights in grams

# Sphericity - is a measure of how closely the shape of an object approaches that of a mathematically perfect sphere.

# Color - Every fruit has a different color at different stages. You can encode the color to an integer value. For example

# Green as 20
# Greenish Yellow as 40
# Orange as 60
# Red as 80
# Reddish Yellow as 100
# Label - We have considered two fruits for simplicity. They are Apple and Orange.
    

# At the end of the experiment, you will be able to :

# * Classify fruits data using KNN classifier
# * Visualize the predictions before and after scaling
import os
import pandas as pd
import numpy as np

# Load the dataset
file_path = "d:/Mrigank-Preparation/IIITH AI/Mrigank-IIITH-AI/Unit 1 - LR KNN/data/social_advertising.csv"
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(df.head())
