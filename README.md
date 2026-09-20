# 🛒 CityMall Computer Components Scraper

## 📌 Project Title
CityMall.com.mm Computer Components Scraper

## 🎯 Project Objective
A Python-based web scraper that collects product information (name, price, seller, and product link) from the **Computer Components & Accessories** category on CityMall Myanmar.  
The scraper handles one page, cleans the extracted data, and exports results into an Excel file.

## 🌐 Website Name and URL
- **Website:** CityMall Myanmar  
- **Category URL:**  
  https://www.citymall.com.mm/citymall/en/Categories/Home-%26-Living-Lifestyle/Electronics/Computer-Components-%26-Accessories/c/id05011003

## 📊 Description of the Data Extracted
The scraper extracts the following fields for each product:
- Product Name  
- Product Price (Ks → converted to float)  
- Seller / Shop Name  
- Product Link (full URL)

## 🛠️ Technologies / Libraries Used
| Technology    | Purpose                        |
|---------------|--------------------------------|
| Python        | Main programming language      |
| Requests      | Sending HTTP requests          |
| BeautifulSoup | Parsing and extracting HTML    |
| Pandas        | Creating and managing dataset  |
| tqdm          | Displaying scraping progress   |
| openpyxl      | Writing data to Excel          |

## 📦 Python Libraries Required
## 🧱 Python Libraries Required

- requests  
- beautifulsoup4  
- tqdm  
- pandas  
- openpyxl  


## ⚙️ Installation
Clone the repository:
```bash
git clone https://github.com/your-username/citymall-scraper.git
cd citymall-scraper
▶️ How to Run the Program
Run the Python script:
python citymall_scraper.py

pip install -r requirements.txt

The scraper will:

Send requests to CityMall product pages.

Parse HTML with BeautifulSoup.

Extract product details.

Export results to Exported_Data.xlsx.

📑 Data Fields Extracted
Name → Product name

Price → Product price (float)

Seller → Seller/shop name

Link → Full product URL
📊 Sample Output

| Name | Price | Seller | Link |
| --- | --- | --- | --- |
| Anitech Wires Optical Mouse | 23,500 | Sold by CMHL | Product Link |
| Logitech Wireless Mouse M185 | 60,000 | Sold by CMHL | Product Link |
| Kingston Micro SD 32GB | 15,000 | Sold by CMHL | Product Link |

📈 Number of Products / Pages Scraped
Pages scraped: 1

Products scraped: ~20–24 (depending on items listed on the page)

⚠️ Challenges Encountered
Identifying correct HTML tags/classes (div.product-info)

Handling missing or inconsistent seller names

Cleaning price values (removing commas and “Ks”)

📝 Important Notes / Limitations
The scraper currently works for one page only.

To extend to multiple pages, pagination logic must be added.

The scraper depends on CityMall’s current HTML structure. If the website changes, functions may need updating.

Data is for educational purposes only.

👨‍💻 Project Author
Developed by: Myat Myat Nwe
