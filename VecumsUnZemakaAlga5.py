import pandas as pd
file_path = 'EmployeeData.xlsx'
employee_data = pd.read_excel(file_path)
lowest_salary_employee = employee_data[employee_data['Annual Salary'] == emploee_data['Annual Salary'].min()]
age_of_lowest_salary_employee = lowest_salary_employee['Age'].iloc[0]
print(f"The age of the employee with the lowest salary is: {age_of_lowest_salary_employee}")