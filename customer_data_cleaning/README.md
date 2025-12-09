# Customer Data Cleaning

Goal: Clean one messy DataFrame then save to CSV file

1. Strip whitespace
2. Convert numerical strings to numeric (CustomerID & SignupDaysAgo)
3. Fix capitalization
4. Lowercase all emails
5. Invalidate emails missing "@"
6. Invalidate emails starting with "@"
7. Invalidate emails ending with "@"
8. Replace missing values in "SignupDaysAgo" with the column median
9. Drop missing rows
10. Save to CSV file

Output
See 'sample_output.txt'
