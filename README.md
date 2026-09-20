🛒 CityMall Computer Components Scraper
📌 Project Objective
A Python-based web scraper that collects product information (name, price, seller, and product link) from the Computer Components & Accessories category on CityMall Myanmar.
The scraper handles one page, cleans the extracted data, and exports results into an Excel file.

🌐 Website
Website: CityMall Myanmar

Category URL:  
https://www.citymall.com.mm/citymall/en/Categories/Home-%26-Living-Lifestyle/Electronics/Computer-Components-%26-Accessories/c/id05011003

📊 Data Extracted
Product Name

Product Price (Ks → converted to float)

Seller / Shop Name

Product Link (full URL)

🛠️ Technologies Used
Technology	Purpose
Python	Main programming language
Requests	Sending HTTP requests
BeautifulSoup	Parsing and extracting HTML
Pandas	Creating/managing dataset
tqdm	Progress bar (optional)
openpyxl	Writing data to Excel


📦 Installation
Clone the repository:

bash
git clone https://github.com/your-username/citymall-scraper.git
cd citymall-scraper
Install dependencies:

bash
pip install -r requirements.txt
▶️ How to Run
Run the Python script:

bash
python citymall_scraper.py
The scraper will:

Send requests to CityMall product pages.

Parse HTML with BeautifulSoup.

Extract product details.

Export results to Exported_Data.xlsx.

📑 Sample Output
Name	Price	Seller	Link
Anitech Wires Optical Mouse	23,500	Sold by CMHL	Product Link
Logitech Wireless Mouse M185	60,000	Sold by CMHL	Product Link
Kingston Micro SD 32GB	15,000	Sold by CMHL	Product Link


⚠️ Challenges
Identifying correct HTML tags/classes (div.product-info).

Handling missing or inconsistent seller names.

Cleaning price values (removing commas and “Ks”).

🧩 Main Functions
extract_name() → Extracts product name.

extract_price() → Cleans and converts price to float.

extract_seller() → Extracts seller/shop name.

extract_link() → Builds full product URL.

export_as_excel() → Saves data to Excel.

⚙️ Configuration
To scrape another category, replace the URL in:

python
my_url = "https://www.citymall.com.mm/citymall/en/Categories/.../c/idXXXXXX"
⚠️ Important Notes
Website Changes: If CityMall updates its HTML structure, functions may need editing.

Request Rate: Add delays (time.sleep()) if scraping multiple pages.

Legal:
