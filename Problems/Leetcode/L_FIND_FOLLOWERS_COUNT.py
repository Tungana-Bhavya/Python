Find Followers Count
-----------------------

import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    df = followers.groupby('user_id').nunique('follower_id').sort_values(by='user_id', ascending=True).reset_index()
    df = df.rename(columns = {'follower_id':'followers_count'})
    return df
