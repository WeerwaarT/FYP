# This script reads the filtered listening events data, groups the data by user_id and artist_id,
# then counts the number of occurrences for each user-artist pair (i.e., playcounts).
# The resulting playcounts are then saved to a new file 'LFM-1b_LEs_PC.txt'.

import pandas as pd

LEs_filtered = pd.read_csv('../LFM-1b/LFM-1b_LEs_filtered.txt', sep='\t', header=None)
LEs_filtered.columns = ['user_id', 'artist_id', 'album_id', 'track_id', 'timestamp']

# group by user-id and artist-id, then count the number of rows in each group
playcounts = LEs_filtered.groupby(['user_id', 'artist_id']).size().reset_index(name='playcount')

playcounts.to_csv('../LFM-1b/LFM-1b_LEs_PC.txt', sep='\t', index=False)
