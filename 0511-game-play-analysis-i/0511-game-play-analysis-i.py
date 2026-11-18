import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    grouped=activity.groupby('player_id')['event_date'].min()
    return pd.DataFrame({'player_id':grouped.index, 'first_login':grouped})