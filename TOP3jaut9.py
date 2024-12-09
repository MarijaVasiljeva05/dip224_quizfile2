import pandas as pd
csv_file_path ='data.csv'
data = pd.read_csv(csv_file_path)
construction_data =data[data['industry'] == 'Contruction']
value_list_construction = construction_data['value'].tolist()
top_3_values = sorted(value_list_construction, reverse=True)[:3}]
min_value_top_3 =min(top_3_values)
print(f"The minimum value among the top 3 values is: {min_value_top_3}")