# Define the songs for each album
albums = {
    'Taylor Swift': ["Tim McGraw", "Picture to Burn", "Teardrops on My Guitar", "A Place in This World", "Cold as You",
                     "The Outside", "Tied Together with a Smile", "Stay Beautiful", "Should’ve Said No",
                     "Mary’s Song (Oh My My My)", "Our Song", "I’d Lie", "I’m Only Me When I’m with You",
                     "Invisible", "A Perfectly Good Heart"],
    "Fearless (Taylor's Version": ["Fearless (Taylor’s Version)", "Fifteen (Taylor’s Version)", "Love Story (Taylor’s Version)",
                                   "Hey Stephen (Taylor’s Version)", "White Horse (Taylor’s Version)",
                                   "You Belong with Me (Taylor’s Version)", "Breathe (Ft. Colbie Caillat) (Taylor’s Version)",
                                   "Tell Me Why (Taylor’s Version)", "You’re Not Sorry (Taylor’s Version)", "The Way I Loved You (Taylor’s Version)",
                                   "Forever & Always (Taylor’s Version)", "The Best Day (Taylor’s Version)", "Change (Taylor’s Version)",
                                   "Jump Then Fall (Taylor’s Version)", "Untouchable (Taylor’s Version)", "Forever & Always (Piano Version) (Taylor’s Version)",
                                   "Come In With the Rain (Taylor’s Version)", "SuperStar (Taylor’s Version)", "The Other Side of the Door (Taylor’s Version)",
                                   "Today Was a Fairytale (Taylor’s Version)", "You All Over Me (From The Vault) Ft. Maren Morris"
],
    "Speak now": ["Mine", "Sparks Fly", "Back to December", "Speak Now", "Dear John", "Mean", "The Story of Us", "Never Grow Up",
                  "Enchanted", "Better than Revenge", "Innocent", "Haunted", "Last Kiss", "Long Live", "Ours",
                  "If This Was a Movie", "Superman"
],

}


import random
# Define a function to prompt the user to compare two songs and return the preferred song
def compare_songs(song1, song2):
    response = input(f'Which song do you prefer: \n1. {song1}\n2. {song2}\n')
    if response.lower() == "1" :
        return song1
    elif response.lower() == "2" :
        return song2
    else:
        print('Invalid input, please try again...')
        return compare_songs(song1, song2)


# Create a list of all the songs
all_songs = []
for album, songs in albums.items():
    all_songs.extend(songs)

# Shuffle the list of all songs
random.shuffle(all_songs)

# Ask the user to compare all songs and collect their preferred songs
ratings = {}
for i in range(len(all_songs) - 1):
    song1, song2 = all_songs[i], all_songs[i+1]
    response = compare_songs(song1, song2)
    if response == song1:
        preferred_song = song1
        other_song = song2
    else:
        preferred_song = song2
        other_song = song1
    for album, songs in albums.items():
        if preferred_song in songs:
            album_ratings = ratings.get(album, [])
            album_ratings.append(songs.index(preferred_song))
            ratings[album] = album_ratings
        if other_song in songs:
            album_ratings = ratings.get(album, [])
            album_ratings.append(songs.index(other_song))
            ratings[album] = album_ratings


# Calculate the average rating for each album
album_ratings = {}
for album, ratings_list in ratings.items():
    album_rating = sum(ratings_list) / len(ratings_list)
    album_ratings[album] = album_rating

# Sort the album ratings from highest to lowest and display them
sorted_album_ratings = sorted(album_ratings.items(), key=lambda x: x[1], reverse=True)
print('Album ratings (highest to lowest):')
for album, rating in sorted_album_ratings:
    print(f'{album}: {rating:.2f}')

########
# First, calculate the average rating for each song
song_ratings = {}
for album, songs in albums.items():
    for song in songs:
        ratings_for_song = ratings.get(song, [])
        if ratings_for_song:
            average_rating = sum(ratings_for_song) / len(ratings_for_song)
            song_ratings[song] = average_rating

# Sort the songs by their ratings, from highest to lowest
sorted_songs = sorted(song_ratings, key=song_ratings.get, reverse=True)

# Print the sorted list of songs
print('Here are the songs, ranked from highest to lowest based on your ratings:')
for rank, song in enumerate(sorted_songs, start=1):
    print(f'{rank}. {song}')
