import pandas as pd
from sklearn.model_selection import train_test_split

import kagglehub

# Intialize dataset 
path = kagglehub.dataset_download("gauravduttakiit/resume-dataset") + "/UpdatedResumeDataSet.csv"
print("Path to dataset files:", path)

# Load dataset into a DataFrame
raw_df = pd.read_csv(path)

# Display the DataFrame
print(raw_df.head())
