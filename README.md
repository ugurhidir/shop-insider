# ShopInsider - General Purpose E-commerce Product Data Scraper (Phase 1)

**Project Repository:** `https://github.com/ugurhidir/shop-insider`

## Project Overview

ShopInsider (Phase 1) is a Python-based web scraping tool designed to extract product information from e-commerce websites. The primary goal of this initial phase is to demonstrate the ability to accept a user-provided URL for a product listing page, reliably fetch dynamic web content, parse HTML to extract relevant data points (product name, price, and product URL), and store this structured data into a CSV file for potential further analysis. This project serves as a foundational step towards building a more comprehensive e-commerce analysis tool and was **initially tested and demonstrated using laptop listings from Hepsiburada.com as a sample case.**

The development of this scraper involved overcoming challenges related to dynamic content loading and anti-scraping mechanisms, necessitating the use of browser automation techniques. The tool is designed with the flexibility to be adapted for various e-commerce platforms by adjusting its HTML parsing logic (selectors).

## Core Functionality (Phase 1)

*   **Flexible URL Input:** While demonstrated with Hepsiburada, the script can be adapted to take a URL for a product listing page from various e-commerce sites.
*   **Dynamic Content Handling:** Utilizes Selenium WebDriver to control a Chrome browser instance, allowing it to render JavaScript-heavy pages and access dynamically loaded content that `requests` alone cannot retrieve.
*   **HTML Parsing:** Employs BeautifulSoup4 to parse the retrieved HTML structure, making it easy to navigate and search for specific data elements.
*   **Data Extraction:** Identifies and extracts the following key information for each listed product (selectors need to be adapted per site):
    *   Product Name
    *   Current Price
    *   Direct URL to the product page
*   **Data Cleaning & Transformation:** Includes logic to clean and convert extracted price strings into a numerical (float) format suitable for analysis. Product URLs are also normalized to full, absolute links based on the target site.
*   **Structured Data Storage:** Organizes the scraped data into a structured format (list of dictionaries) and then uses the Pandas library to create a DataFrame, which is subsequently saved as a CSV file (e.g., `scraped_products.csv`).
*   **Error Handling:** Implements `try-except` blocks to manage potential issues during web requests, browser automation, data parsing, and file I/O, ensuring a more robust script.

## Technologies & Libraries Utilized
(Bu bölüm aynı kalabilir)

## Skills Demonstrated & Learning Outcomes
(Bu bölüm büyük ölçüde aynı kalabilir, "Targeted Web Scraping" yerine "Versatile Web Scraping" gibi bir ifade kullanılabilir veya genel e-ticaret sitelerine uygulanabilirliği vurgulanabilir.)

1.  **Versatile Web Scraping:**
    *   Understanding of how e-commerce web pages are structured (HTML, DOM).
    *   Ability to inspect web page elements using browser developer tools to identify target data and appropriate selectors **across different e-commerce platforms.**
    *   Proficiency in sending HTTP-like requests (via Selenium) and handling responses.

(Diğer beceri maddeleri büyük ölçüde geçerliliğini korur, sadece Hepsiburada özelindeki vurgu genele yayılır)

## How to Run

1.  **Prerequisites:**
    *   Python 3.6+
    *   Google Chrome browser installed.
2.  **Clone the Repository:**
    ```bash
    git clone https://github.com/ugurhidir/shop-insider.git
    cd shop-insider
    ```
3.  **Install Dependencies:**
    ```bash
    pip install selenium webdriver-manager beautifulsoup4 pandas
    ```
4.  **Modify Target URL (and potentially selectors):**
    *   Open the Python script (e.g., `shop_insider.py`).
    *   Change the `URL` variable to the product listing page of the e-commerce site you want to scrape.
    *   **Important:** You will likely need to inspect the HTML of the new target site and **adjust the BeautifulSoup selectors** (e.g., for `urun_kartlari`, `ad_elementi`, `fiyat_elementi`) within the script to match the new site's structure. This script was initially tested with Hepsiburada's laptop category.
5.  **Run the Script:**
    ```bash
    python shop_insider.py
    ```
    The script will launch a Chrome browser, navigate to the specified URL, scrape product data, and save it to a CSV file (e.g., `scraped_products.csv`).

## Future Enhancements (ShopInsider - Phases 2+)
(Bu bölüm aynı kalabilir, "Scraping Multiple E-commerce Sites" maddesi zaten bu genel yaklaşımla uyumlu.)