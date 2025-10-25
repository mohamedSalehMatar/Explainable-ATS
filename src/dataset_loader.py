import pandas as pd
from sklearn.model_selection import train_test_split

# Intialize dataset path
path='data_raw/generated_data.csv'

# Load dataset into a DataFrame
raw_df = pd.read_csv(path)

# Display the DataFrame
print(raw_df.head()) 

# using the train test split function
X= raw_df[['resume_text', 'job_text']]
y= raw_df['fit_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                   random_state=104, 
                                   test_size=0.25, 
                                   shuffle=True)

# printing out train and test sets
print('X_train : ')
print(X_train.head())
print('')
print('X_test : ')
print(X_test.head())
print('')
print('y_train : ')
print(y_train.head())
print('')
print('y_test : ')
print(y_test.head())