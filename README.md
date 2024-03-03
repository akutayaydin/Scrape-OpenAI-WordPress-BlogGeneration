# Scrape-OpenAI-WordPress-BlogGeneration

### Introduction
This repository contains a Python script for scraping data from Quora and generating AI-generated blog content based on the scraped data. The script utilizes Selenium, BeautifulSoup, Pandas,the OpenAI API, the Dall-e API and Wordpress integration plugin. 

### Requirements
- Python 3.x
- Selenium
- BeautifulSoup
- Pandas
- Scrapy
- `wordpress_xmlrpc` library

You can install the required libraries using pip:

```bash
pip install selenium
pip install beautifulsoup4
pip install pandas
pip install scrapy
pip install python-wordpress-xmlrpc
```

### Usage
1. Clone this repository to your local machine.
2. Ensure you have the required dependencies installed.
3. Customize the script as needed.
4. Run the script using the command: `python scraper.py`

### Customization
- Adjust `keywords` list to specify the search terms you want to scrape on Quora.
- Modify `num_of_scrolls` to adjust the number of times the script scrolls down the page to load more content.
- Customize `num_of_questions_to_scrape` to specify the number of questions to scrape for each keyword.
- Tweak `more_buttons_to_click` to set the number of "more" buttons the script clicks for loading more content.
- Adjust wait times (`longer_wait_time`, `wait_time`) as needed to ensure proper loading of content.
- Customize the filename for the backup CSV file in the `file_name` variable.
- Ensure to update WordPress credentials (`url`, `username`, `password`) in the code for posting to WordPress.

### Functionality
- The script iterates over each keyword in the `keywords` list.
- For each keyword, it scrapes Quora's search results page for questions and related data.
- It collects details such as question text, number of followers, number of upvotes, number of answers, and top answers for each question.
- The scraped data is stored in a Pandas DataFrame.
- The script also includes functionality to generate AI-generated blog content based on the scraped data.
- Finally, the script backs up the scraped data to a CSV file and posts it to WordPress.

### AI-Generated Blog Content
The script includes functionality to generate AI-generated blog content using OpenAI's GPT-3.5 model. It follows these steps:

It reads the previously scraped data from the CSV file.
It prepares the text for AI generation, combining the topic, question, and top 3 content for each entry.
It passes the prepared text to the OpenAI API to generate blog content.
It extracts the title and content from the generated blog post.
It updates the DataFrame with the generated content and marks the status as 'In_Review'.
The generated blog content is then ready for review and use.

### WordPress Posting
The script includes functionality to post the scraped data to a WordPress website using WordPress XML-RPC. Here's how it works:
1. It reads the previously scraped data from the CSV file.
2. It prepares the content for posting, including the title, body, tags, and category.
3. It uploads any media files (e.g., images) associated with the post.
4. It posts the content to WordPress, marking the status as 'pending'.
5. Upon successful posting, it prints a success message.

### Notes
- This script assumes the presence of a Selenium web driver configured correctly for your system.
- Adjustments may be required for optimal performance based on network speed and Quora's website changes.
- Ensure to install and activate the WordPress XML-RPC plugin on your WordPress website to enable XML-RPC functionality.

### Disclaimer
This script is provided for educational and informational purposes only. Ensure compliance with Quora's terms of service and usage policy while using this script.
