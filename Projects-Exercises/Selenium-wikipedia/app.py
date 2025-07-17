from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome() # Chrome tarayıcısını aç (Chrome tarayıcısını kullanıyoruz)

url = "https://tr.wikipedia.org/wiki/%C4%B0stanbul"  # İstanbul sayfasının URL'sini belirliyoruz



browser.get(url) # Sayfayı aç (Sayfayı açıyoruz) 

time.sleep(5) # 5 saniye bekle (5 saniye bekliyoruz)

elements = browser.find_elements(By.CSS_SELECTOR, "div.mw-heading.mw-heading3 > h3") # h3 etiketini seç (h3 etiketini seçiyoruz)

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