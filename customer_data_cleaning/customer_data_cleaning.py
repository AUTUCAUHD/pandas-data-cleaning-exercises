import pandas as pd
import numpy as np

df = pd.DataFrame({
    "CustomerID": [" 101", "102 ", "103", None, " 104", "105 ", "  "],
    "Name": ["john doe", " Jane SMITH ", "ALICE brown", "Bob", None, "mArY  jOnEs", ""],
    "Email": ["JOHN@EXAMPLE.COM", "jane@example.com ", None, "bob@", "alice@example.com", "MARY@EXAMPLE.COM", ""],
    "City": [" miami", "New YORK ", "los angeles", None, " CHICAGO", "new york", ""],
    "SignupDaysAgo": ["10", " 25 ", None, "five", "40", "15", ""]
})

# ID FIX
# Strip whitespace
df["CustomerID"] = df["CustomerID"].str.strip().str.replace(r"\s+", " ", regex=True)

# Convert to numeric
df["CustomerID"] = pd.to_numeric(df["CustomerID"], errors="coerce")


# NAME FIX
# Strip whitespace & Fix capitalization
df["Name"] = df["Name"].str.strip().str.lower().str.title().str.replace(r"\s+", " ", regex=True)


# EMAIL FIX
# Lowercase all emails
df["Email"] = df["Email"].str.lower()

# Invalidate emails missing "@"
df = df[df["Email"].str.contains("@", na=False)].copy()

# Invalidate emails starting with or ending with "@"
df = df[(~df["Email"].str.startswith("@", na=False)) &
        (~df["Email"].str.endswith("@", na=False))].copy()


# CITY FIX
# Strip whitespace & Fix capitalization
df["City"] = df["City"].str.lower().str.title().str.strip().str.replace(r"\s+", " ", regex=True)


# SIGNUPDAYSAGO FIX
# Convert to numeric
df["SignupDaysAgo"] = pd.to_numeric(df["SignupDaysAgo"], errors="coerce")

# Replace missing values with the column median
df["SignupDaysAgo"] = df["SignupDaysAgo"].fillna(df["SignupDaysAgo"].median())


# Drop missing rows
df.replace("", np.nan, inplace=True)
df.dropna(subset=["CustomerID", "Name", "Email", "City"], inplace=True)

# Save to CSV file
df.to_csv("file.csv", index=False)

print(df.to_string())
