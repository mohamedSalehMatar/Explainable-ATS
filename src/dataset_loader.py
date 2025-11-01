import pandas as pd
from sklearn.model_selection import train_test_split

import kagglehub

import os
from pypdf import PdfReader

# Downloading dataset from Kaggle
path = kagglehub.dataset_download("snehaanbhawal/resume-dataset")
print("Path to dataset files:", path)
it_resumes_path = path + r"\data\data\INFORMATION-TECHNOLOGY"
print("Path to IT resumes dataset files:", it_resumes_path)

# creating a pdf reader object
reader = PdfReader(os.path.join(it_resumes_path, os.listdir(it_resumes_path)[0]))

# printing number of pages in pdf file
print(len(reader.pages))

# getting a specific page from the pdf file
page = reader.pages[0]

# extracting text from page
text = page.extract_text()
print(text)
