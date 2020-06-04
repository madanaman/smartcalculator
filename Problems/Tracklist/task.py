def tracklist(**kwargs):
    for k in kwargs.keys():
        print(k)
        for x, y in kwargs[k].items():
            print("ALBUM:", x, "TRACK:", y)

#
# tracklist(Woodkid={"The Golden Age": "Run Boy Run",
#                    "On the Other Side": "Samara"},
#           Cure={"Disintegration": "Lovesong",
#                 "Wish": "Friday I'm in love",
#                 "Seventeen Seconds": "A Forest"})
