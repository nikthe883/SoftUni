import os
def add_songs(*args):

    lyrics = {}

    for i in args:
        if i[0] not in lyrics:
            lyrics[i[0]] = []
        lyrics[i[0]].extend(i[1])

    result = []
    for song_title, song_lyrics in lyrics.items():
        result.append('- ' + song_title)
        if song_lyrics:
            result.extend(song_lyrics)
    return os.linesep.join(result)

