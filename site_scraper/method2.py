


import requests

def google_search(api_key, cx, query, num_results=10):
    search_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cx,
        'q': query,
        'num': num_results
    }
    
    response = requests.get(search_url, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors
    results = response.json()
    
    urls = [item['link'] for item in results.get('items', [])]
    return urls

# Example values
api_key = 'AIzaSyAcAEBKiph3QXKN7j7CRizMh0cZXrntO48'
cx = 'b3ff3b4c190694914'  # Replace with your Custom Search Engine ID
query = 'inurl:facebook-agent'
urls = google_search(api_key, cx, query)

# Print all URLs
for url in urls:
    print(url)    