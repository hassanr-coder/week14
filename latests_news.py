'''
Rayaan Hassan
CMSC 111
Spring 2026
Week 14 Assignment 2
Code Helped: Gemini Ai
'''
import os
import requests

def fetch_latest_news():
    # 1. Store API Key Safely (Task 1)
    # Using Option A: Environment Variable
    api_key = os.getenv("NEWS_API_KEY")
    
    if not api_key:
        print("API key not found. Please set your API key.")
        return

    # API Configuration (NewsAPI.org)
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "us",
        "pageSize": 10,  # Request at least 10 headlines (Task 2.2)
        "apiKey": api_key
    }

    try:
        # 2. Fetch Latest Headlines (Task 2)
        response = requests.get(url, params=params)
        
        # Check that request succeeded (HTTP 200) (Task 2.3)
        if response.status_code != 200:
            print(f"Error: Request failed with status code {response.status_code}")
            return

        # 3. Parse JSON (Task 4)
        data = response.json()
        articles = data.get("articles", [])

        # Handle "No articles returned" (Task 4)
        if not articles:
            print("No articles returned.")
            return

        # 4. Print Headline + Publication Date (Task 3)
        print("--- Latest News Headlines ---")
        for i, article in enumerate(articles, 1):
            title = article.get("title")
            published_at = article.get("publishedAt")
            
            # Format according to required output: 1. Headline: <title> Published: <date>
            print(f"{i}. Headline: {title} Published: {published_at}")

        print(f"\nTotal headlines printed: {len(articles)}")

    except requests.exceptions.RequestException as e:
        # Handle Request fails (Task 4)
        print(f"An error occurred while fetching data: {e}")
    except ValueError:
        # Handle JSON parsing issues (Task 4)
        print("Error: Could not parse JSON response.")

if __name__ == "__main__":
    fetch_latest_news()