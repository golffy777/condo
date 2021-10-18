from selenium.webdriver.common.keys import Keys
import time
import re
import pandas as pd
import bs4
import requests
from selenium import webdriver
import numpy as np
import pyautogui

driver = webdriver.Chrome(executable_path=r'chromedriver.exe')

driver.get('https://eclaim3.emcsthai.com/esurvey/frmLogin.aspx')
driver.maximize_window()
dcwh = driver.current_window_handle
driver.find_element_by_id('txtUserName').send_keys('noppadol@se.co.th')
driver.find_element_by_id('txtPassWord').send_keys('Sesurvey1501*')
driver.find_element_by_id('imbLogin').click()
driver.find_element_by_id('btnEnter').click()


allhandle_windows = driver.window_handles
for handle in allhandle_windows:
    if handle != dcwh:
        driver.switch_to_window(dcwh)


driver.find_element_by_id('dgvInbox_ctl03_sname').click()

day = '04'
month = '/ก.ย./'
year = '2564'

all_data = []
all_day = []
page = 2
i = 0

def load_data():
    data = driver.find_elements_by_xpath('//*[@id="dgvList"]/tbody/tr')
    return data

for c in range(1):
    #data = driver.find_elements_by_xpath('//*[@id="dgvList"]/tbody/tr')
    for count, value in enumerate(load_data):
        if count > 0 and count < 16:
            all_data.append(value.text)
            
            data_frame = pd.DataFrame(all_data)
            data_frame.columns = ['Table']

            dm = data_frame.Table.str.extract(
                '(\d\d\D{6}\d{4}\s\d\d\W\d\d)(\D\D\d{11}\s\s\D)')
            dm.columns = ['Day/Time', 'e-Survey']
            dmc = data_frame.Table.str.extract('(.+)SEAIO')
            dmc.columns = ['DayMonthClaim']
            dmytc = dmc.DayMonthClaim.str.extract(
                '(\d\d)(\D{6})(\d{4})(\s\d\d\W\d\d)(\D\D\d{11})')
            dmytc.columns = ['Day', 'Month', 'Year', 'Time', 'Claim']


            d = dmytc['Day'].values
            m = dmytc['Month'].values
            t = dmytc['Time'].values
            y = dmytc['Year'].values
            c = dmytc['Claim'].values

            d_list = list(df_s['Day'].values)
            m_list = list(df_s['Month'].values)
            t_list = list(df_s['Time'].values)
            y_list = list(df_s['Year'].values)
            c_list = list(df_s['Claim'].values)

            

            
    
            while i < 500:
                if d[i] == day :
                    all_day.append((d[i], m[i], y[i], c[i]))
                    #driver.find_element_by_xpath('//*[@id="dgvList_ctl02_lkbSrRefID"]').click()
                    
                    

                i += 1
                break



