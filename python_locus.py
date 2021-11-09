# -*- coding: utf-8 -*-
"""
Created on Wednesday; by Ajay Kumar (xenificity)
PYTHON AUTOMATION SCRIPT - FOR DOWNLOADING DATA FROM IRRI SNP PLATFORM.
"""
#Import packages
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import time
import os

#fetching locus ids from excel file
os.chdir('D:/_IRRI-SOUTH ASIA/Colleague_queries/Dr_Krishna')
print("*****Automation Script for extracting haplotypic information*****")
print("\n Please upload, list of locus id......")
time.sleep(5)

df = pd.read_csv('loc_list.csv') 
print("\n\n Your locus ids are following:")

#Pass loc_id or csv file containing loc_ids
df = df.iloc[:,0]
print(df)
print("\n\n Your data is starting to download, please wait.!")
time.sleep(4)

#For each loc_id, script will execute and download the corresponding dataset
def automate_SNP(df):
    for x in df:
        locus_id = x #Each loc_id
        print("\n\n")
        print("Downloading data for \t",locus_id)
        #passing url here
        try:
            file_url = r'https://snp-seek.irri.org/_snp.zul;jsessionid=4D237C971AA61F835FFDC69C5DDB9DCC'
            open_tab = webdriver.Chrome()
            #driver = webdriver.Chrome(executable_path='D:/_IRRI-SOUTH ASIA/Breeding for Crop Improvement Training - IRRI CGIAR/Breeding for Crop Improvement Training/Automation_python_script_Ajay/88.0.4324.104_chrome_installer.exe') #note here you should have installed webdriver for opening browser
            open_tab.get(file_url) #opening tab here
            input_box =open_tab.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[3]/div/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/table/tbody[1]/tr[4]/td[2]/div/table/tbody/tr/td/table/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr/td[3]/span/input')
            input_box.send_keys(locus_id)
            time.sleep(4)
            checkbox = open_tab.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[3]/div/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/table/tbody[1]/tr[5]/td[2]/div/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td[1]/div/span[5]/input')
            checkbox.click()
            time.sleep(3)
            radio_button = open_tab.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[3]/div/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/table/tbody[1]/tr[5]/td[2]/div/table/tbody/tr/td/table/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr/td[17]/span/input')
            radio_button.click()
            search_button = open_tab.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[3]/div/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/table/tbody[1]/tr[5]/td[3]/div/table/tbody/tr/td/table/tbody/tr[1]/td/button')
            time.sleep(15)
            search_button.click()
            time.sleep(35) #wait for loading next page
            generative_csv_file = open_tab.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[3]/div/table/tbody/tr/td/table/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[3]/td/div/div[2]/div[1]/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td[3]/button')
            generative_csv_file.click()
            time.sleep(45)
            open_tab.close() #close the tab
            list_of_files = os.listdir('C:/Users/91981/Downloads')
            for each_file in list_of_files:
                if each_file.startswith('snp3kvars'):  #since its all type str you can simply use startswith
                    print(each_file)
            os.rename(r'C:/Users/91981/Downloads/{}'.format(each_file),r'C:/Users/91981/Downloads/{}.csv'.format(locus_id)) #enter desired path for downloaded file
            #download the csv output file 
        except:
            print('An error occured at',locus_id)
            continue

    print("Haplotypic data successfully downloaded!")
automate_SNP(df)


'''

#brainstorming

first = pd.read_excel(r'C:/Users/91981/Downloads/all files in one folder/.xlsx')
second = pd.read_excel(r'C:/Users/91981/Downloads/1000-1500 batch genes.xlsx')

genes_ajay_3k = pd.read_excel(r"C:/Users/91981/Documents/genes_ajay_3k.xlsx")
for x in genes_ajay_3k:
     file = pd.read_csv(r"C:/Users/91981/Downloads/all_files/{}.csv".format(x))
     print(file)
     
list_of_files = os.listdir('C:/Users/91981/Downloads/all_files')
for each_file in list_of_files:
    file = pd.read_csv("C:/Users/91981/Downloads/all_files/{}".format(x))
'''

