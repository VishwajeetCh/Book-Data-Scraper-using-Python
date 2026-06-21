import requests
from bs4 import BeautifulSoup
import os
import csv
import datetime
import pandas as pd

URL = "https://books.toscrape.com/"

def save_data(title, price):
        file_exists = os.path.isfile("data.csv")


        data = {
            "Product": title,
            "Price": price,
            "Date": datetime.datetime.now()
        }

        df = pd.DataFrame([data])

        if file_exists:
            df.to_csv("data.csv", mode="a",
                    header=False, index=False)
        else:
            df.to_csv("data.csv", index=False)


    # Fetch webpage
response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")

    # Get first book
first_book = soup.find("article", class_="product_pod")

title = first_book.h3.a["title"]
price = first_book.find("p", class_="price_color").text
rating = first_book.p["class"][1]

print(f"Title: {title}")
print(f"Price: {price}")
print(f"Rating: {rating} stars")

    # Save using your function
save_data(title, price)

    # Optional: Save full data using csv
books_data = [{
        "title": title,
        "price": price,
        "rating": rating
    }]

with open("books.csv", "w", newline="", encoding="utf-8") as file:
        headers = ["title", "price", "rating"]
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(books_data)

print("Scraping complete! Check books.csv and data.csv")