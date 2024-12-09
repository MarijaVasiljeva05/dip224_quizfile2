import pandas as pd
file_path = 'EmployeeData.xlsx'
employee_data = pd.read_excel(file_path)
sales_employees = employee_data[employee_data['Department'] == 'Sales']
average_age_sales = round(sales_employees['Age'].mean())
averange_age_sales_int = int(average_age_sales)
print(f"The average age of employees in the sales department is: {average_age_sales_int}")