import os

print("--- Starting EPL Data Pipeline ---")

# Step 1: Push latest data to BigQuery
print("Running data loading script...")
os.system('python push_to_bigquery.py')

# Step 2: Generate AI summary from the new data
print("\nRunning AI summary script...")
os.system('python generate_summary.py')

print("\n--- Pipeline Execution Finished ---")
