class Song:
    # Class attributes
    total_songs = 0
    all_artists = []
    all_genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class attributes
        Song.total_songs += 1

        if artist not in Song.all_artists:
            Song.all_artists.append(artist)

        if genre not in Song.all_genres:
            Song.all_genres.append(genre)

        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1

    def play(self):
        return f"Playing '{self.name}' by {self.artist}"

    @classmethod
    def get_total_songs(cls):
        return cls.total_songs

    @classmethod
    def get_all_artists(cls):
        return cls.all_artists

    @classmethod
    def get_all_genres(cls):
        return cls.all_genres

    @classmethod
    def get_genre_count(cls, genre):
        return cls.genre_count.get(genre, 0)

    @classmethod
    def get_artist_count(cls, artist):
        return cls.artist_count.get(artist, 0)


# Example usage / testing
if __name__ == "__main__":
    song1 = Song("Blinding Lights", "The Weeknd", "Pop")
    song2 = Song("Levitating", "Dua Lipa", "Pop")
    song3 = Song("Bad Guy", "Billie Eilish", "Pop")
    song4 = Song("Rolling in the Deep", "Adele", "Soul")

    print(song1.play())
    print("Total songs:", Song.get_total_songs())
    print("All artists:", Song.get_all_artists())
    print("All genres:", Song.get_all_genres())
    print("Pop genre count:", Song.get_genre_count("Pop"))
    print("Dua Lipa song count:", Song.get_artist_count("Dua Lipa"))
    pass
