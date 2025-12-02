import pandas as pd

df = pd.DataFrame({
    "Name": [" Charizard", "charizard ", "BLASTOISE", None, "  pikAchu  ", "Pikachu", "venusaur ", "Venusaur", ""],
    "Type1": ["Fire", "FiRe", "Water", None, "Electric", " electric ", "Grass", "grass ", " Grass"],
    "Type2": ["Flying", "flying", None, "Poison", None, None, " Poison ", None, ""],
    "Power": [534, 534, 530, None, 320, 320, 525, 525, 525]
})

df["Name"] = df["Name"].str.strip().str.lower().str.capitalize() # Fix weird spellings
df["Type1"] = df["Type1"].str.strip().str.lower().str.capitalize() # Fix weird spellings
df["Type2"] = df["Type2"].str.strip().str.lower().str.capitalize() # Fix weird spellings
df.drop_duplicates(subset=["Name"], inplace=True) # Drop duplicate Pokemon (after fixing weird spellings so spellings can match)
df.replace('', None, inplace=True) # Replace any "" with None
df.dropna(subset=["Name", "Type1"], inplace=True) # Drop any row with None

print(df.to_string())
