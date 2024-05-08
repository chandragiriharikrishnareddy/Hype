import requests
from bs4 import BeautifulSoup
import sqlite3

# Function to scrape quotes from the website
def scrape_quotes():
    url = "https://www.bikewale.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')
    extracted_quotes = []
    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]
        extracted_quotes.append({'text': text, 'author': author, 'tags': tags})
    return extracted_quotes

# Function to initialize SQLite database and store quotes
def store_quotes(quotes):
    conn = sqlite3.connect('quotes.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS quotes
                 (text TEXT, author TEXT, tags TEXT)''')
    for quote in quotes:
        c.execute("INSERT INTO quotes (text, author, tags) VALUES (?, ?, ?)",
                  (quote['text'], quote['author'], ', '.join(quote['tags'])))
    conn.commit()
    conn.close()

# Main function
def main():
    quotes = scrape_quotes()
    store_quotes(quotes)
    print("Quotes extracted and stored successfully!")

if __name__ == "__main__":
    main()
