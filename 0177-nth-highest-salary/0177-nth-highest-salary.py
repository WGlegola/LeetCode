import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    nlg = employee.drop_duplicates("salary").sort_values(by='salary',ascending=False)['salary']
    print(nlg)
    if nlg.count()<N or N<=0:
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})
    return pd.DataFrame({f'getNthHighestSalary({N})':[nlg.iloc[N-1]]})