# %%
import re
import pandas as pd
import numpy as np

# %%
df=pd.read_csv("dataset/sample-dataset.csv")

# %%
df

# %%
df = df.dropna(subset=['title'])

# %%
df = df.replace(to_replace=[r'<.*?>', r'http\S+'], value='', regex=True)

# %%
df

# %% [markdown]
# 

# %%
def replacep(tag_string):
    return tag_string.replace('|', ' ')
df['tags'] = df['tags'].apply(replacep)

# %%
df

# %%
df.head

# %%


# %%
def get_unique_tags(tag_string):
    return set(tag_string.split('|'))
df['unique_tags'] = df['tags'].apply(get_unique_tags)
all_unique_tags = [tag for sublist in df['unique_tags'] for tag in sublist]
tag_frequency = pd.Series(all_unique_tags).value_counts()
tag_frequency

# %%
THRESHOLD=2

# %%
popular_tags = tag_frequency[tag_frequency > THRESHOLD]

# %%
popular_tags

# %%
tag_frequency = df['tags'].value_counts().to_dict()

# Check if a tag should be kept
def should_keep(row):
    tags = row['tags'].split(',')
    for tag in tags:
        if tag_frequency[tag] >= THRESHOLD:
            return True
    return False

# Apply filter
filtered_df = df[df.apply(should_keep, axis=1)]

# %%
filtered_df

# %%


# %%



