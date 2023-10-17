import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data
file_path = '/Users/vaibhavreddy/Documents/Scripts/Spotify_Data-Analytics/spotify-2023.csv'
spotify_data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Converting the 'streams' column to numeric, ignoring errors to keep non-convertible values as NaN
spotify_data['streams'] = pd.to_numeric(spotify_data['streams'], errors='coerce')

# Dropping rows where 'streams' is NaN
spotify_data = spotify_data.dropna(subset=['streams'])

# Creating a list of features to analyze
features_to_analyze = ['bpm', 'danceability_%', 'valence_%', 'energy_%', 'acousticness_%']

# Calculating the correlation between 'streams' and musical features
correlation = spotify_data[['streams'] + features_to_analyze].corr()

# Displaying the correlation
print(correlation)

# Visualizing the correlation
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', linewidths=2, linecolor='black')
plt.title('Correlation between Musical Features and Popularity (Streams)')
plt.show()
