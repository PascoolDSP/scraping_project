import time
from selenium import webdriver
from bs4 import BeautifulSoup

def html_grabber(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless") 

    driver = webdriver.Chrome(options=options)

    driver.get(url)

    time.sleep(5)  

    html_code = driver.page_source

    soup = BeautifulSoup(html_code, 'html.parser')

    driver.quit()

    return soup.prettify()
