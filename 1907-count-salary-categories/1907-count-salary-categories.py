import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    cats = ["Low Salary", "Average Salary", "High Salary"]
    label = accounts["income"].map(
        lambda x: "Low Salary" if x < 20000
        else ("High Salary" if x > 50000 else "Average Salary")
    )
    counts = label.value_counts().reindex(cats, fill_value=0)
    return pd.DataFrame(data={'category':cats,'accounts_count':counts})