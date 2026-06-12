class Song:
    count = 0
    genres = {}
    artists = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Total number of Song instances
        Song.count += 1

        # Count songs by genre
        if genre in Song.genres:
            Song.genres[genre] += 1
        else:
            Song.genres[genre] = 1

        # Count songs by artist
        if artist in Song.artists:
            Song.artists[artist] += 1
        else:
            Song.artists[artist] = 1