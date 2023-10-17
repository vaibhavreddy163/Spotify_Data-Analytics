import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load your data
file_path = '/Users/vaibhavreddy/Documents/Scripts/Spotify_Data-Analytics/cleaned_spotify_data.csv'
spotify_data = pd.read_csv(file_path)

# Selecting features and target variable
X = spotify_data.select_dtypes(include=['number']).drop(columns=['streams'])
y = spotify_data['streams']

# Splitting the data into training and test sets (80% training, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Building and training the Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Printing the evaluation metrics
print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R2) score: {r2}")
