# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 16:01:43 2019

@author: Amiya
"""

#s = 'Total School Affiliated From CBSE For CAR NICOBAR:'
#print(len(s))
#s = s[:-1]
#s = s.split()

#l=len(s)
#s=s[6:len(s)]
#d=''
#for sr in s:
#    d+=sr+' '
    
#print(d)
l = [[1,2,3]]

l.append([2,3,4])

print(l)

def jst():
    return 'hi',5



t= jst()

t1=t[0]
t2=t[1]

import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import csv

def get_driver(browser:str = "firefox") -> webdriver:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(current_dir)
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=current_dir + "\\chromedriver.exe")
    else:
        driver = webdriver.Firefox(executable_path=current_dir + "\\geckodriver.exe")
    # Maximum Wait time to find elements in page (in order to let them load first)
    driver.implicitly_wait(10)

    return driver


driver = get_driver("chrome")
driver.get('http://cbseaff.nic.in/cbse_aff/schdir_Report/AppViewdir.aspx?affno=2520097')
time.sleep(5)
name_of_institution = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[3]/td[2]').text
print(name_of_institution)
affiliation_number = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[4]/td[2]').text
print(affiliation_number)
state = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[5]/td[2]').text
print(state)
district = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[6]/td[2]').text
print(district)
postal_address = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[7]/td[2]').text
print(postal_address)
pin_code = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[8]/td[2]').text
print(pin_code)
std_code = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[9]/td[2]').text
print(std_code)
office_phone_no = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[10]/td[2]').text
print(office_phone_no)
residence_phone_no = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[11]/td[2]').text
print(residence_phone_no)
fax_no = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[12]/td[2]').text
print(fax_no)
email = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[13]/td[2]').text
print(email)
website = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[14]/td[2]').text
print(website)
year_of_foundation = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[15]/td[2]').text
print(year_of_foundation)
date_of_first_opening_of_school = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[16]/td[2]').text
print(date_of_first_opening_of_school)
name_of_principal_head_of_institution = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[17]/td[2]').text
    #print(name_of_principal_head_of_institution)
sex = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[18]/td[2]').text
    #print(sex)
principals_educational_professional_qualifications = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[19]/td[2]').text
    #print(principals_educational_professional_qualifications)
administrative_no_of_experience_in_years = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[21]/td[2]').text
    #print(administrative_no_of_experience_in_years)
teaching_no_of_experience_in_years = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[22]/td[2]').text
    #print(teaching_no_of_experience_in_years)
status_of_the_school = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[23]/td[2]').text
    #print(status_of_the_school)
try:
    type_of_affiliation = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[24]/td[2]').text
except Exception:
    pass
    #print(type_of_affiliation)
affiliation_period_from = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[26]/td[2]').text
    #print(affiliation_period_from)
affiliation_period_to = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[27]/td[2]').text
    #print(affiliation_period_to)
name_of_trust_society_managing_committee = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[28]/td[2]').text
    #print(name_of_trust_society_managing_committee)
driver.close()






/html/body/div[2]/table/tbody/tr[22]/td[2]
/html/body/div[2]/table/tbody/tr[23]/td[2]
/html/body/div[2]/table/tbody/tr[25]/td[2]
/html/body/div[2]/table/tbody/tr[27]/td[2]
















