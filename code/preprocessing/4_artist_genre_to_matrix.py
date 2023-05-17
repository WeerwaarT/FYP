# This script reads the genre data associated with each artist, transforms it into a binary format where each genre
# column represents the presence (1) or absence (0) of the corresponding genre for the artist. The output is a matrix
# with artist IDs as rows and genres as columns

import numpy as np
import pandas as pd

columns = ['artist_id', 'rnb', 'rap', 'electronic', 'rock', 'new age', 'classical', 'reggae', 'blues', 'country',
           'world', 'folk', 'easy listening', 'jazz', 'vocal', "children's", 'punk', 'alternative', 'spoken word',
           'pop', 'heavy metal']
rows = []
with open('../LFM-1b_UGP/LFM-1b_artist_id_genres_allmusic_filtered.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        numbers = list(map(int, line.rstrip().split('\t')))
        artist_id = numbers[0]
        indices = [i + 1 for i in numbers[1:]]
        row = np.zeros(21, dtype=int)
        row[0] = artist_id
        row[indices] = 1
        rows.append(pd.Series(row, index=columns))

df = pd.concat(rows, axis=1).T
df.to_csv('../LFM-1b_UGP/LFM-1b_artist_id_genres_allmusic_filtered_matrix.txt', sep='\t', index=False)
