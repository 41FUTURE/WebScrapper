Pokémon Amazon Scraper
Description
This utility is crafted for collecting data on Pokémon Fit Plush items available on Amazon Japan. Utilizing Selenium, it efficiently navigates through the webpage, captures essential details, and organizes them neatly into a CSV file.

Prerequisites
Python installed
Selenium library
Appropriate WebDriver (Example uses ChromeDriver)
Captured Data Fields
Name of Pokémon
ASIN Identifier
Link to Product Page
Users can tailor the script to gather additional data if needed.

Steps to Deploy
1. Installing Python
If not already installed, obtain Python from python.org.

2. Installing Selenium
Run the following command to get Selenium: pip install selenium

3. WebDriver Acquisition
Download ChromeDriver or an alternative, compatible WebDriver. Extract it to an accessible directory.

4. Running the Utility
Download the provided script.
Modify the chrome_driver_path variable to point to your WebDriver's location.
Execute using:
python filename.py  # Substitute with the actual filename


The gathered data populates a products.csv file.

Caution
Confirm alignment with Amazon's robots.txt and terms of service prior to execution.
The utility is designated for educational exploration and is not endorsed for unauthorized commercial application.
Contributions
Enhancements and improvements are appreciated. Fork, adjust, and submit pull requests as desired.
