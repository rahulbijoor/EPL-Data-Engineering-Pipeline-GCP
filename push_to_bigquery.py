from scrape import league_table, top_scorers # Add other functions as you create them
from pandas_gbq import to_gbq
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
PROJECT_ID = os.getenv('GCP_PROJECT_ID')
DATASET_ID = "epl_analytics" # The name of your BigQuery dataset

functions = [league_table, top_scorers] # Add other functions here

print("Starting BigQuery load process...")
"""for func in functions:
    table_name = func.__name__
    df = func()
    print(f"Loading data for {table_name}...")
    to_gbq(
        dataframe=df,
        destination_table=f"{DATASET_ID}.{table_name}",
        project_id=PROJECT_ID,
        if_exists='replace'
    )
print("BigQuery load process complete.")
"""
for func in functions:
    table_name = func.__name__
    df = func()

    # ADD THIS CHECK
    if df is not None and not df.empty:
        print(f"Loading data for {table_name}...")
        # ... to_gbq call ...
    else:
        print(f"Skipping {table_name} 