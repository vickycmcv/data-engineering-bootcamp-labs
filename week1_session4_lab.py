import pandas as pd

# Data Understanding
# Load the dataset into a DataFrame called df.
df = pd.read_csv(r'../Activities/Week1/Files/nba.csv')

# Display the first 5 rows. 
first_5_rows = df.head()
print(first_5_rows)

# Check the number of rows and columns. 
df_shape = df.shape
print("Number of rows and columns: ",df_shape)

# List all column names. 
column_names = df.columns
print("Column names:")
print(column_names)

# Data Cleaning 
# Convert the Salary column to numeric (handle errors).
df1 = pd.to_numeric(df["Salary"], errors="coerce")

# Count how many missing (NaN) values are in each column. 
nan_count = pd.isnull(df1).sum()
print("Total of missing values: ",nan_count)

# Drop rows where Salary is missing.
df2 = df.dropna(subset=["Salary"])
print("Rows where Salary is missing deleted. Here the count of null:")
print(pd.isnull(df2).sum())

# Fill missing College values with "Unknown". 
df3 = df2.copy()
df3['College']=df3['College'].fillna("Unknown")
print("Missing College values with 'Unknown'. Here the count of null:")
print(pd.isnull(df3).sum())

#  Filtering Data
# Show all players from Boston Celtics. 
boston_celtics_players = df3[df3["Team"] == "Boston Celtics"]
print("Players from Boston Celtics:")
print(boston_celtics_players)

# Show players whose Age is greater than 30.
age_greater_30 = df3[df3["Age"] > 30]
print("Players whose Age is greater than 30:")
print(age_greater_30)

# Filter players who play as PG (Point Guard). 
pg_position_players = df3[df3["Position"] == "PG"]
print("Players who play as PG:")
print(pg_position_players)

# Find players with Salary greater than 5,000,000. 
salary_greater_5M = df3[df3["Salary"] > 5000000]
print("Players with Salary greater than 5,000,000:")
print(salary_greater_5M)

# Sorting
# Sort players by Salary (highest first). 
sorted_salary_desc = df3.sort_values("Salary", ascending=False)
print("Players sorted by salary desc:")
print(sorted_salary_desc)

# Sort players by Age (youngest first). 
sorted_age_asc = df3.sort_values("Age", ascending=True)
print("Players sorted by age asc:")
print(sorted_age_asc)

# GroupBy Operations 
# Find the average salary per team. 
df3_gruped_team = df3.groupby("Team")
df3_gruped_team_avg_salary = df3_gruped_team["Salary"].mean()
print("Average salary per team:")
print(df3_gruped_team_avg_salary)

# Count number of players in each team. 
df3_gruped_team_count_players = df3_gruped_team["Salary"].count()
print("Count number of players in each team:")
print(df3_gruped_team_count_players)

# Find the maximum salary in each team. 
df3_gruped_team_max_salary = df3_gruped_team["Salary"].max()
print("Maximum salary in each team:")
print(df3_gruped_team_max_salary)

# Aggregations
# What is the average age of players? 
avg_age = df3["Age"].mean()
print("Average age of players: ",avg_age)

# What is the maximum salary in the dataset? 
max_salary = df3["Salary"].max()
print("Maximum salary: ",max_salary)

# What is the minimum weight? 
min_weight = df3["Weight"].min()
print("Minimum weight: ", min_weight)

# Column Operations
# Create a new column Age_in_5_years.
df3["Age_in_5_years"]=df3["Age"]+5
print("new column Age_in_5_years added:")
print(df3.head())

# Create a new column Salary_in_Millions (Salary / 100000).
df3["Salary_in_Millions"] = df3["Salary"]/1000000 
print("new column Salary_in_Millions added:")
print(df3.head())

# Bonus 
# Which team has the highest total salary payout? 
df3_gb_team_sum_salary= df3.groupby("Team")["Salary"].sum()
df3_gb_team_sum_salary_highest = df3_gb_team_sum_salary.sort_values(ascending=False).iloc[:1]
print("Team with the highest total salary payout: ",df3_gb_team_sum_salary_highest)

# Which position has the highest average salary? 
df3_gb_pos_avg_salary = df3.groupby("Position")["Salary"].mean()
df3_gb_pos_avg_salary_highest = df3_gb_pos_avg_salary.sort_values(ascending=False).iloc[:1]
print("Position with the highest average salary: ",df3_gb_pos_avg_salary_highest)