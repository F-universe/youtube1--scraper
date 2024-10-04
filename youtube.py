from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

# Set up Flask
app = Flask(__name__)

# Set the ChromeDriver path
chromedriver_path = r'C:\Users\fabio\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

@app.route('/')
def index():
    return render_template('index.html', data=None)

@app.route('/search', methods=['POST'])
def search():
    # Get the word entered by the user in the form
    keyword = request.form['keyword']
    
    # Set up Selenium WebDriver using Service
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service)
    
    # Go to YouTube and search for the keyword
    search_url = f"https://www.youtube.com/results?search_query={keyword}"
    driver.get(search_url)

    # Add a pause to load the initial results
    time.sleep(5)
    
    # Scroll down to load more videos (increased number of scrolls)
    for _ in range(10):  # Increase the number of scrolls
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(2)  # Wait a bit longer to load more content
    
    # Wait until the video elements are visible
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ytd-video-renderer"))
    )

    # Get the HTML of the page
    page_html = driver.page_source
    soup = BeautifulSoup(page_html, 'html.parser')
    
    # Find all video elements (ytd-video-renderer)
    video_elements = soup.find_all('ytd-video-renderer')

    # List to store video details
    video_data = []

    # Iterate over each video to extract information
    for video in video_elements:
        # Extract the video title
        title_tag = video.find('a', id='video-title')
        title = title_tag['title'] if title_tag else 'N/A'

        # Extract the video URL
        url = f"https://www.youtube.com{title_tag['href']}" if title_tag else '#'

        # Add the video to the list of collected data
        video_data.append({
            'title': title,
            'url': url
        })
    
    # Close the browser
    driver.quit()
    
    # Pass the data to the HTML template
    return render_template('index.html', data=video_data)

if __name__ == '__main__':
    app.run(debug=True)
