from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Enter tuşu için
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

print("🚀 Twitter Hashtag Arama Botu Başlatılıyor...")
print("📝 İlk önce Twitter'a giriş yapacağız, sonra hashtag araması yapacağız")

# Chrome tarayıcısını başlat
browser = webdriver.Chrome()

# Twitter/X ana sayfasına git
url = "https://x.com/"
print(f"📱 {url} adresine gidiliyor...")
browser.get(url)
time.sleep(2)

print("\n🔐 GİRİŞ İŞLEMİ BAŞLIYOR...")

# Giriş yap butonuna tıkla
try:
    giris_yap_butonu = browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div')
    giris_yap_butonu.click()
    print("✅ 'Giriş Yap' butonuna tıklandı!")
except NoSuchElementException:
    print("❌ 'Giriş Yap' butonu bulunamadı!")
    browser.quit()
    exit()

time.sleep(5)

# Kullanıcı adı girişi
print("👤 Kullanıcı adı giriliyor...")
try:
    kullanici_adi_kutusu = browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[4]/label/div/div[2]/div/input')
    kullanici_adi_kutusu.send_keys("Erkan_0630")  #kullanıcı adı 
    print("✅ Kullanıcı adı başarıyla girildi!")
except NoSuchElementException:
    print("❌ Kullanıcı adı kutusu bulunamadı! Alternatif yöntemler deneniyor...")
    
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
            kullanici_adi_kutusu.send_keys("Erkan_0630")  #kullanıcı adı 
            print(f"✅ Alternatif XPATH ile başarılı: {xpath}")
            element_bulundu = True
            break
        except NoSuchElementException:
            continue
    
    if not element_bulundu:
        print("❌ Kullanıcı adı kutusu hiç bulunamadı!")
        browser.quit()
        exit()

# İleri butonuna tıkla
time.sleep(2)
print("➡️ İleri butonuna tıklanıyor...")

try:
    iler_butonu = browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/button[2]/div')
    iler_butonu.click()
    print("✅ İleri butonuna başarıyla tıklandı!")
except NoSuchElementException:
    print("❌ İleri butonu bulunamadı! Alternatif yöntemler deneniyor...")
    
    alternatif_iler_xpaths = [
        '//button//span[text()="Next"]/..',
        '//button//span[text()="İleri"]/..',
        '//button[contains(text(), "Next")]',
        '//button[contains(text(), "İleri")]'
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

# Şifre girişi
time.sleep(3)
print("🔑 Şifre giriliyor...")

try:
    sifre_kutusu = browser.find_element(By.XPATH, '//input[@name="password"]')
    sifre_kutusu.send_keys("Erkanaslı0512")  # ← BURAYA KENDİ ŞİFRENİZİ YAZIN
    print("✅ Şifre başarıyla girildi!")
except NoSuchElementException:
    print("❌ Şifre kutusu bulunamadı! Alternatif yöntemler deneniyor...")
    
    alternatif_sifre_xpaths = [
        '//input[@type="password"]',
        '//input[contains(@placeholder, "Password")]',
        '//input[contains(@placeholder, "Şifre")]'
    ]
    
    sifre_bulundu = False
    for xpath in alternatif_sifre_xpaths: # alternatif xpath'ler
        try:
            sifre_kutusu = browser.find_element(By.XPATH, xpath)
            sifre_kutusu.send_keys("Erkanaslı0512")  # ← BURAYA KENDİ ŞİFRENİZİ YAZIN
            print(f"✅ Şifre kutusu alternatif XPATH ile bulundu: {xpath}")
            sifre_bulundu = True
            break
        except NoSuchElementException:
            continue
    
    if not sifre_bulundu:
        print("❌ Şifre kutusu hiç bulunamadı!")
        browser.quit()
        exit()

# Giriş butonuna tıkla
time.sleep(2)
print("🚪 Giriş butonuna tıklanıyor...")

try:
    giris_butonu = browser.find_element(By.XPATH, '//button[contains(@role, "button")]//span[text()="Giriş yap" or text()="Log in"]/..')
    giris_butonu.click()
    print("✅ Giriş butonuna başarıyla tıklandı!")
except NoSuchElementException:
    print("❌ Giriş butonu bulunamadı! Alternatif yöntemler deneniyor...")
    
    alternatif_giris_xpaths = [
        '//button//span[text()="Log in"]/..',
        '//button//span[text()="Giriş yap"]/..',
        '//button[contains(text(), "Log in")]',
        '//button[contains(text(), "Giriş")]'
    ]
    
    giris_bulundu = False
    for xpath in alternatif_giris_xpaths:
        try:
            giris_butonu = browser.find_element(By.XPATH, xpath)
            giris_butonu.click()
            print(f"✅ Giriş butonu alternatif XPATH ile bulundu: {xpath}")
            giris_bulundu = True
            break
        except NoSuchElementException:
            continue
    
    if not giris_bulundu:
        print("❌ Giriş butonu hiç bulunamadı!")
        browser.quit()
        exit()

print("⏳ Giriş işlemi tamamlanıyor...")
time.sleep(10)

# Giriş kontrolü
try:
    ana_sayfa_elementi = browser.find_element(By.XPATH, '//nav[@role="navigation"]')
    print("🎉 Başarıyla giriş yapıldı! Ana sayfadasınız.")
except NoSuchElementException:
    print("⚠️ Giriş durumu belirsiz. Manuel kontrol edin.")

print("\n🔍 HASHTAG ARAMA İŞLEMİ BAŞLIYOR...")

# Aranacak hashtag'leri listele (istediğiniz gibi değiştirebilirsiniz)
hashtag_listesi = [
    "#python",
    "#javascript", 
    "#teknoloji",
    "#yapayZeka",
    "#selenium"
]

print(f"📋 {len(hashtag_listesi)} hashtag aranacak: {hashtag_listesi}")

# Her hashtag için arama yap
for i, hashtag in enumerate(hashtag_listesi, 1):
    print(f"\n--- {i}. ARAMA: {hashtag} ---")
    
    try:
        # Arama kutusunu bul (verdiğiniz XPATH)
        arama_kutusu = browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/div/div[2]/div/input')
        
        # Önceki aramayı temizle
        arama_kutusu.clear()
        print(f"🔍 '{hashtag}' aranıyor...")
        
        # Hashtag'i yaz
        arama_kutusu.send_keys(hashtag) 

        # Enter tuşuna bas (arama yap)
        arama_kutusu.send_keys(Keys.RETURN)
        print(f"✅ '{hashtag}' araması başlatıldı!")
        
        # Arama sonuçları yüklensin diye bekle
        time.sleep(5)
        
        # Arama sonuçlarının yüklenip yüklenmediğini kontrol et
        try:
            sonuc_kontrol = browser.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
            if len(sonuc_kontrol) > 0: # tweet bulunduysa
                print(f"📊 {len(sonuc_kontrol)} tweet bulundu!")
            else:
                print("⚠️ Tweet bulunamadı veya henüz yüklenmedi")
        except:
            print("⚠️ Sonuç kontrolü yapılamadı")
            
    except NoSuchElementException:
        print(f"❌ Arama kutusu bulunamadı! Alternatif yöntemler deneniyor...")
        
        # Alternatif arama kutusu XPATH'leri
        alternatif_xpaths = [
            '//input[@placeholder="Ara"]',
            '//input[@placeholder="Search"]', 
            '//input[@data-testid="SearchBox_Search_Input"]',
            '//input[contains(@placeholder, "search")]',
            '//input[contains(@placeholder, "ara")]'
        ]
        
        bulundu = False
        for alt_xpath in alternatif_xpaths:
            try:
                arama_kutusu = browser.find_element(By.XPATH, alt_xpath)
                arama_kutusu.clear()
                arama_kutusu.send_keys(hashtag)
                arama_kutusu.send_keys(Keys.RETURN)
                print(f"✅ Alternatif yöntemle '{hashtag}' arandı!")
                bulundu = True
                break
            except NoSuchElementException:
                continue
        
        if not bulundu:
            print(f"❌ '{hashtag}' araması yapılamadı!")
            continue
    
    # Sonraki aramaya geçmeden önce bekle
    if i < len(hashtag_listesi):  # Son arama değilse
        print(f"⏳ Sonraki arama için 3 saniye bekleniyor...")
        time.sleep(3)

print("\n🎉 Tüm hashtag aramaları tamamlandı!")
browser.back() # geri dön
print("🔍 Tarayıcıyı kapatmak için 10 saniye bekleniyor...") 
time.sleep(10)

# Tarayıcıyı kapat
browser.quit()
print("👋 Program sonlandı!") 