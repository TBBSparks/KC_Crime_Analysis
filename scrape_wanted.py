#import dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import re
import pandas as pd
import time
import lxml

def init_browser():
    executable_path = {"executable_path" : "geckodriver"}
    return Browser("firefox", **executable_path, headless=False)

wanted_web = {}

def scrape_latest():
    
    browser = init_browser()

    url = 'https://spotcrime.com/MO/Kansas%20City/trends'
    browser.visit(url)
    html = browser.html
    time.sleep(10) # Sleep for 10 seconds
    soup = bs(html, "html.parser")

    latest_crime = soup.find('p').get_text()
    
    wanted_web["latest_crime"] = latest_crime
   
    browser.quit()
    return wanted_web


