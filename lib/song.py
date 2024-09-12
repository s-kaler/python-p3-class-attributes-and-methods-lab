class Song:

    all = []
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_all(self)
        Song.add_genre(genre)
        Song.add_artist(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_all(cls, song):
        cls.all.append(song)
        cls.count += 1

    @classmethod
    def show_song_names(cls):
        print([song.name for song in cls.all])
    
    @classmethod
    def add_genre(cls, genre):
        if not genre in cls.genres:
            cls.genres.append(genre)
    
    @classmethod
    def add_artist(cls, artist):
        if not artist in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1