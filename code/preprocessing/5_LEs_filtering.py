# This script filters the contents of 'LFM-1b_LEs.txt' based on matching user and artist IDs found in the respective
# datasets, 'LFM-1b_artists_filtered.txt' and 'LFM-1b_UGP/sample_user_ids.txt'. The filtered lines are written to
# 'LFM-1b_LEs_filtered.txt'.

import pandas as pd


with open('../LFM-1b/LFM-1b_LEs.txt', 'r', encoding='utf-8') as infile, \
        open('../LFM-1b/LFM-1b_LEs_filtered.txt', 'w', encoding='utf-8') as outfile:
    df_artist = pd.read_csv('../LFM-1b/LFM-1b_artists_filtered.txt', sep='\t', header=None)
    artist_ids = set(str(artist_id) for artist_id in df_artist[0].tolist())

    df_user = pd.read_csv('../LFM-1b_UGP/sample_user_ids.txt')
    user_ids = set(str(user_id) for user_id in df_user['user_id'].tolist())

    for line in infile:
        if line:
            parts = line.split('\t', 2)
            if parts[0] in user_ids and parts[1] in artist_ids:
                outfile.write(line)
