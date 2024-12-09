import pandas as pd
file_path = 'EmployeeData.xlsx'
employee_data = pd.read_excel(file_path)
sales_employees = employee_data[emloyee_data['Department'] == 'sales']
num_sales_employees = sales_employees.shape[0]
print(f"Number of employees in the Sales department: {num_sales_emloyees}")