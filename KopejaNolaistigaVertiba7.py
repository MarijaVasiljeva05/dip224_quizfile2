import pandas as pd
csv_file_path ='data.csv'
data = pd.read_csv(csv_file_path)
filtered_data = data[data['line_code'] == 'C0300.02']
value_list_filtered = filtered_data['value'].tolist()
total_values_count = len(value_list_filtered)
print(f"The total number of values where the line_code is 'C0300.02' is: {total_values_count}")