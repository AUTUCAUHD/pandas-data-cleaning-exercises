import pandas as pd

df = pd.DataFrame({
    "team": ["A", "A", "A", "B", "B", "B", "B"],
    "month": ["Jan", "Jan", "Feb", "Jan", "Feb", "Feb", "Mar"],
    "sales": ["100", "120", "150", "80", None, "90", "110"]
})

# Convert sales column to numeric
df["sales"] = pd.to_numeric(df["sales"], errors="coerce")

# Pivot table and aggregation
df = pd.pivot_table(
    df,
    index="team",
    columns="month",
    values="sales",
    aggfunc=["mean", "sum"]
)

# Ordering months
month_order = ["Jan", "Feb", "Mar"]

df = df.reindex(columns=month_order, level=-1)

# Flattening columns
df.columns = [
    f"{agg}_{month}"
    for agg, month in df.columns
]

print(df.to_string())
