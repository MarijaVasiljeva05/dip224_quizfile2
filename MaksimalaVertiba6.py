import pandas as pd
csv_file_path = 'data.csv'
data = pd.read_csv(csv_file_path)
manufacturing_data = data[data['industry'] == 'Manufacturing']
value_list = manufacturing_data['value'].tolist()
max_value_manufacturing = max(value_list)
print(f"The maximum value in the 'value' column for the Manufacturing industry is:{max_value_manufacturing}")