import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    group = employee['managerId'].value_counts()[lambda s:s>=5]
    return employee[employee['id'].isin(group.index)][['name']]
