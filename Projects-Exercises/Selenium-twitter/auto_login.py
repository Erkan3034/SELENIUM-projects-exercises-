from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome() # Chrome tarayıcısını aç 

url = "https://x.com/" # ana url adresi

browser.get(url) # url'e gidiyoruz

time.sleep(2) # 5 saniye bekliyoruz 



giris_yap_butonu = browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div')

giris_yap_butonu.click() # giriş yap butonuna TIKLA

time.sleep(5) # 5 saniye bekliyoruz 

try:
    kullanici_adi_kutusu = browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[4]/label/div/div[2]/div/input')
    kullanici_adi_kutusu.send_keys("Erkan_0630") # kullanıcı adını yazdır
    print("Kullanıcı adı başarıyla girildi!")
except NoSuchElementException:
    print("Element bulunamadı! XPATH güncellenmeli.")
    print("Alternatif yöntemler deneniyor...")
    
    # Farklı XPATH'ler deneyelim
    alternatif_xpaths = [
        '//input[@name="text"]',
        '//input[@autocomplete="username"]',
        '//input[contains(@placeholder, "kullanıcı")]',
        '//input[contains(@placeholder, "username")]'
    ]
    
    element_bulundu = False
    for xpath in alternatif_xpaths:
        try:
            kullanici_adi_kutusu = browser.find_element(By.XPATH, xpath)
            kullanici_adi_kutusu.send_keys("Erkan_0630")
            print(f"Alternatif XPATH ile başarılı: {xpath}")
            element_bulundu = True
            print("Kullanıcı adı başarıyla girildi!")
            break
        except NoSuchElementException:
            continue
    
    if not element_bulundu:
        print("Hiçbir alternatif XPATH çalışmadı. Manual inceleme gerekli.")
        browser.quit()
        exit()

# İleri butonuna tıkla
time.sleep(2)
print("İleri butonunu arıyor...")

try:
    iler_butonu = browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/button[2]/div')
    iler_butonu.click()
    print("İleri butonuna başarıyla tıklandı!")
except NoSuchElementException:
    print("İleri butonu bulunamadı! Alternatif yöntemler deneniyor...")
    
    # İleri butonu için alternatif XPATH'ler
    alternatif_iler_xpaths = [
        '//button//span[text()="Next"]/..',
        '//button//span[text()="İleri"]/..',
        '//button[contains(text(), "Next")]',
        '//button[contains(text(), "İleri")]',
        '//div[@role="button"]//span[text()="Next"]/../..',
        '//div[@role="button"]//span[text()="İleri"]/../..'
    ]
    
    iler_bulundu = False
    for xpath in alternatif_iler_xpaths:
        try:
            iler_butonu = browser.find_element(By.XPATH, xpath)
            iler_butonu.click()
            print(f"İleri butonu alternatif XPATH ile bulundu: {xpath}")
            iler_bulundu = True
            break
        except NoSuchElementException:
            continue
    
    if not iler_bulundu:
        print("İleri butonu hiç bulunamadı!")
        browser.quit()
        exit()

# Şifre kutusunu bekle ve doldur
time.sleep(3)
print("Şifre kutusunu arıyor...")

try:
    sifre_kutusu = browser.find_element(By.XPATH, '//input[@name="password"]')
    sifre_kutusu.send_keys("sifre")  # şifre kutusunu doldur
    print("Şifre başarıyla girildi!")
except NoSuchElementException:
    print("Şifre kutusu bulunamadı! Altrnatif yöntemler deneniyor...")
    
    # Şifre kutusu için alternatif XPATH'ler
    alternatif_sifre_xpaths = [
        '//input[@type="password"]',
        '//input[contains(@placeholder, "Password")]',
        '//input[contains(@placeholder, "Şifre")]',
        '//input[contains(@autocomplete, "password")]'
    ]
    
    sifre_bulundu = False
    for xpath in alternatif_sifre_xpaths:
        try:
            sifre_kutusu = browser.find_element(By.XPATH, xpath)
            sifre_kutusu.send_keys("sifre")  # Şifrenizi buraya yazın
            print(f"Şifre kutusu alternatif XPATH ile bulundu: {xpath}")
            sifre_bulundu = True
            break
        except NoSuchElementException:
            continue
    
    if not sifre_bulundu:
        print("Şifre kutusu hiç bulunamadı!")
        browser.quit()
        exit()

# Giriş butonuna tıkla
time.sleep(20)
print("Giriş butonunu arıyor...")

try:
    giris_butonu = browser.find_element(By.XPATH, '//button[contains(@role, "button")]//span[text()="Giriş yap" or text()="Log in"]/..')
    giris_butonu.click()
    print("Giriş butonuna başarıyla tıklandı!")
except NoSuchElementException:
    print("Giriş butonu bulunamadı! Alternatif yöntemler deneniyor...")
    
    # Giriş butonu için alternatif XPATH'ler
    alternatif_giris_xpaths = [
        '//button//span[text()="Log in"]/..',
        '//button//span[text()="Giriş yap"]/..',
        '//button[contains(text(), "Log in")]',
        '//button[contains(text(), "Giriş")]',
        '//div[@role="button"]//span[text()="Log in"]/../..',
        '//div[@role="button"]//span[text()="Giriş yap"]/../..'
    ]
    
    giris_bulundu = False
    for xpath in alternatif_giris_xpaths:
        try:
            giris_butonu = browser.find_element(By.XPATH, xpath)
            giris_butonu.click()
            print(f"Giriş butonu alternatif XPATH ile bulundu: {xpath}")
            giris_bulundu = True
            break
        except NoSuchElementException:
            continue
    
    if not giris_bulundu:
        print("Giriş butonu hiç bulunamadı!")
        browser.quit()
        exit()

print("✅ Giriş işlemi tamamlandı! Ana sayfaya yönlendiriliyor...")
time.sleep(10)  # Giriş işleminin tamamlanması için bekle

# İsteğe bağlı: Başarılı giriş kontrolü
try:
    # Giriş yapıldığında görünen bir element kontrol et (örnek)
    ana_sayfa_elementi = browser.find_element(By.XPATH, '//nav[@role="navigation"]')
    print("🎉 Başarıyla giriş yapıldı! Ana sayfadasınız.")
except NoSuchElementException:
    print("⚠️ Giriş durumu belirsiz. Manuel kontrol edin.")

time.sleep(5)  # Son kontrol için bekle




