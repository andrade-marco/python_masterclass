# Tuples
#################
tupleOne = 'a', 'b', 'c'
tupleTwo = ('a', 'b', 'c')

welcome = ('Welcome to my Nightmare', 'Alice Cooper', 1975)
album, artist, year = welcome  # Deconstructing tuple

print(artist)

imelda = 'More Mayhem', 'Imelda May', 2011, (
    (1, 'Pulling the Rug'), (2, 'Psycho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz'))

album, artist, year, tracks = imelda
print('Album details')
print('*' * 40)
print('Artist: ' + artist)
print('Album: ' + album)
print('Year: ' + str(year))
print('\tTracks: ', end='')
for song in tracks:
    print('{0}: {1}'.format(song[0], song[1]), end=", ")
