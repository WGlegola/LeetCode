import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['periods'] = employees.out_time - employees.in_time 
    grouped = employees.groupby(['emp_id', 'event_day'],as_index = False)['periods'].sum().sort_values('event_day')
    return pd.DataFrame({'day':grouped.event_day,'emp_id':grouped.emp_id,'total_time':grouped.periods})