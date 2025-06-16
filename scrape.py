import requests
from bs4 import BeautifulSoup
import pandas as pd

def league_table():
    """Scrapes the EPL league table from BBC Sport."""
    # Your web scraping code will go here
    print("Scraping league_table...")
    # For now, return an empty DataFrame as a placeholder
    return pd.DataFrame({'team': ['Team A'], 'points': [0]})

# You will add more functions here (top_scorers, etc.)