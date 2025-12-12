import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Region": [" east", "East ", "WEST", "West", "north", "North", None],
    "Employee": ["alice", " Bob ", "CARL", "dana", "Evan", None, "Temp"],
    "Sales": ["120000", "90000 ", None, "75000", "50000", "65000", "30000"],
    "HoursWorked": ["160", "150", "140", None, "120", "130", "100"]
})

def clean_column(x):
    return x.str.strip().str.lower().str.title().str.replace(r"\s+", " ", regex=True)

def numeric_conversion(x):
    return pd.to_numeric(x, errors="coerce")

try:
    # Clean Region (strip whitespace, normalize to title case)
    df["Region"] = clean_column(df["Region"])

    # Clean Employee
    df["Employee"] = clean_column(df["Employee"])
    df["Employee"] = df["Employee"].replace({"Temp": None})

    # Convert "Sales" and "HoursWorked" to numeric
    df["Sales"] = numeric_conversion(df["Sales"])
    df["HoursWorked"] = numeric_conversion(df["HoursWorked"])

    # Drop missing "Region" and "Employee" rows
    df.dropna(subset=["Region", "Employee"], inplace=True)

    # Replace missing "Sales" with the median "Sales"
    df["Sales"] = df["Sales"].fillna(df["Sales"].median())

    # Replace missing "HoursWorked" with 0
    df["HoursWorked"] = df["HoursWorked"].fillna(0)

    df = df.groupby("Region").apply(
        lambda r: r.assign(
            SalesRank=r["Sales"].rank(ascending=False, method="first").astype("int64"),
            Efficiency=(r["Sales"] / r["HoursWorked"]).replace([np.inf, -np.inf], 0)
        ).sort_values(["SalesRank", "Efficiency"], ascending=[True, False]),
        include_groups=False
    ).copy()
except Exception as e:
    print(f"An error has occurred: {e}")

print(df.to_string())
