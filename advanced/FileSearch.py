import os
import fnmatch

def find_albums(root, artist_name):
    for path, directories, files in os.walk(root):
        for artist in fnmatch.filter(directories, artist_name):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield (os.path.join(album_path, album), album)

def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):
            yield song

def filenames(directory, extension):
    for path, directories, files in os.walk(directory):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            absolute_path = os.path.abspath(path)
            yield os.path.join(absolute_path, file)

album_list = find_albums('./data/music', 'Aerosmith')
song_list = find_songs(album_list)

for f in filenames('./data/music', 'emp3'):
    print(f)
