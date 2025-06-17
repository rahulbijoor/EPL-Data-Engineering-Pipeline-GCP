import requests
from bs4 import BeautifulSoup
import pandas as pd

def league_table():
    """Scrapes the EPL league table from BBC Sport."""
    print("Scraping league_table from BBC Sport...")
    url = 'https://www.bbc.com/sport/football/premier-league/table'

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    table = soup.find("table", attrs={"data-testid": "standings-table"})

    # Get the table headers
    headers = []
    for i in table.find_all('th'):
        title = i.text.strip()
        headers.append(title)

    # Create a pandas DataFrame
    df = pd.DataFrame(columns=headers)

    # Get the table rows
    for j in table.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [i.text.strip() for i in row_data]
        length = len(df)
        df.loc[length] = row

    print("Successfully scraped league_table.")
    return df

def top_scorers():
    """Scrapes the EPL top scorers from BBC Sport."""
    print("Scraping top_scorers from BBC Sport...")
    url = 'https://www.bbc.com/sport/football/premier-league/top-scorers'
    
    # ... add your scraping logic here ...
    
    # Create and return a pandas DataFrame
    # df_scorers = ...
    
    # print("Successfully scraped top_scorers.")
    # return df_scorers
    
    # For now, let's return a placeholder until you implement it
    return pd.DataFrame() 