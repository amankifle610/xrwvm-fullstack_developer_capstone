import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set default backend and sentiment analyzer URLs
backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv('sentiment_analyzer_url', default="http://localhost:5050/")

# Function to make GET requests to the backend
def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params += key + "=" + value + "&"

    request_url = backend_url + endpoint + "?" + params

    print(f"GET from {request_url}")
    try:
        # Call GET method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        # Catch any exception and print error details
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")

# Function to analyze review sentiments
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        # Call GET method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        # Catch any exception and print error details
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")

# Function to post a review
def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        # Call POST method of requests library with JSON payload
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as err:
        # Catch any exception and print error details
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
