import time
from time import sleep

from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from tqdm import tqdm

#Открывает браузер и ищет статьи в поиске "парсинг"
browser = Chrome('/Users/Мария/Desktop/chromedriver')
url = 'https://cyberleninka.ru/'
browser.get(url)
input_tab = browser.find_element_by_tag_name('input')
input_tab.send_keys('парсинг')
button = browser.find_element_by_class_name('search-btn')
button.click()
time.sleep(5)
#названия статей
num = 5
soup = BeautifulSoup(browser.page_source, "lxml")

i = 1
file = open('DB.txt', 'w', encoding='utf-8')
while i<2:
    num=1
    while num<11:
                                                               
        book_name = browser.find_element_by_xpath("//*[@id='search-results']/li["+ str(num) +"]/h2/a") #название статьи
        autor = browser.find_element_by_xpath("//*[@id='search-results']/li["+ str(num) +"]/span[1]") #автор(ы)
        annotation = browser.find_element_by_xpath("//*[@id='search-results']/li["+ str(num) +"]/div")#аннотация
   
        file.write("Статья №"+str(num)+"\n")
        file.write(book_name.text.strip()+'\n')
        file.write(autor.text.strip()+'\n')
        file.write(annotation.text.strip()+'\n')
        num += 1
    i+=1
    button_two=browser.find_element_by_xpath('//*[@id="body"]/div[3]/div/div[1]/ul/li[2]/a')
    button_two.click()
    
