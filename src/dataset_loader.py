import pandas as pd

# Intialize dataset path
path='data_raw/generated_data.csv'

# Load dataset into a DataFrame
raw_df = pd.read_csv(path)

# Display the DataFrame
print(raw_df.to_string()) 