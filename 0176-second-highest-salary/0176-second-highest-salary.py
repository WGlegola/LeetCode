import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    nlg = employee.drop_duplicates("salary").sort_values(by='salary',ascending=False)['salary']
    print(nlg)
    if nlg.count()<2:
        return pd.DataFrame({f'SecondHighestSalary':[None]})
    return pd.DataFrame({f'SecondHighestSalary':[nlg.iloc[1]]})
    