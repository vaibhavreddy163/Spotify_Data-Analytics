import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data
file_path = '/Users/vaibhavreddy/Documents/Scripts/Spotify_Data-Analytics/spotify-2023.csv'
spotify_data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Removing commas from the 'in_deezer_playlists' column and converting to numeric
spotify_data['in_deezer_playlists'] = spotify_data['in_deezer_playlists'].str.replace(',', '').astype(float)

# Summing playlist and chart appearances for each platform
spotify_data['spotify_presence'] = spotify_data['in_spotify_playlists'] + spotify_data['in_spotify_charts']
spotify_data['apple_presence'] = spotify_data['in_apple_playlists'] + spotify_data['in_apple_charts']
spotify_data['deezer_presence'] = spotify_data['in_deezer_playlists'] + spotify_data['in_deezer_charts']

# Visualizing the presence on different platforms
plt.figure(figsize=(10, 5))
sns.boxplot(data=spotify_data[['spotify_presence', 'apple_presence', 'deezer_presence']])
plt.title('Distribution of Song Presence Across Different Platforms')
plt.ylabel('Presence (Playlists + Charts)')
plt.show()
