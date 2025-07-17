from selenium import webdriver
import time, random
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()


url = "https://eksisozluk.com/istanbul--32102?p=" # İstanbul konuslu gönderileri al

pageCount = 1
entries = [] # Gönderileri sakla

while pageCount <= 10:
    randomPage = random.randint(1, 1341)
    newUrl = url + str(randomPage)  # Rastgele yerine sıralı
    print(f"Gidilen sayfa: {pageCount}")
    print(browser.current_url)
    browser.get(newUrl)
    time.sleep(3)
    
    elements = browser.find_elements(By.CSS_SELECTOR, ".content")
    for element in elements:
<<<<<<< HEAD
        entries.append(element.text)
        print(element.text)

        with open("entries.txt", "a", encoding="utf-8") as file: # entrileri txt dosyasına yaz
            file.write(element.text + "\n")
    print("--------------------------------")
=======
        entries.append(element.text) # Gönderileri sakla
        print(element.text) # Gönderileri yazdır
    print("--------------------------------") # Sayfa numarasını yazdir
>>>>>>> 494e0d2b992bead1034e53f3afedfd671f360f52
    print(f"Sayfa {pageCount} gönderileri alındı")
    pageCount += 1


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
