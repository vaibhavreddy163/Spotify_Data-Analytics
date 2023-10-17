import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data
file_path = '/Users/vaibhavreddy/Documents/Scripts/Spotify_Data-Analytics/spotify-2023.csv'
spotify_data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Setting the aesthetic style of the plots
sns.set_style("whitegrid")

# Creating a list of features to analyze
features_to_analyze = ['bpm', 'danceability_%', 'valence_%', 'energy_%', 'acousticness_%']

# Creating a figure object
plt.figure(figsize=(15, 10))

# Creating subplots for each feature
for i, feature in enumerate(features_to_analyze, 1):
    plt.subplot(2, 3, i)
    sns.histplot(spotify_data[feature], kde=True, bins=30, color='skyblue')
    plt.title(f'Distribution of {feature}')
    plt.xlabel('')
    plt.ylabel('')

# Adjusting the layout
plt.tight_layout()
plt.show()
