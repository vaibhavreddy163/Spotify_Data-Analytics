import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

# Load your data
file_path = '/Users/vaibhavreddy/Documents/Scripts/Spotify_Data-Analytics/cleaned_spotify_data.csv'
spotify_data_new = pd.read_csv(file_path)

# Features to be used for the recommendation
features = ['danceability_%', 'valence_%', 'energy_%', 'acousticness_%', 'instrumentalness_%', 'liveness_%', 'speechiness_%']

# Handling potential missing values in the selected features by filling them with the mean
spotify_data_new[features] = spotify_data_new[features].fillna(spotify_data_new[features].mean())

# Extracting and scaling the selected features
recommendation_data = spotify_data_new[features]
scaler = MinMaxScaler()
recommendation_data_scaled = scaler.fit_transform(recommendation_data)

# Calculating the cosine similarity between songs
cosine_sim = cosine_similarity(recommendation_data_scaled)

# Function to get song recommendations based on user input
def get_song_recommendations(num_recommendations=5):
    track_name = input("Enter a song name: ")
    
    # Finding songs that contain the words from the input
    matched_songs = spotify_data_new[spotify_data_new['track_name'].str.contains(track_name, case=False)]
    
    # If no matches are found
    if matched_songs.empty:
        print("No songs found with the given words in the title.")
        return
    
    # If multiple matches are found, ask the user to select one
    if len(matched_songs) > 1:
        print("Multiple songs found. Please select the correct one:")
        for i, song in enumerate(matched_songs['track_name']):
            print(f"{i+1}: {song}")
        selection = int(input("Enter the number of the correct song: ")) - 1
        idx = matched_songs.index[selection]
    else:
        idx = matched_songs.index[0]
    
    # Getting recommendations based on the selected song
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]  # Skipping the input song itself
    song_indices = [i[0] for i in sim_scores]
    return spotify_data_new['track_name'].iloc[song_indices]

# Testing the recommendation function (you can run this line to test the function)
recommended_songs = get_song_recommendations()
print(recommended_songs)
