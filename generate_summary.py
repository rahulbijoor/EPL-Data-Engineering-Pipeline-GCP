import os
import pandas as pd
from pandas_gbq import read_gbq
from dotenv import load_dotenv
import google.generativeai as genai

# --- Configuration ---
load_dotenv()
PROJECT_ID = os.getenv('GCP_PROJECT_ID')
DATASET_ID = "epl_analytics"
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Configure the Gemini client
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def get_data_from_bigquery():
    """Queries the necessary tables from BigQuery and returns them as DataFrames."""
    print("Fetching data from BigQuery...")
    
    # Query for the league table, ordering by position
    # The 'Pos' column might be a string, so we cast it to an integer for correct sorting
    sql_league_table = f"SELECT * FROM `{PROJECT_ID}.{DATASET_ID}.league_table` ORDER BY CAST(Pos AS INT64) ASC"
    df_table = read_gbq(sql_league_table, project_id=PROJECT_ID)

    # Query for the top scorers
    sql_top_scorers = f"SELECT * FROM `{PROJECT_ID}.{DATASET_ID}.top_scorers` LIMIT 10"
    df_scorers = read_gbq(sql_top_scorers, project_id=PROJECT_ID)
    
    print("Data fetched successfully.")
    return df_table, df_scorers

def generate_epl_summary():
    """Generates a weekly EPL summary using Gemini Pro."""
    df_table, df_scorers = get_data_from_bigquery()

    # --- Create the Prompt for the AI ---
    # Convert dataframes to a string format that's easy for the LLM to read
    table_str = df_table.to_string(index=False)
    scorers_str = df_scorers.to_string(index=False)

    prompt = f"""
    You are a knowledgeable and engaging sports analyst for the English Premier League.
    Based on the following data, please provide a concise and insightful summary of the current league standings and the top scorer race.

    Your summary should:
    1.  Mention the team at the top of the table and their points.
    2.  Briefly comment on the top 4 teams (the Champions League spots).
    3.  Mention one or two interesting details from the table (e.g., a team that is surprisingly high or low).
    4.  Name the current top goal scorer and their number of goals.
    5.  Maintain a professional and engaging tone.

    Here is the data:

    **Current League Table:**
    {table_str}

    **Top Goal Scorers:**
    {scorers_str}

    **Your Analysis:**
    """

    print("Sending prompt to Gemini Pro...")
    response = model.generate_content(prompt)
    
    print("\n--- AI-Generated EPL Weekly Summary ---")
    print(response.text)
    print("---------------------------------------\n")

if __name__ == "__main__":
    generate_epl_summary()