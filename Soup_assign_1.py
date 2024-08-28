import requests
from bs4 import BeautifulSoup
import pandas as pd

# Initialize the DataFrame
df = pd.DataFrame(columns=[
    'book_name', 'publisher', 'language', 'paperback', 
    'isbn_10', 'isbn_13', 'weight', 'dimensions', 'first_three_reviews'
])

# Function to get book details from the book's detail page
def get_book_details(book_link):
    response = requests.get(book_link)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    details = {}
    
    # Extracting the book name
    book_name = soup.find('span', attrs={'id': 'productTitle'})
    details['book_name'] = book_name.text.strip() if book_name else 'NaN'
    
    # Extracting the product details from the "Product Details" section
    product_details = soup.find('div', {'id': 'detailBullets_feature_div'})
    if product_details:
        for li in product_details.find_all('li'):
            text = li.text.strip()
            if 'Publisher' in text:
                details['publisher'] = text.split(':')[-1].strip()
            elif 'Language' in text:
                details['language'] = text.split(':')[-1].strip()
            elif 'Paperback' in text:
                details['paperback'] = text.split(':')[-1].strip()
            elif 'ISBN-10' in text:
                details['isbn_10'] = text.split(':')[-1].strip()
            elif 'ISBN-13' in text:
                details['isbn_13'] = text.split(':')[-1].strip()
            elif 'Weight' in text:
                details['weight'] = text.split(':')[-1].strip()
            elif 'Dimensions' in text:
                details['dimensions'] = text.split(':')[-1].strip()
    
    # Extracting the first three customer reviews
    reviews = soup.find_all('div', {'data-hook': 'review'})
    customer_reviews = [review.find('span', {'data-hook': 'review-body'}).text.strip() for review in reviews[:3]]
    details['first_three_reviews'] = customer_reviews if customer_reviews else 'NaN'
    
    return details

# Function to get values from a URL and append them to the DataFrame
def get_data(pageno):
    url = f'https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_{pageno}_books?ie=UTF8&pg={pageno}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    for d in soup.find_all('div', attrs={'class': "zg-grid-general-faceout"}):
        book_link = d.find('a', attrs={'class': "a-link-normal"})
        if book_link:
            full_link = 'https://www.amazon.in' + book_link.get('href')
            book_details = get_book_details(full_link)
            df.loc[len(df)] = book_details
    
    return df

# Example usage
no_of_pages = 2  # Number of pages to scrape
for i in range(1, no_of_pages + 1):
    df = get_data(i)

# Display the final DataFrame
print(df.head())

# Optionally, save the DataFrame to a CSV file
df.to_csv('amazon_bestsellers_details.csv', index=False)
