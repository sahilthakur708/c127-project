from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome('C:/Users/admin/OneDrive/Desktop/c127 project/chromedriver.exe')
browser.get(start_url)

time.sleep(10)

def scrape ():
    headers=['Proper name','Distance (ly)','Mass (M☉)','Radius (R☉)']
    stars_data=[]

    for i in range (0,5):
        soup=BeautifulSoup(browser.page_source,'html.parser')
        for tr_tag in soup.find_all('tr'):
            td_tags=ul_tag.find_all('td')
            temp_list=[]

            for index,td_tag in enumerate(td_tags):
                if index==0:
                    temp_list.append(td_tag.find_all('a')[0].contents[0])
                
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    
                    except:
                        temp_list.append("")

            stars_data.append(temp_list)
    
    with open('data.csv','w') as f:
        csv_writer=csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(stars_data)

scrape()

