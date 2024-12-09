import pandas as pd
csv_file_path ='data.csv'
data = pd.read_csv(csv_file_path)
agriculture_data = data[data['industry'] == 'Agriculture']
value_list_agriculture = agriculture_data['value'].tolist()
every_second_element = value_list_agriculture[::2]
sum_of_every_second_element = sum(every_second_element)
print(f"The sum of every second element is: {sum_of_second_element}")