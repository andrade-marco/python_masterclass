import os

root = './data/music'

for path, directories, files in os.walk(root, topdown=True):
    if files:
        print(path)
        first_split = os.path.split(path)
        second_split = os.path.split(first_split[0])
        print(first_split)
        print(second_split)
        for f in files:
            song_details = f[:-5].split('-')
            print(song_details)
        print('-' * 40)
