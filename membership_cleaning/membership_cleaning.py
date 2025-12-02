import pandas as pd

df = pd.DataFrame({
    "Name": ["  john doe", "JOHN DOE ", "Jane Smith", " jane  smith ", None, "Carlos0 Diaz", "Carlos Diaz", "Anna", "Anna ", "   "],
    "Email": ["john@example.com", "JOHN@example.Com", "jane.smith@", None, "invalid.email", "carlos@diaz.com", "carlos@diaz.com", "anna@example.com", "", "anna@example.com"],
    "Age": ["29", "29", "  34 ", None, "??", "41", "41", "19", "19", "19"],
    "SignUpDate": ["2022-01-04", "2021/1/4", "04-01-2022", "2022-13-04", None, "2020-07-12", "2020/07/12", "07/12/20", "2020.07.12", ""],
    "Membership": ["  aCtIve  ", "Active ", "ACTIVE", "inactive", None, "active", "active", " trial", "Trial ", ""]
})

# Fix Name Column
df["Name"] = df["Name"].str.strip().str.lower().str.title().str.replace(r'\s+', ' ', regex=True).str.replace(r'\d*', '', regex=True)
df.replace('', None, inplace=True)
df.drop_duplicates(subset=["Name"], inplace=True)
df.dropna(subset=["Name"], inplace=True)

# Fix Email Column
df["Email"] = df["Email"].str.lower()
df = df[~df["Email"].str.endswith('@')] # Selects rows that do not have emails ending with '@'
df.dropna(subset=["Email"], inplace=True)

# Fix Age Column
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df = df[(df["Age"] > 10) & (df["Age"] < 100)]
df["Age"].fillna(df["Age"].median())

# Clean SignUpDate
df["SignUpDate"] = pd.to_datetime(df["SignUpDate"], errors="coerce")
df.dropna(subset=["SignUpDate"], inplace=True)

# Fix Membership column
df["Membership"] = df["Membership"].str.strip().str.lower()
df["Membership"] = df["Membership"].replace({"": None})
df["Membership"] = df["Membership"].replace({None: "inactive"})
df.loc[~df["Membership"].isin(["active", "inactive"]), "Membership"] = "inactive" # Locates index where the condition is met then turns it to inactive

print(df.to_string())
