from flask import Flask, render_template, request, redirect
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Importa la classe Service
from selenium.webdriver.common.keys import Keys
import time

# Configura Flask
app = Flask(__name__)

# Configura il percorso del ChromeDriver
chromedriver_path = r'C:\Users\fabio\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    # Ottieni la parola inserita dall'utente nel form
    parola = request.form['parola']
    
    # Configura il webdriver di Selenium utilizzando Service
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service)
    
    # Vai su YouTube e cerca la parola
    search_url = f"https://www.youtube.com/results?search_query={parola}"
    driver.get(search_url)
    
    # Lascia il browser aperto per 5 secondi per vedere i risultati
    time.sleep(5)
    
    # Chiude il browser
    driver.quit()
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
