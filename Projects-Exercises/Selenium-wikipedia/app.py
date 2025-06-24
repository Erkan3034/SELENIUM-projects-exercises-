from selenium import webdriver
import time

browser = webdriver.Chrome() # Chrome tarayıcısını aç

url = "https://tr.wikipedia.org/wiki/%C4%B0stanbul"

browser.get(url) # Sayfayı aç

time.sleep(10) # 10 saniye bekle 

browser.close() # Tarayıcıyı kapat
