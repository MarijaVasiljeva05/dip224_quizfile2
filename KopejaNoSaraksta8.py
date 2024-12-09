import pandas as pd
csv_file_path = 'data.csv'
data = pd.read_csv(csv_csv_file_path)
mining_data = data[data['industry'] == 'Mining']
value_list_mining = mining_data['value'].tolist()
average_value_mining = round(sum(value_list_mining) / len(value_list_mining))
average_value_mining_int = int(average_value_mining)
print("The avarege value for the Mining industry is: {average_value_mining_int}")