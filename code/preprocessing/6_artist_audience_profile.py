# This code calculates the audience profile for each artist based on user interactions stored in the
# 'LFM-1b_LEs_filtered.txt' file. It then normalizes the audience profiles and saves them to separate files

import numpy as np
import pandas as pd

threshold = 200  # 10, 20, 50, 100, 200

df = pd.read_csv(f'../LFM-1b_UGP/LFM-1b_UGP_allmusic_sampled_filtered_{threshold}.txt', sep='\t')
df.set_index('user_id', inplace=True)

artist_genre_matrix = pd.read_csv('../LFM-1b_UGP/LFM-1b_artist_id_genres_allmusic_filtered_matrix.txt', sep='\t')
artist_genre_matrix.set_index('artist_id', inplace=True)
artist_audience_profile = {artist_id: np.zeros(20) for artist_id, _ in artist_genre_matrix.iterrows()}

LEs_filtered = pd.read_csv('../LFM-1b/LFM-1b_LEs_filtered.txt', sep='\t', header=None)
LEs_filtered.columns = ['user_id', 'artist_id', 'album_id', 'track_id', 'timestamp']

# iterate over the rows of the dataframe
for _, row in LEs_filtered.iterrows():
    user_id, artist_id = int(row['user_id']), int(row['artist_id'])
    artist_audience_profile[artist_id] += df.loc[user_id].values \
        if np.dot(artist_genre_matrix.loc[artist_id].values, df.loc[user_id].values) >= 1 else 0

df_new = pd.DataFrame.from_dict(artist_audience_profile, orient='index')
df_new.columns = artist_genre_matrix.columns
df_new.index.name = 'artist_id'
df_new.to_csv(f'../LFM-1b_UGP/AAP/LFM-1b_AAP_{threshold}.txt', sep='\t')

df_normalized = df_new.div(df_new.sum(axis=1), axis=0)
df_normalized.to_csv(f'../LFM-1b_UGP/AAP/LFM-1b_AAP_{threshold}_normalized.txt', sep='\t')
