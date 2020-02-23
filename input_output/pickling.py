import pickle

imelda = ("More Mayhem",
          "Imelda May",
          "2011",
          ((1, "Pulling The Rug"),
           (2, "Psycho"),
           (3, "Mayhem"),
           (4, "Kentish Town Waltz")))

even = range(0, 10, 2)
odd = range(1, 10, 2)

# default protocol is 3 for pickling data
with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)
    pickle.dump(even, pickle_file)
    pickle.dump(odd, pickle_file)
    pickle.dump(2983974, pickle_file)
# object must be read in the same order that they are written
with open("imelda.pickle", "rb") as imelda_pickle:
    imelda2 = pickle.load(imelda_pickle)
    even_list = pickle.load(imelda_pickle)
    odd_list = pickle.load(imelda_pickle)
    x = pickle.load(imelda_pickle)

print(imelda2)
album, artist, year, track_list = imelda2

for tack in track_list:
    track_number, track_title = tack
    print(track_number, track_title)

print('=' * 20)

for i in even_list:
    print(i)

print('=' * 20)

for j in odd_list:
    print(j)

print('=' * 20)

print(x)
