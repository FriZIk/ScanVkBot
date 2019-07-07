from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
import ScanIPS as IPs
import re

def StopParser(driver,display):
    driver.quit()
    display.stop()


def AutoParserIPs(town):
    display = Display(visible=0, size=(1, 1))  
    display.start()
    driver = webdriver.Chrome()
    link = "https://4it.me/getlistip"
    driver.get(link)
    elem = driver.find_element_by_id("city")
    elem.send_keys(town)
    elem.submit()
    ips = []
    try:
        value  = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME,"pre")))
        ips = value.text
        StopParser(driver,display)

        prefab = re.compile('-')
        CountOfStrings = len(prefab.findall(ips))

        prefab1 = re.compile('\n')
        CountOfn = len(prefab1.findall(ips))

        IPs.StringParser(ips,CountOfStrings,CountOfn)
    finally:
        StopParser(driver,display)