# Membership Subscription Data Cleaning

Goal: Clean user sign-up data by fixing email issues, standardizing names, parsing dates, and removing malformed entries.

1. Cleans messy DataFrame
2. Fixes names
3. Handles invalid emails
4. Removes invalid entries
5. Parses dates
6. Validates fields
7. .str.strip(), .str.lower(), .str.title(), .str.replace(), .str.endswith()
8. Regex
9. Invalidates ages under 10 and over 100
10. Turn empty strings into 'None' then replacing 'None' with 'inactive'
11. Status can only either be 'active' or 'inactive'. If not 'active' then 'inactive'

Output
See 'sample_output.txt'
