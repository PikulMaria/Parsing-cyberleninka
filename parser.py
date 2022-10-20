#Пикуль Мария гр. P4109
import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait as wait


browser = Chrome('/Users/Мария/Desktop/chromedriver')
a=0

i = 1
file = open('DB.txt', 'a', encoding='utf-8')
while i<11:
    url = "https://cyberleninka.ru/search?q=парсинг&page="+str(i)
    browser.get(url)
    time.sleep(3)
    num=1
    while num<11:
               
        book_name = browser.find_element_by_xpath("//*[@id='search-results']/li["+ str(num) +"]/h2/a") #название статьи
        autor = browser.find_element_by_xpath("//*[@id='search-results']/li["+ str(num) +"]/span[1]") #автор(ы)
        annotation = browser.find_element_by_xpath("//*[@id='search-results']/li["+ str(num) +"]/div")#аннотация
        a+=1
        file.write("Статья №"+ str(a) +"\n")
        file.write(book_name.text.strip()+'\n')
        file.write(autor.text.strip()+'\n')
        file.write(annotation.text.strip()+'\n')
        print(book_name.text.strip())
        num += 1
    i+=1
 
