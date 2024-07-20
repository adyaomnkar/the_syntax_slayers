import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
file_path = '/mnt/data/fdata.csv'
data = pd.read_csv("fdata.csv")

# Handle missing values (if any)
data.dropna(inplace=True)

# Selecting relevant features
features = ['Crop_Year', 'Area', 'Max _Team', 'Min_Temp', 'Avg_temp', 'Rainfall', 'Humidity']
categorical_features = ['State_Name', 'District_Name', 'Season', 'Crop', 'Soil']

# One-hot encoding categorical variables
encoder = OneHotEncoder(sparse=False)
encoded_categorical = encoder.fit_transform(data[categorical_features])

# Concatenate encoded categorical features with the rest of the features
features_data = np.concatenate([data[features].values, encoded_categorical], axis=1)
target = data['Production'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features_data, target, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


print(f"R-squared (R²) Score: {r2}")
