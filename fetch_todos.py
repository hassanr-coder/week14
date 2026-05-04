'''
Rayaan Hassan
CMSC 111
Spring 2026
Week 14 Assignment 3
Code Helped: Gemini Ai
'''
import requests

# 1. Define the URL
url = "https://jsonplaceholder.typicode.com/todos"

try:
    # 2. Send a GET request to the API
    response = requests.get(url)

    # 3. Confirm the request was successful (status code 200)
    if response.status_code == 200:
        # 4. Parse the JSON response
        todos = response.json()

        # 5. Extract the "title" field from each task using a loop
        # We only need the first 20 task titles
        titles_to_print = todos[:20]
        
        count = 0
        for task in titles_to_print:
            count += 1
            title = task.get("title")
            # Print in numbered list format
            print(f"{count}. {title}")

        # Print the total number of titles printed
        print(f"\nTotal titles printed: {count}")
    
    else:
        # Handle request failure (non-200 response)
        print(f"Request failed. Status code: {response.status_code}")

except Exception as e:
    # Handle connection errors or other unexpected issues
    print(f"Request failed. Error: {e}")