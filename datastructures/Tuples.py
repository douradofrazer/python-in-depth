t = ("a", "b", "c")  # good to use brackets but not necessary
print(t)
print("a", "b", "c")
print(("a", "b", "c"))

# Tuples are immutable
# imelda[1] = "Imelda May" will throw and exception
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the lightning", "Metallica", 1984
print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

"""
Value inside tuple cannot be reassigned as its immutable but
the variable can be reassigned to a new object.
NOTE: Right side of an assignment is evaluated before the left hand side
"""
imelda = imelda[0], "Imelda May", imelda[2]
print(imelda)

"""
Assignment of values
a = b = c = b = 9
a, b = 12, 13
print(a, b)
---swap--
a, b = b, a
print(a, b)
"""
title, artist, year = imelda  # unpacking the tuple
print(title)
print(artist)
print(year)

# --------------------------------------------------
media = "Thriller", "Jackson", 1990, ((1, "Beat It"), (2, "Billie Jean"), (3, "Human Nature"))
title, artist, year, tracks = media
print(title)
print(artist)
print(year)
print(tracks)
"""
NOTE: Tuple is immutable so its contents can't be changed, 
however if a tuple contains a list the contents of the list can be changed.
"""
media = "Thriller", "Jackson", 1990, ([(1, "Beat It"), (2, "Billie Jean"), (3, "Human Nature")])
media[3].append((5, "Modifying list"))
title, artist, year, tracks = media
for songs in tracks:
    track, title = songs
    print("\tTrack number is {}, Tile: {}".format(track, title))
