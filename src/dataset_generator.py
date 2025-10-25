import csv
import random

# Initialize list to hold generated data
data = []

# Generates Sample data for resumes, job descriptions and fit scores
for i in range(500):
    resume_text = f"Resume content {i}"
    job_text = f"Job description content {i}"
    fit_score = random.uniform(0, 1)
    data.append({
        'resume_text': resume_text,
        'job_text': job_text,
        'fit_score': fit_score
    })

# Writes generated data to a CSV file
with open('data_raw/generated_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['resume_text', 'job_text', 'fit_score']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
