#Import packages
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import time
import os

#fetching locus ids from excel file
os.chdir('D:/_IRRI-SOUTH ASIA/Team_works/Dr_Niran/Task - 6') #Set working directory
print("*****Automation Script for extracting haplotypic information*****")
print("\n Please upload, list of locus id......")
time.sleep(5)

df = pd.read_csv('genes.csv') #pass your genes filename
print("\n\n Your locus ids are following:")

#Pass loc_id or csv file containing loc_ids
df = df.iloc[0:,0] #Slicing and converting in desired format
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
            time.sleep(10) #Make the next line comment if dont want to take indels 
            checkbox = open_tab.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[3]/div/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/table/tbody[1]/tr[5]/td[2]/div/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td[1]/div/span[5]/input')
            checkbox.click() #clicking
            time.sleep(10) #Next line will decide whether to take non-synonymous only or not (if comment it wont take - it will take all SNPs)
            radio_button = open_tab.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[3]/div/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/table/tbody[1]/tr[5]/td[2]/div/table/tbody/tr/td/table/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr/td[17]/span/input')
            radio_button.click()  #Next line will click on search button
            search_button = open_tab.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[3]/div/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/table/tbody[1]/tr[5]/td[3]/div/table/tbody/tr/td/table/tbody/tr[1]/td/button')
            search_button.click()
            time.sleep(50)#wait for loading next page - giving a 50seconds break
            generative_csv_file = open_tab.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[3]/div/table/tbody/tr/td/table/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[3]/td/div/div[2]/div[1]/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td[3]/button')
            generative_csv_file.click() #downloading csv file, change the above xpath accordinlgy if you want to change the type of downloading file
            time.sleep(50)
            open_tab.close() #close the tab
          
        except:
            print('An error occured at',locus_id)
            continue

    print("Haplotypic data successfully downloaded!")
automate_SNP(df)
