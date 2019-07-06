from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
import numpy as np

def AutoParserIPs(town):
    display = Display(visible=0, size=(800, 800))  
    display.start()
    driver = webdriver.Chrome()
    link = "https://4it.me/getlistip"
    driver.get(link)
    elem = driver.find_element_by_id("city")
    elem.send_keys(town)
    elem.submit()
    ips = []
    try:
        value  = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME,"pre")))
        ips = value.text
        IpsArray = np.array(ips)
        print(IpsArray)
    finally:
        driver.quit()
        display.stop()