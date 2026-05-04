'''
Rayaan Hassan
CMSC 111
Spring 2026
Week 14 Assignment 1
Code Helped: Gemini Ai
'''
import requests

# 1. Define the URL
url = "https://jsonplaceholder.typicode.com/users/1"

try:
    # 2. Send a GET request to the API
    response = requests.get(url)

    # 3. Check that the request was successful
    # This will raise an exception for 4XX or 5XX status codes
    response.raise_for_status()

    # 4. Parse the returned JSON data
    user_data = response.json()

    # 5. Extract and print the user's name and email
    name = user_data.get("name")
    email = user_data.get("email")
    
    print(f"Name: {name} Email: {email}")

except requests.exceptions.HTTPError as http_err:
    # Handles specific HTTP errors (like 404 Not Found)
    print(f"HTTP error occurred: {http_err}")
except Exception as error:
    # Handles other errors (like connection issues or JSON parsing errors)
    print(f"An error occurred: {error}")
