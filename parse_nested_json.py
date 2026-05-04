'''
Rayaan Hassan
CMSC 111
Spring 2026
Week 14 Assignment 4
Code Helped: Gemini Ai
'''
import json

def parse_student_data():
    try:
        # 1 & 2. Open and load the local JSON file
        with open("nested_data.json", "r") as file:
            data = json.load(file)

        # 3. Extracting nested values
        # Navigate through dictionaries and lists
        student_name = data["student"]["name"]
        student_email = data["student"]["contact"]["email"]
        student_city = data["address"]["city"]
        
        # Accessing the list of courses
        # First course is index 0, Second course is index 1
        first_course_name = data["courses"][0]["course_name"]
        second_course_grade = data["courses"][1]["grade"]

        # Print using the required format
        print(f"Student Name: {student_name}")
        print(f"Email: {student_email}")
        print(f"City: {student_city}")
        print(f"First Course: {first_course_name}")
        print(f"Second Course Grade: {second_course_grade}")

    except (KeyError, IndexError, FileNotFoundError, json.JSONDecodeError):
        # 4. Required exact error message for missing/bad data
        print("Missing data in JSON file.")

if __name__ == "__main__":
    parse_student_data()