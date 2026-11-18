import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    group=courses.groupby('class')['student'].nunique().reset_index()
    return pd.DataFrame({'class':group.loc[group['student']>=5]['class']})