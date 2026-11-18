import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders.groupby('customer_number',as_index=False)['order_number'].nunique().sort_values('order_number')[['customer_number']].iloc[-1:]