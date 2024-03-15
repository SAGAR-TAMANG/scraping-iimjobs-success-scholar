from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import pandas as pd
import numpy as np

def main():
  chrome_options = Options
  CHROMEDRIVER = "C:\Program Files\chromedriver_win32\chromedriver.exe"
  
  service = Service(CHROMEDRIVER)
  chrome_options.binary_location(r"C:\Users\TAMANG\Downloads\chrome-win64\chrome-win64\chrome.exe")
  
  driver = webdriver.Chrome(service, chrome_options)

  driver.get("https://www.iimjobs.com/search/IT-0-0-0-1.html")


main()