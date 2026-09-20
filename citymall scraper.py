import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd

def create_bsObj(website_url):
    """Create a BeautifulSoup object for the input URL."""
    # Request data from the website
    
    response = requests.get(website_url, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code == 200:
        # Extract web code
        web_data = response.text
        
        # Create a beautifulsoup object from web data
        bsObj = BeautifulSoup(web_data, "html.parser")
    
    return bsObj

    item_tags_link = bsObj.find_all("div", class_ = "product-info")

#Extract product names
def extract_name(item_tag):
    """Extract product name."""
    product_name = item_tag.find("div", class_="product-title").find("a", class_="name").text
    return product_name
# Extract product prices 
def extract_price(item_tag_var):
    """Extract product name from item tag"""
    item_price_tag = item_tag_var.find("p", class_="product-price mt-1")
    item_price = float(item_price_tag.text.replace(",", "").replace("Ks", ""))
    return item_price
# Extract sellers
def extract_seller(item_tag):
    """Extract seller name."""
    seller_tag = item_tag.find("p", class_="product-seller").text
    return seller_tag

#Extract Product Link
def extract_link(item_tag):
    """Extract Product Link from item tag"""
    item_link = item_tag.find("div", class_ ="product-title").find("a", class_="name").get("href")
    main_website = "https://www.citymall.com.mm"
    link_tag = main_website + item_link
    return link_tag
def page1_link(website_url_1):
    """Extract product info from page1."""
    bsObj = create_bsObj(website_url_1)
    item_tags = bsObj.find_all("div", class_="product-info")

    names, prices, sellers, links = [], [], [], []
    for item_tag in item_tags:
        names.append(extract_name(item_tag))
        prices.append(extract_price(item_tag))
        sellers.append(extract_seller(item_tag))
        links.append(extract_link(item_tag))


    return names, prices, sellers, links

def export_as_excel(names, prices, sellers, links):
    """Export data as Excel file."""
    df = pd.DataFrame({
        "Name": names,
        "Price": prices,
        "Seller": sellers,
        "Link": links
    })
    df.to_excel("Exported Data.xlsx", index=False)
    print("Exported Data.xlsx" exported successfully!")

##### Main #####

my_url = "https://www.citymall.com.mm/citymall/en/Categories/Home-%26-Living-Lifestyle/Electronics/Computer-Components-%26-Accessories/c/id05011003?q=%3Arelevance&page=0"

names, prices, sellers, links = page1_link(my_url)
export_as_excel(names, prices, sellers, links)


    


