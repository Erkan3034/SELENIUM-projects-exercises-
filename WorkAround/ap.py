from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# WebDriver'ın yolu (eğer PATH'e ekli değilse tam yol yazılmalı)
driver = webdriver.Chrome()  # Chrome kullanıyorsan ChromeDriver yüklü olmalı

# 1. Google'a git
driver.get("https://www.google.com")

# 2. Çerezleri kabul et (Google bazen soruyor)
try:
    accept_button = driver.find_element(By.XPATH, "//button[text()='Kabul et']")
    accept_button.click()
except:
    pass  # Çıkmazsa devam et

# 3. Arama kutusunu bul ve yazı yaz
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python Nedir")
search_box.send_keys(Keys.RETURN)  # Enter tuşu

# 4. Sonuçların yüklenmesini bekle
time.sleep(3)

# 5. Başlıkları yazdır
results = driver.find_elements(By.XPATH, "//h3")
for result in results[:5]:  # İlk 5 başlığı yazdıralım
    print(result.text)

# 6. Tarayıcıyı kapat
driver.quit()
