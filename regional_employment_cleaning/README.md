# Regional Employment Data Cleaning

Goal: Clean one messy DataFrame, add two columns, use helper functions, use groupby(), use apply(), and use assign().

1. Strip whitespace
2. Convert numerical strings to numeric (Sales & HoursWorked)
3. Fix capitalization
4. Drop missing "Region" and "Employee" rows
5. Replace missing "Sales" with the median "Sales"
6. Replace missing "HoursWorked" with 0
7. Group DataFrame by "Region"
8. Use .assign() to create two columns (SalesRank & Efficiency)
9. Sort "SalesRank" as ascending and "Efficiency" as descending
10. Use helper functions (clean_column() & numeric_conversion())

Ouput
See 'sample_output.txt'
