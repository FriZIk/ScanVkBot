from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import numpy as np
import sqlite3
import telebot
import os.path


def TelebotInitialize(BotKey):
    print("Введите ключ бота:")
    bot = telebot.TeleBot(BotKey)
    try :
        user - bot.get_me()
        print("Успешное подключение")
    except:
        print("Ошибка подключения,проверьте правильность введённых данных!")


def AutoParserIPs(town):
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
        DbWorker(ips)
    finally:
        driver.quit()


def DbWorker(ips):
    conn = sqlite3.connect('/home/frizik/Projects/ScanTelegramBot/Data/IpsDataBase.sqlite')
    cursor = conn.cursor()
    print(ips)
    
    PathToDatabase = "/home/frizik/Projects/ScanTelegramBot/Data/IpsDataBase.sqlite"
    if os.path.exists(PathToDatabase) != True:
        cursor.execute('''CREATE TABLE ips (id int auto_increment primary key,Adress varchar,ActiveStatus varchar)''')                      
    cursor.execute("INSERT INTO ips (Adress,ActiveStatus) VALUES ('83.221.202.194','active')")

    conn.commit()
    cursor.close()
    conn.close()


def main():
    print("Введите ключ бота:")
    BotFatherKey = input()
    TelebotInitialize(BotFatherKey)
    print("Введите название города:")
    TownName = input() 
    AutoParserIPs(TownName)
    

if __name__ == "__main__":
    main()
