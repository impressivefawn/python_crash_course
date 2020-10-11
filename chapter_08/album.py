# 8-7. Album:
def make_album(artist, title):
    """Build a dictionary describing a music album"""
    album_dict = {
        'artist': artist.title(), 
        'title': title.title()
        }
    return album_dict

album = make_album('linkin park', 'meteora')
print(album)

album = make_album('eminem', 'recovery')
print(album)

album = make_album('green day', 'american idiot')
print(album)


def make_album(artist, title, songs=None):
    """Build a dictionary describing a music album"""
    if songs:
        album_dict = {
            'artist': artist.title(), 
            'title': title.title(),
            'songs': songs
        }
    else:
        album_dict = {
            'artist': artist.title(), 
            'title': title.title()
            }
    return album_dict

album = make_album('linkin park', 'meteora', 13)
print(album)

album = make_album('eminem', 'recovery')
print(album)

album = make_album('green day', 'american idiot', 13)
print(album)