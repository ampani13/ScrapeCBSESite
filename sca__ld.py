# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 13:18:23 2019

@author: Amiya
"""
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import csv


def get_driver(browser:str = "firefox") -> webdriver:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    #print(current_dir)
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=current_dir + "\\chromedriver.exe")
    else:
        driver = webdriver.Firefox(executable_path=current_dir + "\\geckodriver.exe")
    # Maximum Wait time to find elements in page (in order to let them load first)
    driver.implicitly_wait(10)

    return driver

def scrape_column(driver: webdriver, state_name :str, district_name :str):
    
    for i in range(2,27):
        try:
            serial_no = driver.find_element_by_xpath('//*[@id="T1"]/tbody/tr/td/table['+str(i)+']/tbody/tr/td[1]').text
            affiliation_no = driver.find_element_by_xpath('//*[@id="T1"]/tbody/tr/td/table['+str(i)+']/tbody/tr/td[2]/table/tbody/tr[1]/td').text
            name = driver.find_element_by_xpath('//*[@id="T1"]/tbody/tr/td/table['+str(i)+']/tbody/tr/td[2]/table/tbody/tr[2]/td').text
            head_principal_name = driver.find_element_by_xpath('//*[@id="T1"]/tbody/tr/td/table['+str(i)+']/tbody/tr/td[2]/table/tbody/tr[3]/td').text
            status_of_school = driver.find_element_by_xpath('//*[@id="tdstatus"]').text
            affiliated_upto =	driver.find_element_by_xpath('//*[@id="tdAffUpto"]').text
            school_info = driver.find_element_by_xpath('//*[@id="T1"]/tbody/tr/td/table['+str(i)+']/tbody/tr/td[2]/table/tbody').text
            school_addr = driver.find_element_by_xpath('//*[@id="T1"]/tbody/tr/td/table['+str(i)+']/tbody/tr/td[3]/table/tbody').text
            with open('persons.csv', 'a') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',')
                #filewriter.writerow(['Serial No', 'School Info', 'School Addr'])
                filewriter.writerow([serial_no, affiliation_no, name, state_name, district_name, head_principal_name])
        except NoSuchElementException:
            break
        print(serial_no)
        print(school_info)
        print(school_addr)
    return serial_no

def condition_scrape_column(driver: webdriver, total :int,state_name :str, district_name :str):
    serial_no = scrape_column(driver, state_name, district_name)
    click=0
    while serial_no<total:
        click += 1
        element_ahead = driver.find_element_by_xpath('//*[@id="Button1"]')
        driver.execute_script('arguments[0].click();', element_ahead)
        serial_no = scrape_column(driver, state_name, district_name)
    while(click>0):
        element_back = driver.find_element_by_xpath('//*[@id="Button2"]')
        driver.execute_script('arguments[0].click();', element_back)
        click -=1
    
def scarpe_cbse():
    print('scapping...')
    #current_dir = os.path.dirname(os.path.abspath(__file__))
    #print(current_dir)
    link = 'http://cbseaff.nic.in/cbse_aff/schdir_Report/userview.aspx'
    driver = get_driver("chrome")
    driver.get(link)
    driver.maximize_window()
    # Wait till page is loaded
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'Table1')))
    except TimeoutException:
        driver.quit()
        print("Loading of page " + str(driver) + " took too much time!")
    #print('fnd')
    time.sleep(5)
    # select state-wise radio button
    state_wise = driver.find_element_by_xpath('//*[@id="optlist_2"]')
    state_wise.click()
    time.sleep(5)
    
    for state in range(2,100):
        state_='//*[@id="ddlitem"]/option['+str(state)+']'
        try:
            state_select = driver.find_element_by_xpath(state_)
        except NoSuchElementException:
            break
        state_select.click()
        #print(state_select.text())
        time.sleep(2)
        for district in range(2,100):
            district_='//*[@id="DropDownDistrict"]/option['+str(district)+']'
            try:
                district_select = driver.find_element_by_xpath(district_)
            except NoSuchElementException:
                break
            district_select.click()
            #print(district_select.text())
            driver.find_element_by_xpath('//*[@id="search"]').click()
            time.sleep(5)
            #print(district_select.text)
            #print(state_select.text)
            try:
                state_name = driver.find_element_by_xpath('//*[@id="Lbltype1"]').text
                district_name = driver.find_element_by_xpath('//*[@id="lbltotal"]').text
                district_name = district_name[:-1]
                district_name = district_name.split()
                district_name=district_name[6:len(district_name)]
                final_district_name=''
                for sr in district_name:
                    final_district_name+=sr+' '
                print(state_name+' '+final_district_name)
                total = driver.find_element_by_xpath('//*[@id="tot"]').text
                condition_scrape_column(driver, total, state_name, district_name)
            except NoSuchElementException:
                continue          
    driver.quit()

if __name__ == "__main__":
    print('started...')
    scarpe_cbse();
    print('done...')

