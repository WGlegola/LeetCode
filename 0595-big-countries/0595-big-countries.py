import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([world.loc[world['area']>=3000000 ,['name','population','area']],world.loc[world['population']>=25000000,['name','population','area']]]).drop_duplicates()
    