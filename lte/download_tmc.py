#from turtle import down
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
import os
#import matplotlib.pyplot as plt
#import numpy as np
#import xml.etree.ElementTree as ET
#import pandas as pd
import time

# ch2_tmc_ndn_20210518T1656115474_d_oth_d18
path_to_downloads = "/home/cynaptics/Downloads/"
temp = 0
dict = {'upper_left_lat': 60, 'upper_left_long': -130, 
        'upper_right_lat': 60, 'upper_right_long': -125,
        'lower_left_lat': 30, 'lower_left_long': -130,
        'lower_right_lat': 30, 'lower_right_long': -125}

def filter(driver):
    dropdown = Select(driver.find_element(By.NAME,"filterForm:filterTable:0:attr"))
    dropdown.select_by_value("CorrectedCoordinates;LOCATION_QUAD;label.Product_Observational.Observation_Area.Mission_Area.isda:Geometry_Parameters.isda:Corrected_Corner_Coordinates_onlyForPradan")
    upper_left_long = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'filterForm:filterTable:0:ULLong')))
    upper_left_lat = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'filterForm:filterTable:0:ULLat')))
    upper_right_long = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'filterForm:filterTable:0:URLong')))
    upper_right_lat = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'filterForm:filterTable:0:URLat')))
    lower_left_long=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'filterForm:filterTable:0:BLLong')))
    lower_left_lat=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'filterForm:filterTable:0:BLLat')))
    lower_right_long=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'filterForm:filterTable:0:BRLong')))
    lower_right_lat=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'filterForm:filterTable:0:BRLat')))
    upper_left_lat.send_keys(dict['upper_left_lat'])
    upper_left_long.send_keys(dict['upper_left_long'])
    upper_right_lat.send_keys(dict['upper_right_lat'])
    upper_right_long.send_keys(dict['upper_right_long'])
    lower_left_lat.send_keys(dict['lower_left_lat'])
    lower_left_long.send_keys(dict['lower_left_long'])
    lower_right_lat.send_keys(dict['lower_right_lat'])
    lower_right_long.send_keys(dict['lower_right_long'])
    driver.find_element(By.ID,"filterForm:filterButton").click()

def find_link_and_download(driver, downloaded):
    links = driver.find_elements(By.PARTIAL_LINK_TEXT, 'ch2_tmc')
    # print(links)
    # return 0
    for link in links:
        global temp 
        temp += 1
        image_name = link.get_attribute('href')[139:180]
        # print(image_name)
        if image_name.find("oth") == -1:
            continue
        if os.path.exists(path_to_downloads + image_name + ".zip"):
            downloaded += 1
            print(f"{image_name}: File aldready downloaded, Total files downloaded: {downloaded}\n")
            continue
        else:
            link.click()
            print(f"Downloading startedS: {image_name}")
            while not os.path.exists(path_to_downloads + image_name + ".zip"):
                time.sleep(1)
            downloaded += 1                
            print(f"{image_name}: File sucessfully downloaded, Total files downloaded: {downloaded}\n")

    return downloaded


def download():
    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),chrome_options=options)
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get('https://pradan.issdc.gov.in/ch2/')

    sign_in_link = driver.find_element(By.LINK_TEXT,'BrowseAndDownload')
    sign_in_link.click()

    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'username')))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'password')))
    username.send_keys('mathjax')
    password.send_keys('Lmaonoob3.14')
    driver.find_element(By.XPATH,"//*[@type='submit']").click()
    driver.find_element(By.ID,"tableForm:payloads:6:j_idt44").click()

    downloaded = 0
#    filter(driver)
    downloaded = find_link_and_download(driver, downloaded)

    while(temp != 8200):
        next = driver.find_element(By.CSS_SELECTOR, ".ui-paginator-next.ui-state-default.ui-corner-all")
        next.click()
        time.sleep(3)
        downloaded = find_link_and_download(driver, downloaded)
    
    return

download()
