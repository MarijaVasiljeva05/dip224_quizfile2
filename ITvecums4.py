import pandas as pd
file_path = 'EmployeeData.xlsx'
employee_data = pd.read_excel(file_path)
employees_in_salary_range = employee_data[(employee_data['Annual Salary'])]
num_employees_in_salary_range = employees_in_salary_range.shape[0]
print(f"The number of employees with a salary in the range 150,000 < salary < 200,000 is: {num_employees_in_salary_range}")