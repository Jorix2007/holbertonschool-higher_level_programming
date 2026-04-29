import requests
import csv

def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder.
    Prints the status code and all post titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    # Print the status code of the response
    print(f"Status Code: {response.status_code}")
    
    # If the request is successful (Status Code 200), parse and print titles
    if response.status_code == 200:
        posts = response.json()  # Parses the fetched data into a Python list of dictionaries
        for post in posts:
            print(post.get("title"))

def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder.
    Extracts id, title, and body, and saves them to a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    # If the request is successful, proceed to save data
    if response.status_code == 200:
        posts = response.json()
        
        # Structure the data using a list comprehension
        data_to_save = [
            {"id": post.get("id"), "title": post.get("title"), "body": post.get("body")}
            for post in posts
        ]
        
        # Write the structured data to a CSV file
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as csv_file:
            fieldnames = ["id", "title", "body"]
            
            # csv.DictWriter is perfect for writing lists of dictionaries
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            writer.writeheader()  # Writes the column names
            writer.writerows(data_to_save)  # Writes all the rows of data
