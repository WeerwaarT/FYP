# This script generates the Artist Fan Profiles (AFP) for a given set of thresholds. The profiles represent the genre
# preferences of the fans for each artist.

import numpy as np
import pandas as pd

thresholds = [10, 20, 50, 100, 200]

dfs = {}
for threshold in thresholds:
    df = pd.read_csv(f'../LFM-1b_UGP/LFM-1b_UGP_allmusic_sampled_filtered_{threshold}.txt', sep='\t')
    df.set_index('user_id', inplace=True)
    dfs[threshold] = df

df_artists = pd.read_csv('../LFM-1b/LFM-1b_artists_filtered.txt', sep='\t', header=None)
artist_fan_profiles = {threshold: {artist_id: np.zeros(20) for artist_id in df_artists[0].values}
                       for threshold in thresholds}

df_plays = pd.read_csv('../LFM-1b/LFM-1b_LEs_PC.txt', sep='\t')
grouped_plays = df_plays.groupby('user_id')

for user_id in df_plays['user_id'].unique():
    user_plays = grouped_plays.get_group(user_id)
    for threshold in thresholds:
        user_genre_profile = dfs[threshold].loc[user_id].values
        mask = user_plays['playcount'] >= threshold
        artist_ids = user_plays[mask]['artist_id'].values

        for artist_id in artist_ids:
            artist_fan_profiles[threshold][artist_id] += user_genre_profile

genre_columns = ['rnb', 'rap', 'electronic', 'rock', 'new age', 'classical', 'reggae', 'blues', 'country',
                 'world', 'folk', 'easy listening', 'jazz', 'vocal', "children's", 'punk', 'alternative', 'spoken word',
                 'pop', 'heavy metal']

for threshold, fan_profile in artist_fan_profiles.items():
    df = pd.DataFrame.from_dict(fan_profile, orient='index')
    df.columns = genre_columns
    df.index.name = 'artist_id'
    df.to_csv(f'../LFM-1b_UGP/AFP/LFM-1b_AFP_{threshold}.txt', sep='\t')

    df_normalized = df.div(df.sum(axis=1), axis=0)
    df_normalized.to_csv(f'../LFM-1b_UGP/AFP/LFM-1b_AFP_{threshold}_normalized.txt', sep='\t')
