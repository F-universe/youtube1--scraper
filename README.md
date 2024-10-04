YouTube Search Scraper
This project uses Flask and Selenium to scrape YouTube search results and display the corresponding video titles and links. The application allows users to search for YouTube videos by entering a keyword and displaying the video titles and links.

Features
Enter a keyword via the search form.
Scrape YouTube search results using Selenium.
Extract video titles and links.
Display the data on the web page.
Prerequisites
To run this project, you need the following software and libraries:

Python 3.x
Flask
Selenium
BeautifulSoup4
Google Chrome
ChromeDriver (compatible with your installed Chrome version)
Installation
Clone the repository:

bash
Copia codice
git clone https://github.com/your-username/your-repo.git
cd your-repo
Create a virtual environment (optional but recommended):

bash
Copia codice
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install the dependencies:

bash
Copia codice
pip install -r requirements.txt
If you don’t have a requirements.txt file, manually install the libraries:

bash
Copia codice
pip install flask selenium beautifulsoup4
Download ChromeDriver that matches your version of Google Chrome, and place it in the path specified in the code:

bash
Copia codice
C:\Users\fabio\Downloads\chromedriver-win64\chromedriver.exe
Modify the ChromeDriver path in the code if necessary:

python
Copia codice
chromedriver_path = r'C:\Users\fabio\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
Running the Application
Run the Flask application:

bash
Copia codice
python app.py
Open your browser and visit http://127.0.0.1:5000/.

Enter a keyword in the search field and view the video titles and links corresponding to your search.

Project Structure
app.py: The main file of the Flask application. It contains the logic to handle the search form and perform the scraping with Selenium.
templates/index.html: The HTML page for searching and displaying results.
Using Selenium
The application uses Selenium to simulate a web browser and navigate YouTube. The scraping process follows these steps:

Perform a YouTube search with the entered keyword.
Scroll the page to load more results.
Extract the video titles and URLs using BeautifulSoup.
Display the results on the web page.
Note
Make sure you have the latest version of Google Chrome and the corresponding ChromeDriver installed and correctly configured.
Use the code in compliance with the website’s scraping policies.
Contributing
If you’d like to contribute to this project, feel free to open a pull request or create an issue to discuss changes.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
