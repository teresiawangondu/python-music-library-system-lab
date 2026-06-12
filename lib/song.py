class Song:
    count = 0

    genres = {}
    artists = {}

    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1

        # genres dictionary
        Song.genres[genre] = Song.genres.get(genre, 0) + 1

        # artists dictionary
        Song.artists[artist] = Song.artists.get(artist, 0) + 1

        # duplicate dictionaries required by the tests
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1