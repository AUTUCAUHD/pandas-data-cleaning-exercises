import pandas as pd
import numpy as np

employees = pd.DataFrame({
    "EmpID": [" 101", "102 ", "103", "104", None, "105"],
    "Employee": ["alice ", "BOB", " Cara", "dan", "Temp", "eva"],
    "Department": [" sales", "Sales ", "IT", "it ", "HR", None]
})

sales = pd.DataFrame({
    "EmployeeID": [101, 102, 103, 103, 104, 105],
    "DealsClosed": ["12", "18", "9", None, "25", "15"],
    "Revenue": ["60000", "85000", "45000", "30000", "120000", None]
})

time_tracking = pd.DataFrame({
    "EmpID": [101, 102, 103, 104, 105],
    "HoursWorked": ["160", "170", "150", None, "140"]
})

def convert_to_numeric(x):
    return pd.to_numeric(x, errors="coerce")

def clean_column(x):
    return x.str.strip().str.lower().str.title().str.replace(r"\s+", " ", regex=True)

# Fix Employee names and Department names
employees["Employee"] = clean_column(employees["Employee"])
employees["Department"] = clean_column(employees["Department"])
employees["Department"] = employees["Department"].str.upper()

# Convert to numeric
employees["EmpID"] = convert_to_numeric(employees["EmpID"])
sales["DealsClosed"] = convert_to_numeric(sales["DealsClosed"])
sales["Revenue"] = convert_to_numeric(sales["Revenue"])
time_tracking["HoursWorked"] = convert_to_numeric(time_tracking["HoursWorked"])

# Invalidate "Temp"
employees["Employee"] = employees["Employee"].replace("Temp", None)

# Drop null rows
employees.dropna(inplace=True)

# Aggregate "sales" to avoid duplicates
sales_agg = sales.groupby("EmployeeID").agg(
    DealsClosed=("DealsClosed", "sum"),
    Revenue=("Revenue", "sum")
).reset_index()

# Merge Datasets
first_merge = pd.merge(employees, sales_agg, how="left", left_on="EmpID", right_on="EmployeeID")
first_merge.drop("EmployeeID", axis=1, inplace=True)

full_df = pd.merge(first_merge, time_tracking, how="left", on="EmpID")

# Null DealsClosed turned to 0
full_df["DealsClosed"] = full_df["DealsClosed"].fillna(0)

# Empty HoursWorked converted to median
full_df["HoursWorked"] = full_df["HoursWorked"].fillna(full_df["HoursWorked"].median())

# Create RevenuePerHour
full_df["RevenuePerHour"] = (full_df["Revenue"] / full_df["HoursWorked"]).replace([np.inf, -np.inf], 0)

# Create DealsPerHour
full_df["DealsPerHour"] = (full_df["DealsClosed"] / full_df["HoursWorked"]).replace([np.inf, -np.inf], 0)

# Create DeptAvgRevenue (Track average revenue of each department)
full_df["DeptAvgRevenue"] = full_df.groupby("Department")["Revenue"].transform("mean")

full_df = full_df.groupby("Department").apply(
    lambda d: d.assign(
        RankInDept=d["Revenue"].rank(ascending=False, method="first").astype("int64"),
        TopPerformer=lambda p: np.where(p["RankInDept"] == 1, "Yes", "No")
    ).sort_values("RankInDept"),
    include_groups=False
).copy()

print(full_df.to_string())
