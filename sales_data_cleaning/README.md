# Sales Data Cleaning

Goal: Clean and merge three messy DataFrames, add columns, use helper functions, use groupby(), use apply(), use assign(), use transform(), use agg().

1. Strip whitespace
2. Convert numerical strings to numeric (EmpID, DealsClosed, Revenue, HoursWorked)
3. Fix capitalization
4. Replace missing "HoursWorked" with median
5. Drop missing or "Temp" employees
6. Aggregate "sales" to avoid having to drop duplicates
7. Merge "employees" and "sales_agg" dataframes
8. Merge "time_tracking" dataframe with merged "employees" and "sales_agg" dataframes
9. Create "RevenuePerHour" column
10. Create "DealsPerHour" column
11. Create "DeptAvgRevenue" column with groupby().transform()
12. Group dataframe by each Department and create "RankInDept" and "TopPerformer" columns with .assign()

Output
See 'sample_output.txt'
