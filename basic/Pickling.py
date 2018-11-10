import pickle

imelda = ('More Mayhem', 'Imelda May', '2011', ((1, 'Pulling the Rug'),
                                                (2, 'Psycho'),
                                                (3, 'Mayhem'),
                                                (4, 'Kentish Town Waltz')))
even = list(range(0, 11, 2))
odd = list(range(1, 11, 2))
number = 223455653

with open('../data/imelda.pickle', 'wb') as pickleFile:
    pickle.dump(imelda, pickleFile)
    pickle.dump(even, pickleFile)
    pickle.dump(odd, pickleFile)
    pickle.dump(number, pickleFile)

with open('../data/imelda.pickle', 'rb') as imeldaPickle:
    imelda2 = pickle.load(imeldaPickle)
    evenList = pickle.load(imeldaPickle)
    oddList = pickle.load(imeldaPickle)
    someNumber = pickle.load(imeldaPickle)

print('-' * 50)

album, artist, year, trackList = imelda2
print(album)
print(artist)
print(year)
for track in trackList:
    trackNumber, trackTitle = track
    print(trackNumber, trackTitle)

print('-' * 50)

for i in evenList:
    print(i)

for i in oddList:
    print(i)

print(someNumber)
