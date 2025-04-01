'''
How can I perform the following operations on the given employee table:
'''
import pandas as pd

# Create the DataFrame
data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['John Smith', 'Alice Brown', 'Bob White', 'Emma Green', 'Charlie Red'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
    'Age': [30, 28, 35, 40, 25],
    'Salary': [70000, 60000, 80000, 90000, 55000],
    'JoinDate': ['2018-07-15', '2020-03-10', '2016-11-01', '2012-05-25', '2021-06-01'],
    'ExperienceYears': [5, 3, 7, 11, 2]
}

df = pd.DataFrame(data)

# a. Write a query to select only the Name and Salary columns
selected_columns = df[['Name', 'Salary']]
print("a. Name and Salary columns:\n", selected_columns)

# b. Filter out all employees in the "IT" department
it_employees = df[df['Department'] != 'IT']
print("\nb. Employees not in IT department:\n", it_employees)

# c. Select employees who are older than 30 and find the average salary of employees in each department
older_than_30 = df[df['Age'] > 30]
average_salary = older_than_30.groupby('Department')['Salary'].mean()
print("\nc. Employees older than 30 and average salary in each department:\n", average_salary)

# d. Count the number of employees in each department
employee_count = df['Department'].value_counts()
print("\nd. Number of employees in each department:\n", employee_count)

# e. Add a new column Bonus which is 10% of each employee's salary
df['Bonus'] = df['Salary'] * 0.10
print("\ne. DataFrame with Bonus column:\n", df)

# f. Replace all occurrences of "HR" in the Department column with "Human Resources."
df['Department'] = df['Department'].replace('HR', 'Human Resources')
print("\nf. DataFrame with HR replaced by Human Resources:\n", df)

# g. Find the employee(s) with the longest tenure (based on JoinDate)
df['JoinDate'] = pd.to_datetime(df['JoinDate'])  # Convert JoinDate to datetime format
longest_tenure = df[df['JoinDate'] == df['JoinDate'].min()]
print("\ng. Employee(s) with the longest tenure:\n", longest_tenure)

# h. Create a new column SalaryCategory where salaries above 75,000 are categorized as "High" and the rest as "Low."
df['SalaryCategory'] = df['Salary'].apply(lambda x: 'High' if x > 75000 else 'Low')
print("\nh. DataFrame with SalaryCategory column:\n", df)

# i. Check if there are any duplicate EmployeeIDs and remove them if found
df_no_duplicates = df.drop_duplicates(subset=['EmployeeID'])
print("\ni. DataFrame without duplicate EmployeeIDs:\n", df_no_duplicates)

# j. Calculate the median Age of all employees
median_age = df['Age'].median()
print("\nj. Median Age of all employees:", median_age)
