import pandas as pd
file_path = 'EmployeeData.xlsx'
employee_data = pd.read_excel(file_path)
it_employees = employee_data[employee_data['Department'] == 'IT']
max_age_it = it_employees['age'].max()
print(f"The maximum age of an employee in the IT department is: {max_age_it}")