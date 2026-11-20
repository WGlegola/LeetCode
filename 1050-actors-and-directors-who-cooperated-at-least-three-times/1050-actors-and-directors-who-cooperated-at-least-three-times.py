import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    x=actor_director.groupby('actor_id')['director_id'].value_counts().loc[lambda x:x>=3].reset_index().drop(columns='count')
    return x
    