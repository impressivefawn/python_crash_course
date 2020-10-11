# 8-8. User Albums:
def make_album(artist, title):
    """Build a dictionary describing a music album"""
    album_dict = {
        'artist': artist.title(), 
        'title': title.title()
        }
    return album_dict

while True:
    print("\nPlease tell me your favorite album’s artist and title:")
    print("(enter 'q' at any time to quit)")

    a_artist = input("Album’s artist: ")
    if a_artist == 'q':
        break
    t_title = input("Album’s title: ")
    if t_title == 'q':
        break
    print(make_album(a_artist, t_title))