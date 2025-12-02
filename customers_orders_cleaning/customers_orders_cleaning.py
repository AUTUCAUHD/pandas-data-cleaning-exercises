import pandas as pd

customers_raw = pd.DataFrame({
    "CustID": [" 100", "101 ", "0102", "103", None, "  104  ", "105"],
    "FullName": ["john doe", " Jane   Smith", "CARLOS DIAZ", None, "  Mia  Chen", "Mia Chen", "  "],
    "City": ["miami ", " Miami", "ORLANDO", "Tampa", None, "Orlando ", ""]
})

orders_raw = pd.DataFrame({
    "ID": [100, 101, 102, 103, 106, None],
    "OrderTotal": ["250", " 310 ", "abc", "499", "600", "100"],
    "Status": ["completed", "Completed", "pending", "INVALID", "completed", "pending"]
})

# Cleans Customers Raw

# CustID
customers_raw["CustID"] = customers_raw["CustID"].str.strip()
customers_raw.dropna(subset=["CustID"], inplace=True)
customers_raw["CustID"] = customers_raw["CustID"].str.lstrip('0')
customers_raw["CustID"] = pd.to_numeric(customers_raw["CustID"], errors="coerce")

# FullName
customers_raw["FullName"] = customers_raw["FullName"].str.lower().str.title().str.strip().str.replace(r'\s+', ' ', regex=True)
customers_raw["FullName"] = customers_raw["FullName"].replace({"": None})
customers_raw.dropna(subset=["FullName"], inplace=True)

# City
customers_raw["City"] = customers_raw["City"].str.strip().str.title().str.replace(r'\s+', " ", regex=True)
customers_raw["City"] = customers_raw["City"].replace({"": None})
customers_raw.dropna(subset=["City"], inplace=True)


# Cleans Orders Raw

#ID
orders_raw.dropna(subset=["ID"], inplace=True)

# OrdersTotal
orders_raw["OrderTotal"] = pd.to_numeric(orders_raw["OrderTotal"], errors="coerce")
orders_raw.dropna(subset=["OrderTotal"], inplace=True)

# Status
orders_raw["Status"] = orders_raw["Status"].str.strip().str.lower()
orders_raw["Status"] = orders_raw["Status"].replace({"invalid": "unknown"})

# Merge
restaurant_df = pd.merge(customers_raw, orders_raw, left_on="CustID", right_on="ID", how="left")
restaurant_df.drop("ID", axis=1, inplace=True)

print(restaurant_df.to_string())
