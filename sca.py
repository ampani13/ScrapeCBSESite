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
from selenium.webdriver.common.keys import Keys
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

def scrape_page(driver: webdriver, link: str, data):
    driver.execute_script("window.open('');")
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    driver.get(link)
    time.sleep(5)
    start = 3
    try:
        name_of_institution = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 1
    except NoSuchElementException:
        name_of_institution = ''
        start = start - 1
        print(name_of_institution)
    try:
        affiliation_number = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 1
    except NoSuchElementException:
        #print('affiliation_number')
        affiliation_number = ''
        start = start - 1
        print(affiliation_number)
    try:
        state = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 1
    except NoSuchElementException:
        #print('state')
        state = ''
        start = start - 1
        print(state)
    try:
        district = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 1
    except NoSuchElementException:
        #print('district')
        district = ''
        start = start - 1
        print(district)
    try:
        postal_address = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 1
    except NoSuchElementException:
        #print('postal_address')
        postal_address = '' 
        start = start - 1
        print(postal_address)
    try:
        pin_code = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 1
    except NoSuchElementException:
        #print('pin_code')
        pin_code = ''
        start = start - 1
        print(pin_code)
    try:
        std_code = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 1
    except NoSuchElementException:
        #print('std_code')
        std_code = ''
        start = start - 1
        print(std_code)
    try:
        office_phone_no = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 1
    except NoSuchElementException:
        #print('office_phone_no')
        office_phone_no = ''
        start = start - 1
        print(office_phone_no)
    try:
        residence_phone_no = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 1
    except NoSuchElementException:
        #print('residence_phone_no')
        residence_phone_no = ''
        start = start - 1
        print(residence_phone_no)
    try:
        fax_no = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 1
    except NoSuchElementException:
        #print('fax_no')
        fax_no = ''
        start = start - 1
        print(fax_no)
    try:
        email = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 1
    except NoSuchElementException:
        #print('email')
        email = ''
        start = start - 1
        print(email)
    try:
        website = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 1
    except NoSuchElementException:
        #print(website)
        website = ''
        start = start - 1
        print(website)
    try:
        year_of_foundation = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 1
    except NoSuchElementException:
        #print(year_of_foundation)
        year_of_foundation = ''
        start = start - 1
        print(year_of_foundation)
    try:
        date_of_first_opening_of_school = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 1
    except NoSuchElementException:
        #print(date_of_first_opening_of_school)
        date_of_first_opening_of_school = ''
        start = start - 1
        print(date_of_first_opening_of_school)
    try:
        name_of_principal_head_of_institution = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 1
    except NoSuchElementException:
        #print(name_of_principal_head_of_institution)
        name_of_principal_head_of_institution = ''
        start = start - 1
        print(name_of_principal_head_of_institution)
    try:
        sex = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 1
    except NoSuchElementException:
        #print(sex)
        sex = ''
        start = start - 1
        print(sex)
    try:
        principals_educational_professional_qualifications = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 2
    except NoSuchElementException:
        #print(principals_educational_professional_qualifications)
        principals_educational_professional_qualifications = ''
        start = start - 1
        print(principals_educational_professional_qualifications)
    try:
        administrative_no_of_experience_in_years = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 1
    except NoSuchElementException:
        #print(administrative_no_of_experience_in_years)
        administrative_no_of_experience_in_years = ''
        start = start - 1
        print(administrative_no_of_experience_in_years)
    try:
        teaching_no_of_experience_in_years = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 1
    except NoSuchElementException:
        #print(teaching_no_of_experience_in_years)
        teaching_no_of_experience_in_years = ''
        start = start - 1
        print(teaching_no_of_experience_in_years)
    try:
        status_of_the_school = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 1
    except NoSuchElementException:
        #print(status_of_the_school)
        status_of_the_school = ''
        start = start - 1
        print(status_of_the_school)
    try:
        type_of_affiliation = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 2
    except NoSuchElementException:
        #print(type_of_affiliation)
        type_of_affiliation = ''
        start = start - 1
        print(type_of_affiliation)
    try:
        affiliation_period_from = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 1
    except NoSuchElementException:
        #print(affiliation_period_from)
        affiliation_period_from = ''
        start = start - 1
        print(affiliation_period_from)
    try:
        affiliation_period_to = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 1
    except NoSuchElementException:
        #print(affiliation_period_to)
        affiliation_period_to = ''
        start = start - 1
        print(affiliation_period_to)
    try:
        name_of_trust_society_managing_committee = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr['+ str(start) +']/td[2]').text
        start = start + 1
    except NoSuchElementException:
        #print(name_of_trust_society_managing_committee)
        name_of_trust_society_managing_committee = ''
        start = start - 1
        print(name_of_trust_society_managing_committee)
    driver.close()
    
    data.append([name_of_institution, affiliation_number, state,
                             district, postal_address, pin_code, std_code, office_phone_no,
                             residence_phone_no, fax_no, email, website, year_of_foundation,
                             date_of_first_opening_of_school, name_of_principal_head_of_institution,
                             sex, principals_educational_professional_qualifications,
                             administrative_no_of_experience_in_years,
                             teaching_no_of_experience_in_years,
                             status_of_the_school, type_of_affiliation, affiliation_period_from,
                             affiliation_period_to, name_of_trust_society_managing_committee])
    with open('schools_affiliated_tst.csv', 'a') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        filewriter.writerow([name_of_institution, affiliation_number, state,
                             district, postal_address, pin_code, std_code, office_phone_no,
                             residence_phone_no, fax_no, email, website, year_of_foundation,
                             date_of_first_opening_of_school, name_of_principal_head_of_institution,
                             sex, principals_educational_professional_qualifications,
                             administrative_no_of_experience_in_years,
                             teaching_no_of_experience_in_years,
                             status_of_the_school, type_of_affiliation, affiliation_period_from,
                             affiliation_period_to, name_of_trust_society_managing_committee])
    # Switch back to the first tab
    driver.switch_to.window(driver.window_handles[0])
    return data


def scrape_column(driver: webdriver, data: list):
    for i in range(2,27):
        try:
            serial_no = driver.find_element_by_xpath('//*[@id="T1"]/tbody/tr/td/table['+str(i)+']/tbody/tr/td[1]').text
            school_info = driver.find_element_by_xpath('//*[@id="T1"]/tbody/tr/td/table['+str(i)+']/tbody/tr/td[2]/table/tbody')
            page_link = school_info.find_element_by_xpath('//*[@id="T1"]/tbody/tr/td/table['+str(i)+']/tbody/tr/td[2]/table/tbody/tr[2]/td/a').get_attribute('href')
        except NoSuchElementException:
            print('-serial_no-'+'school_info-'+'page_link-')
            break
        #print(serial_no)
        #print(school_info.text)
        print('link: '+page_link)
        data=scrape_page(driver, page_link,data)
        #print(data)
        time.sleep(3)
    return serial_no,data

def condition_scrape_column(driver: webdriver, total :int, data : list):
    output = scrape_column(driver,data)
    serial_no = output[0]
    serial_no = int(serial_no)
    data = output[1]
    print(serial_no)
    print(type(total))
    print(serial_no<total)
    #print('n '+data)
    click=0
    print('n 1')
    while serial_no<total:
        print('n 2')
        click += 1
        element_ahead = driver.find_element_by_xpath('//*[@id="Button1"]')
        driver.execute_script('arguments[0].click();', element_ahead)
        output = scrape_column(driver,data)
        serial_no = output[0]
        serial_no = int(serial_no)
        data = output[1]
    while(click>0):
        element_back = driver.find_element_by_xpath('//*[@id="Button2"]')
        driver.execute_script('arguments[0].click();', element_back)
        click -=1
    return data

    
def scarpe_cbse(no :int):
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
        print('scarpe_cbse')
        driver.quit()
        print("Loading of page " + str(driver) + " took too much time!")
    #print('fnd')
    time.sleep(5)
    # select state-wise radio button
    state_wise = driver.find_element_by_xpath('//*[@id="optlist_2"]')
    state_wise.click()
    time.sleep(5)
    data=[['Name of Institution', 'Affiliation Number', 'State', 'District',
                             'Postal Address', 'Pincode', 'Std Code', 'Office Phone No',
                             'Residence Phone No', 'Fax No', 'Email', 'Website', 'Year of Foundation',
                             'Date of First Opening of School', 'Name of Principal/Head of Institution',
                             'Sex', 'Principals Educational Professional Qualifications',
                             'Administrative No of Experience(in Years)',
                             'Teaching No of Experience(in Years)',
                             'Status of the School', 'Type of Affiliation',
                             'Affiliation Period From', 'Affiliation Period To',
                             'Name of Trust/Society/Managing Committee']]
    print(data)
    with open('schools_affiliated_tst.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        filewriter.writerow(['Name of Institution', 'Affiliation Number', 'State', 'District',
                             'Postal Address', 'Pincode', 'Std Code', 'Office Phone No',
                             'Residence Phone No', 'Fax No', 'Email', 'Website', 'Year of Foundation',
                             'Date of First Opening of School', 'Name of Principal/Head of Institution',
                             'Sex', 'Principals Educational Professional Qualifications',
                             'Administrative No of Experience(in Years)',
                             'Teaching No of Experience(in Years)',
                             'Status of the School', 'Type of Affiliation',
                             'Affiliation Period From', 'Affiliation Period To',
                             'Name of Trust/Society/Managing Committee'])
    
    for state in range(2,100):
        state_='//*[@id="ddlitem"]/option['+str(state)+']'
        try:
            state_select = driver.find_element_by_xpath(state_)
        except NoSuchElementException:
            print('state_select')
            break
        state_select.click()
        #print(state_select.text())
        time.sleep(2)
        for district in range(2,100):
            district_='//*[@id="DropDownDistrict"]/option['+str(district)+']'
            try:
                district_select = driver.find_element_by_xpath(district_)
            except NoSuchElementException:
                print('district_select')
                break
            district_select.click()
            #print(district_select.text())
            driver.find_element_by_xpath('//*[@id="search"]').click()
            time.sleep(5)
            #print(district_select.text)
            #print(state_select.text)
            try:
                #state_name = driver.find_element_by_xpath('//*[@id="Lbltype1"]').text
                #district_name = driver.find_element_by_xpath('//*[@id="lbltotal"]').text
                #district_name = district_name[:-1]
                #district_name = district_name.split()
                #district_name=district_name[6:len(district_name)]
                #final_district_name=''
                #for sr in district_name:
                    #final_district_name+=sr+' '
                #print(state_name+' '+final_district_name)
                total = driver.find_element_by_xpath('//*[@id="tot"]').text
                total = int(total)
                #print('total: '+total)
                data=condition_scrape_column(driver, total,data)
                
            except NoSuchElementException:
                print('-total-'+'data-')
                continue 
    file_name='schools_affiliated_'+str(no)+'.csv'    
    with open(file_name, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    driver.quit()

if __name__ == "__main__":
    print('started...')
    no = input("Enter a no below 100? ")
    no = int(no)
    print(type(no))
    scarpe_cbse(no);
    print('done...')

