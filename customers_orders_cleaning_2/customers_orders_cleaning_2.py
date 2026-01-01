import pandas as pd
import numpy as np

orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5, 6, 7],
    "cust_id": [10, 10, 11, 11, 12, 12, None],
    "month": ["Jan", "Feb", "Jan", "Feb", "Jan", "Mar", "Feb"],
    "amount": ["100.50", "bad", "200", None, "50", "75.25", "300"],
    "items": ["2", "1", "3", "bad", None, "2", "1"]
})

customers = pd.DataFrame({
    "cust_id": [10, 11, 12, 13],
    "customer_name": ["Acme", "BetaCo", "CoreMart", "DeltaLLC"],
    "region": ["East", "West", "East", "South"]
})

def convert_to_numeric(x):
    return pd.to_numeric(x, errors="coerce")

orders["amount"] = convert_to_numeric(orders["amount"])
orders["items"] = convert_to_numeric(orders["items"])

orders = orders.dropna(subset=["cust_id", "amount", "items"])

orders = orders.assign(
    avg_price_per_item=(orders["amount"] / orders["items"].replace(0, np.nan)).round(2)
)

orders_agg = orders.groupby("cust_id").agg(
    total_amount=("amount", "sum"),
    avg_amount=("amount", "mean"),
    total_items=("items", "sum"),
    avg_price_per_item=("avg_price_per_item", "mean")
)

final_df = orders_agg.merge(customers, on="cust_id", how="inner")

print(final_df.to_string( ))
