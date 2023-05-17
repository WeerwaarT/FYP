import numpy as np
import pandas as pd

df = pd.read_csv('../LFM-1b_UGP/sample_user_ids.txt', header=None)
train_id_set = set(df[0].tolist())

df = pd.read_csv('../LFM-1b_UGP/LFM-1b_UGP_weightedPC_allmusic.txt', sep='\t')
user_id_set = set(df['user_id'])

diff_set = user_id_set - train_id_set
test_id_set = np.random.choice(list(diff_set), 400, replace=False)
test_id_set = set(str(user_id) for user_id in test_id_set)

lines = []

with open('../LFM-1b/LFM-1b_LEs.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        if line:
            parts = line.split('\t', 2)
            user_id, artist_id = parts[0], parts[1]
            if user_id in test_id_set:
                lines.append([user_id, artist_id, 1])

df = pd.DataFrame(lines, columns=['user_id', 'artist_id', 'playcount'])
df = df.groupby(['user_id', 'artist_id']).size().reset_index(name='playcount')

df.to_csv('test_playcounts.txt', index=False, sep='\t')
