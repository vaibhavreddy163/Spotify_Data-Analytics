import pandas as pd

# Load your data
file_path = '/Users/vaibhavreddy/Documents/Scripts/Spotify_Data-Analytics/spotify-2023.csv'
spotify_data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Removing commas and converting 'streams' column to numeric
spotify_data['streams'] = spotify_data['streams'].str.replace(',', '')
spotify_data['streams'] = pd.to_numeric(spotify_data['streams'], errors='coerce')

# Dropping rows where 'streams' is NaN
spotify_data = spotify_data.dropna(subset=['streams'])

# Handling missing values by dropping rows with NaN values (this can be adjusted based on the analysis needs)
spotify_data = spotify_data.dropna()

# Encoding categorical variables like 'key' and 'mode'
spotify_data = pd.get_dummies(spotify_data, columns=['key', 'mode'])

# Saving the cleaned data to a new CSV file
spotify_data.to_csv('/Users/vaibhavreddy/Documents/Scripts/Spotify_Data-Analytics/cleaned_spotify_data.csv', index=False)

# Displaying basic information of the cleaned DataFrame
spotify_data.info()
