# This script filters out artists from the dataset that are either not existing or lack genre annotations

with open('../LFM-1b_UGP/LFM-1b_artist_genres_allmusic.txt', 'r', encoding='utf-8') as infile_1, \
        open('../LFM-1b/LFM-1b_artists.txt', 'r', encoding='utf-8') as infile_2, \
        open('../LFM-1b_UGP/LFM-1b_artist_genres_allmusic_filtered.txt', 'w', encoding='utf-8') as outfile:
    all_artists = set()

    for line in infile_2:
        all_artists.add(line.split('\t', 1)[1].rstrip())

    for line in infile_1:
        line = line.rstrip()
        parts = line.split('\t')

        if len(parts) > 1 and parts[0] in all_artists:
            outfile.write(line + '\n')
