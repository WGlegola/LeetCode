import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products.astype({'low_fats':str,'recyclable':str},copy=True).loc[(products['low_fats']=='Y') & (products['recyclable']=='Y')][['product_id']] 
    