import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data
file_path = '/Users/vaibhavreddy/Documents/Scripts/Spotify_Data-Analytics/spotify-2023.csv'
spotify_data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Converting the 'streams' column to numeric
spotify_data['streams'] = pd.to_numeric(spotify_data['streams'], errors='coerce')

# Dropping rows where 'streams' is NaN
spotify_data = spotify_data.dropna(subset=['streams'])

# Grouping by released_year and calculating the mean streams
yearly_streams = spotify_data.groupby('released_year')['streams'].mean().reset_index()

# Visualizing the average streams over the years
plt.figure(figsize=(10, 5))
sns.lineplot(data=yearly_streams, x='released_year', y='streams')
plt.title('Average Streams Over the Years')
plt.xlabel('Released Year')
plt.ylabel('Average Streams')
plt.show()
