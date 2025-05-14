# ShopInsider - E-commerce Product Data Scraper (Phase 1)

**Project Repository:** `https://github.com/ugurhidir/shop-insider`

## Project Overview

ShopInsider (Phase 1) is a Python-based web scraping tool designed to extract product information from e-commerce websites. This script accepts a user-provided URL for a product listing page, fetches dynamic web content using Selenium, parses the HTML with BeautifulSoup, extracts key data points (product name, price, product URL), and stores this structured data into a CSV file. This project was initially demonstrated by scraping laptop listings from Hepsiburada.com, but it is structured to be adaptable to other e-commerce platforms by modifying its HTML parsing logic.

## Core Functionality

*   Accepts a target URL for an e-commerce product listing page.
*   Utilizes Selenium WebDriver to handle JavaScript-rendered content.
*   Parses HTML content using BeautifulSoup4.
*   Extracts product name, current price, and direct product URL.
*   Cleans and converts price data into a numerical format.
*   Normalizes product URLs to absolute links.
*   Saves scraped data to a CSV file (e.g., `scraped_products.csv`).
*   Includes error handling for common web scraping and file I/O issues.

## Technologies & Libraries Utilized

*   Python 3
*   Selenium WebDriver
*   `webdriver_manager` (for ChromeDriver management)
*   BeautifulSoup4 (bs4)
*   Pandas
*   `re` (Regular Expressions module)
*   `time` module

## Skills Demonstrated

*   Web Scraping with Python.
*   Handling dynamically loaded web content using Selenium.
*   HTML parsing and data extraction with BeautifulSoup.
*   Identifying and using appropriate CSS selectors and element attributes (e.g., `data-test-id`).
*   Data cleaning, transformation (e.g., price string to float), and structuring.
*   Storing scraped data in a structured format (CSV) using Pandas.
*   Implementing error handling for robust script execution.
*   Browser automation basics, including headless mode and user-agent spoofing.

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
4.  **Configure the Script (IMPORTANT):**
    *   Open the Python script (e.g., `shop_insider.py`).
    *   **Modify the `URL` variable** to the product listing page of the e-commerce site you wish to scrape.
    *   **Adjust BeautifulSoup Selectors:** You will likely need to inspect the HTML of your target site and **update the selectors** used to find product cards, names, prices, and links within the script. The current selectors are examples based on an initial test case.
5.  **Run the Script:**
    ```bash
    python shop_insider.py
    ```
    The script will output a CSV file (e.g., `scraped_products.csv`) containing the scraped data.

## Future Enhancements

*   Support for scraping multiple e-commerce sites with site-specific parsing configurations.
*   User input for target URLs or search queries.
*   Pagination handling to scrape data from multiple result pages.
*   Database integration (e.g., SQLite) for persistent data storage.
*   Advanced features like price tracking, alerts, and data analysis.
*   Development of a web application interface (e.g., using Flask or Django).