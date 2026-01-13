import requests
import csv

def fetch_and_print_posts():
    """Fetches posts from JSONPlaceholder and prints the titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    # Print the status code: Status Code: 200
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))

def fetch_and_save_posts():
    """Fetches posts and saves them into a CSV file called posts.csv."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        
        # Structure the data for CSV
        structured_data = [
            {'id': p['id'], 'title': p['title'], 'body': p['body']}
            for p in posts
        ]
        
        # Writing to CSV
        with open('posts.csv', mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(structured_data)
