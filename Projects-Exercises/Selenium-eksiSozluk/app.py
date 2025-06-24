from selenium import webdriver
import time, random
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()


url = "https://eksisozluk.com/istanbul--3210?p=" # İstanbul konuslu gönderileri al

pageCount = 1
entries = [] # Gönderileri sakla

while pageCount <= 10:
    randomPage = random.randint(1, 1341) # Sayfa numarasını rastgele seç
    newUrl = url + str(randomPage) # Sayfa numarasını rastgele seç(url sonundaki p= sayfa numarası)
    browser.get(newUrl) # Sayfayı aç
    time.sleep(3) # 3 saniye bekle
    elements = browser.find_elements(By.CSS_SELECTOR, ".content")  # content etiketini seç ve listele
    for element in elements:
        entries.append(element.text) # Gönderileri sakla
        print(element.text) # Gönderileri yazdır
    print("--------------------------------") # Sayfa numarasını yazdır
    print(f"Sayfa {pageCount} gönderileri alındı")
    pageCount += 1 # Sayfa numarasını artır
print("--------------------------------")
print("Tüm gönderiler alındı")


"""
browser.get(url)

elements = browser.find_elements(By.CSS_SELECTOR, ".content")  # content etiketini seç

i=1
for element in elements:
    print(f"{i} - {element.text}")
    i += 1

time.sleep(10)

browser.close()


"""