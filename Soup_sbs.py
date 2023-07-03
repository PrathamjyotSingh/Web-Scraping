import requests
from bs4 import BeautifulSoup

# Add the url
url = 'https://sbssu.ac.in/dptArch.aspx?Id=9'
# Make a request to the website
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)
# Find and extract specific elements from the HTML
title = soup.title.text
print('Page title:\n', title)


print(soup.get_text())

# Find all the links on the page
# links = soup.find_all('a')
# print('Links:')
# for link in links:
#     print(link.get('href'))