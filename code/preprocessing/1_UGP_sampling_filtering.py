# This script loads the playcount data for different music genres associated with each user. It then applies various
# threshold values to determine user preferences for each genre. The sampled user data and the processed playcount data
# (binary representation indicating whether the playcount exceeds the threshold for each genre) are then saved to
# separate files for further analysis.

import pandas as pd

df = pd.read_csv('../LFM-1b_UGP/LFM-1b_UGP_weightedPC_allmusic.txt', sep='\t')
thresholds = [10, 20, 50, 100, 200]

df_sampled = df.sample(n=2000)
df_sampled['user_id'].to_csv('../LFM-1b_UGP/sample_user_ids.txt', index=False)

for threshold in thresholds:
    over_threshold_plays = df_sampled.iloc[:, 1:] >= threshold
    df_copy = df_sampled.copy()
    df_copy.iloc[:, 1:] = over_threshold_plays.astype(int)
    df_copy.to_csv(f'../LFM-1b_UGP/LFM-1b_UGP_allmusic_sampled_filtered_{threshold}.txt', sep='\t', index=False)
