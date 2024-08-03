import re
import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode


items_to_skip = ['info@','.png','.jpg','support@']
websites_limit = 2000
keyword_to_search = 'facebook-agency'


def extract_between(text, start_str, end_str):
    start_index = text.find(start_str)
    if start_index == -1:
        return None
    start_index += len(start_str)
    end_index = text.find(end_str, start_index)
    if end_index == -1:
        return None
    return text[start_index:end_index]

def contains_any(string, values):
    return any(value in string for value in values)  

def extract_emails(text):
    
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    final = []
    
    emails = re.findall(email_pattern, text)
    for email in emails:
        if  not contains_any(email,items_to_skip):
            final.append(email)
    return final

   

def get_emails_from_site(site):

    try:
        response = requests.get(site, timeout=10)
        return(extract_emails(response.text))

    except:
        pass

        


def google_search_scrape(query):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    params = {
        'q': query,
        'num': websites_limit,  
    }
    url = 'https://www.google.com/search?' + urlencode(params)
    response = requests.get(url, headers=headers)
    print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')

    results = []
    for item in soup.find_all('div', class_='egMi0 kCrYT'):
        title = item.get_text()
        link = item.find_next('a')['href']
        results.append((title, link))
    return results



results = google_search_scrape('inurl:{0}'.format(keyword_to_search))
all_emails = []
for title, link in results:
    try:
        for res in list(set(get_emails_from_site(extract_between(link,'&url=','&ved')))):
            print(res)
            if len(res)<50:
                all_emails.append([extract_between(link,'&url=','&ved'),res])
    except:
        pass

print(all_emails)

csv_file_path = 'output.csv'


with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(all_emails) 

print(f'List has been exported to {csv_file_path}')