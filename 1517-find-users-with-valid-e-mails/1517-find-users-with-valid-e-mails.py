import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    legit = 'abcdefghijklmnoprstuwxyz'
    addLegit= '_.-'
    return users.loc[(users['mail'].map(lambda u: u.endswith('@leetcode.com') and u.count('@') == 1 and u[0] not in list(addLegit  + '1234567890') and len([x for x in u.split('@')[0] if x not in list(string.ascii_lowercase + string.ascii_uppercase + '1234567890' + addLegit)]) == 0 ))]