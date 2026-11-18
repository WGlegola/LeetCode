import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients.loc[patients['conditions'].map(lambda x : len([s for s in x.split(' ') if s.startswith('DIAB1')])>0)]