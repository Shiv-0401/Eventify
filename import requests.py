import requests
from bs4 import BeautifulSoup
import re

# Making a GET request
r = requests.get('https://newbrunswick.rutgers.edu/events')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', class_='events-list')
content = s.find_all('p')

pattern = r'(?P<date>.*?,\s*\d{4}),\s*(?P<start_time>.*?)\s*-\s*(?P<end_time>.*?)\s*\|\s*(?P<event>.*)'

# Processing each item in the content
for item in content:
    # Extracting date, start time, end time, and event description using regular expressions
    match = re.match(pattern, item.get_text(strip=True))
    if match:
        date = match.group('date')
        start_time = match.group('start_time')
        end_time = match.group('end_time')
        event_description = match.group('event')
        print("Date:", date)
        print("Start Time:", start_time)
        print("End Time:", end_time)
        print("Event:", event_description)
        print()