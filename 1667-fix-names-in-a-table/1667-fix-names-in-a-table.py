import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].map(lambda x: x.lower().capitalize())
    return users.sort_values('user_id')