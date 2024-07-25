import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
con = requests.get("https://www.ablkart.com/product/mechanzo-12")

# Parse the HTML content
soup = BeautifulSoup(con.text, 'html.parser')

# Extract product name
product_name = soup.find("h2", class_="single-product-title").text.strip()

# Extract product price
product_price = soup.find("h3", class_="spical-price").text.strip()

# Extract product description
product_description = soup.find("div", class_="pro-content").text.strip()

# Structure the extracted information
product_info = {
    "Name": product_name,
    "Price": product_price,
    "Description": product_description,
}

# Open a file to write the structured information
with open("product_info.txt", "w") as f:
    f.write("Product Information\n")
    f.write("-------------------\n")
    f.write(f"Name: {product_info['Name']}\n")
    f.write(f"Price: {product_info['Price']}\n")
    f.write(f"Description: {product_info['Description']}\n")
    f.write("Specifications:\n")
    # for spec_name, spec_value in product_info['Specifications'].items():
    #     f.write(f"  {spec_name}: {spec_value}\n")

print("Product information extracted and saved to 'product_info.txt'")
