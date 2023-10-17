import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset into a pandas DataFrame
file_path = '/Users/vaibhavreddy/Documents/Scripts/Spotify_Data-Analytics/spotify-2023.csv'
spotify_data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Artist Prevalence Analysis
# Counting the number of tracks by each artist
artist_counts = spotify_data['artist(s)_name'].value_counts().head(10)

# Visualizing the artists with the most tracks in the dataset
plt.figure(figsize=(10, 6))
sns.barplot(x=artist_counts.values, y=artist_counts.index, palette='viridis')
plt.xlabel('Number of Tracks')
plt.ylabel('Artist(s)')
plt.title('Top 10 Artists with the Most Tracks in the Dataset')
plt.show()
