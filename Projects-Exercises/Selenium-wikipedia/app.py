from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome() # Chrome tarayıcısını aç

url = "https://tr.wikipedia.org/wiki/%C4%B0stanbul"



browser.get(url) # Sayfayı aç.

time.sleep(5) # 10 saniye bekle sayfadayken

elements = browser.find_elements(By.CSS_SELECTOR, "div.mw-heading.mw-heading3 > h3") # h3 etiketini seç

i = 1    
print("------------- BASLIKLAR-------------------")
for element in elements:
    print(f"{i} - {element.text}")
    i += 1
print("--------------------------------")
    
browser.close() # Tarayıcıyı kapat


"""
Bu kod ile wikipedia sayfsaını açıp İstanbul sayfasının h3 etiketlerini alıyoruz.

"""
