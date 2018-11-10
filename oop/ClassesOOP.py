# Classes - uses more OOP approach
class Song:
    """
    Class to represent a song
    Attributes:
    title (str): Title of the song
    artist (str): Name of the song creator
    duration (int): Duration of the song in seconds
    """

    def __init__(self, title, artist, duration=0):
        """Song init method"""
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title

    name = property(get_title)

# Album class
class Album:
    """
    Class to represent an Album, using it's track list
    Attributes:
        name (str): Name of the album
        year (int): Release year
        artist (str): Name of artist(s) who created the album
        tracks (list[Song]): List of songs on the album
    Methods:
        add_song: Used to add a new song to the album's track list
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = 'Various Artists'
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """
        Adds a song to the track list
        Args:
            song (Song): Title of song to add
            position (Optional[int]): if specified, the song will be added to that position
                in the track list - inserting it between other songs if necessary.
                Otherwise, the song will be added to the end of the list
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


#  Artist class
class Artist:
    """
    Basic class to store artist details
    Attributes:
        name (str): Name of the artist
        albums (list[Album]): list of the albums by this artists. The list includes
        only those albums in this collection, it is not an exhaustive list of the artist's
        published albums
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """ Add album to albums list """
        self.albums.append(album)

    def add_song(self, name, year, title):
        """
        Add new song to the collection of albums
        New album will be created in the collection if it does not exist
        """
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + ' not found')
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print('Album found ' + name)

        album_found.add_song(title)


# Find object
def find_object(field, list):
    """Check list to see if an object with a 'name'
    attribut equal to field exists, return if so"""
    for item in list:
        if item.name == field:
            return item
    return None


# Loading data
def load_data():
    artist_list = []
    with open('./data/albums.txt', 'r') as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

    return artist_list

# Checks if we got all artists, albums, and songs correctly
# Created file can be compared to original file
def create_checkfile(artists):
    """Create a check file from the object data for comparison with the original file"""
    with open('./data/checkfile.txt', 'w') as checkfile:
        for new_artist in artists:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print('{0.name}\t{1.name}\t{1.year}\t{2.title}'.format(new_artist, new_album, new_song), file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    create_checkfile(artists)
    print('There are {} artists'.format(len(artists)))
