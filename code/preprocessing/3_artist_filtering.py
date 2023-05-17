# This script replaces artist names with artist IDs, filters out artists that lack genre annotations.

with open('../LFM-1b_UGP/LFM-1b_artist_genres_allmusic_filtered.txt', 'r', encoding='utf-8') as infile_1, \
        open('../LFM-1b/LFM-1b_artists.txt', 'r', encoding='utf-8') as infile_2, \
        open('../LFM-1b/LFM-1b_artists_filtered.txt', 'w', encoding='utf-8') as outfile_1, \
        open('../LFM-1b_UGP/LFM-1b_artist_id_genres_allmusic_filtered.txt', 'w', encoding='utf-8') as outfile_2:
    genre_annotated_artists = {}
    for line in infile_1:
        if line:
            artist, genre = line.split('\t', 1)
            genre_annotated_artists[artist] = genre

    for line in infile_2:
        artist_id, artist = line.rstrip('\n').split('\t', 1)
        if artist in genre_annotated_artists:
            outfile_1.write(line)
            outfile_2.write(artist_id + '\t' + genre_annotated_artists[artist])
