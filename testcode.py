from selenium.webdriver.common.keys import Keys
import time
import re
import pandas as pd
from bs4 import BeautifulSoup
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

def change_page():
    driver.find_element_by_xpath('//*[@id="ddlPage"]/option[2]').click()

def print_pdf():
    print('pdf')

def print_report():
    print('report')

def print_invoice():
    print('invoice') 

for c in range(1):
#data = driver.find_elements_by_xpath('//*[@id="dgvList"]/tbody/tr')
    for count, value in enumerate(load_data()):
        if count > 0 and count < 16:
            all_data.append(value.text)
            data_frame = pd.DataFrame(all_data)
            data_frame.columns = ['Table']

            df_splite = data_frame.Table.str.extract('(\d\d)(\D{6})(\d{4})(\s)(\d\d\W\d\d)(\s)(\D\d{11})')
            df_splite.columns = ['Day', 'Month', 'Year','blank1', 'Time', 'blank2', 'Claim']
            df_s = df_splite.drop(columns=['blank1', 'blank2'])

            d = df_s['Day'].values
            m = df_s['Month'].values
            t = df_s['Time'].values
            y = df_s['Year'].values
            c = df_s['Claim'].values

            d_list = list(df_s['Day'].values)
            m_list = list(df_s['Month'].values)
            t_list = list(df_s['Time'].values)
            y_list = list(df_s['Year'].values)
            c_list = list(df_s['Claim'].values)




# driver.find_element_by_xpath('//*[@id="dgvList_ctl02_lkbSrRefID"]').click()
# driver.find_element_by_xpath('//*[@id="wuMenuPage1_imbImage"]').click()
# driver.find_element_by_xpath('//*[@id="btnShow_Image2"]').click()

# pyautogui.rightClick(500,500)
# pyautogui.click(498,471)

