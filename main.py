import os

print("--- Starting EPL Data Pipeline ---")

# We will run the BigQuery script directly
os.system('python push_to_bigquery.py')

print("--- Pipeline Execution Finished ---")