import requests
from bs4 import BeautifulSoup

# Add the url
url = 'https://www.flipkart.com/search?q=mobile+phone+5g'
# Make a request to the website
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)
# Find and extract specific elements from the HTML
title = soup.title.text
print('Page title:\n', title)

# Make a request to the website
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# # print(response)

# text = soup.get_text()
# # print(text)

# # links = soup.find_all('a')
# # print('Links:')
# # for link in links:
# #     print(link.get('href'))


# start_word = "Reviews"
# end_word = "ROM"
# start_index = text.find(start_word)
# end_index = text.find(end_word, start_index + len(start_word))
# RAM_ROM = ''
# if start_index != -1 and end_index != -1:
#     RAM_ROM = text[start_index + len(start_word):end_index].strip()

# print(RAM_ROM)


# start_word = "GB)"
# end_word = "Ratings"
# start_index = text.find(start_word)
# end_index = text.find(end_word, start_index + len(start_word))
# Rating_Sold = ''
# if start_index != -1 and end_index != -1:
#     Rating_Sold = text[start_index + len(start_word):end_index].strip()

# print(Rating_Sold)


# import re

# start_word = "Add to Compare"
# end_word = "("

# escaped_start_word = re.escape(start_word)
# escaped_end_word = re.escape(end_word)

# pattern = f"{escaped_start_word}(.*?){escaped_end_word}"
# matches = re.finditer(pattern, text)
# name = []

# for match in matches:
#     project = match.group(1).strip()
#     name.append(project)

# print(name)

# modified_RAM_ROM = [element if '|' in element else '0 GB RAM | ' + element for element in RAM_ROM]

# print(modified_RAM_ROM)

# RAM = [element.split(" | ")[0] for element in modified_RAM_ROM]
# ROM = [element.split(" | ")[1] for element in modified_RAM_ROM]

# print(RAM)
# print(ROM)