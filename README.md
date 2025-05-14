# ShopInsider - E-commerce Product Data Scraper & Analyzer (Phase 1)

**Project Repository:** `https://github.com/ugurhidir/shop-insider`

## Project Overview

ShopInsider (Phase 1) is a Python-based web scraping tool designed to extract product information, specifically for laptops, from the popular Turkish e-commerce platform Hepsiburada.com. The primary goal of this initial phase is to demonstrate the ability to reliably fetch dynamic web content, parse HTML to extract relevant data points (product name, price, and product URL), and store this structured data into a CSV file for potential further analysis. This project serves as a foundational step towards building a more comprehensive e-commerce analysis tool.

The development of this scraper involved overcoming challenges related to dynamic content loading and anti-scraping mechanisms, necessitating the use of browser automation techniques.

## Core Functionality (Phase 1)

*   **Targeted Web Scraping:** Specifically scrapes laptop listings from Hepsiburada (`https://www.hepsiburada.com/ara?q=laptop`).
*   **Dynamic Content Handling:** Utilizes Selenium WebDriver to control a Chrome browser instance, allowing it to render JavaScript-heavy pages and access dynamically loaded content that `requests` alone cannot retrieve.
*   **HTML Parsing:** Employs BeautifulSoup4 to parse the retrieved HTML structure, making it easy to navigate and search for specific data elements.
*   **Data Extraction:** Identifies and extracts the following key information for each listed laptop:
    *   Product Name
    *   Current Price
    *   Direct URL to the product page
*   **Data Cleaning & Transformation:** Includes logic to clean and convert extracted price strings into a numerical (float) format suitable for analysis. Product URLs are also normalized to full, absolute links.
*   **Structured Data Storage:** Organizes the scraped data into a structured format (list of dictionaries) and then uses the Pandas library to create a DataFrame, which is subsequently saved as a CSV file (`hepsiburada_laptoplar_selenium.csv`).
*   **Error Handling:** Implements `try-except` blocks to manage potential issues during web requests, browser automation, data parsing, and file I/O, ensuring a more robust script.

## Technologies & Libraries Utilized

*   **Python 3:** The core programming language.
*   **Selenium WebDriver:**
    *   For browser automation, enabling interaction with dynamic web pages that heavily rely on JavaScript for content rendering.
    *   Used to navigate to the target URL and retrieve the fully rendered HTML `page_source`.
*   **`webdriver_manager`:**
    *   Automates the management (download and setup) of ChromeDriver, ensuring compatibility with the installed Chrome browser version.
*   **BeautifulSoup4 (bs4):**
    *   For parsing HTML and XML documents. Used to navigate the HTML DOM tree and extract specific data elements using tags, classes, and attributes (like `data-test-id`).
*   **Pandas:**
    *   A powerful data manipulation and analysis library. Used here to create a structured DataFrame from the scraped data and to easily export it to a CSV file.
*   **Requests (Implicitly Understood):** While Selenium handles the primary page fetching, understanding how `requests` works is foundational for web scraping.
*   **`re` (Regular Expressions):**
    *   Used for more robust cleaning of price strings, extracting numerical values from varied text formats.
*   **`time` module:**
    *   Used to introduce deliberate pauses (`time.sleep()`) to allow dynamic content on the webpage to load температура (temperature) before attempting to scrape it.

## Skills Demonstrated & Learning Outcomes

This project showcases a range of valuable skills in web scraping and data handling:

1.  **Web Scraping Fundamentals:**
    *   Understanding of how web pages are structured (HTML, DOM).
    *   Ability to inspect web page elements using browser developer tools to identify target data and appropriate selectors.
    *   Proficiency in sending HTTP-like requests (via Selenium which mimics browser behavior) and handling responses.

2.  **Dynamic Web Content Scraping with Selenium:**
    *   Successfully configured and used Selenium WebDriver with ChromeDriver to automate browser actions.
    *   Learned to retrieve `page_source` after JavaScript execution, a crucial skill for modern web scraping.
    *   Implemented strategies like `time.sleep()` for managing page load times (with an understanding that more advanced explicit/implicit waits are future improvements).
    *   Configured Chrome options, including `--headless` mode and `user-agent` spoofing to mimic legitimate browser traffic and potentially bypass basic anti-bot measures.

3.  **HTML Parsing with BeautifulSoup4:**
    *   Effectively used BeautifulSoup to parse complex HTML structures.
    *   Mastered various `find()` and `find_all()` methods with different types of selectors:
        *   Tag names (`'li'`, `'h3'`, `'div'`)
        *   Attributes (e.g., `attrs={"data-test-id": "product-card"}`)
        *   Lambda functions for more flexible class name matching (e.g., `class_=lambda value: value and value.startswith('productListContent-')`)
    *   Navigated nested HTML elements to pinpoint specific data.

4.  **Data Extraction, Cleaning, and Transformation:**
    *   Extracted text content from HTML elements (`.text.strip()`).
    *   Cleaned and normalized data, particularly price strings, using string methods and regular expressions (`re` module) to convert them into usable numerical formats (float).
    *   Handled and constructed absolute URLs from relative paths.

5.  **Data Structuring and Storage with Pandas:**
    *   Organized scraped data into a list of dictionaries, a common and effective way to represent structured records.
    *   Utilized Pandas DataFrames for efficient data handling and manipulation.
    *   Exported structured data to a CSV file, a widely used format for data sharing and analysis.

6.  **Error Handling and Robust Scripting:**
    *   Implemented `try-except` blocks to gracefully handle potential runtime errors such as network issues, element not found exceptions, and data conversion errors (`ValueError`).
    *   Ensured the browser instance (`driver`) is properly closed using `driver.quit()` even if errors occur (though a `finally` block would be a more robust way, the current `except` block also attempts this).

7.  **Problem-Solving and Iterative Development:**
    *   The process of identifying correct and stable selectors for Hepsiburada's complex and potentially dynamic HTML structure required significant debugging, inspection, and iterative refinement of the scraping logic. This demonstrates practical problem-solving skills.
    *   Adapted the scraping strategy from `requests` (which failed due to anti-scraping) to `Selenium`.

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
4.  **Run the Script:**
    ```bash
    python shop_insider.py
    ```
    (Assuming your main Python file is named `shop_insider.py`)
    The script will launch a Chrome browser (possibly headless), navigate to Hepsiburada, scrape laptop data, and save it to `hepsiburada_laptoplar_selenium.csv` in the same directory.

## Future Enhancements (ShopInsider - Phases 2+)

This project is the first phase of a larger vision. Future developments could include:

*   **Scraping Multiple E-commerce Sites:** Expanding to other popular platforms.
*   **User Input for Product/Category:** Allowing users to specify what they want to search for.
*   **Pagination Handling:** Scraping data from multiple pages of search results.
*   **Database Storage:** Using SQLite or another database for more persistent and queryable data storage.
*   **Price Tracking & Alerts:** Monitoring price changes over time and notifying users.
*   **Data Analysis & Visualization:** Performing more in-depth analysis and creating charts.
*   **Web Application Interface:** Building a Flask/Django web app to present the data and analysis in a user-friendly way.
*   **Potential SaaS Product:** Evolving into a subscription-based service for e-commerce insights.