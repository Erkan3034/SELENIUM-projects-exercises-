from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Enter tuşu için
import time
from selenium.common.exceptions import NoSuchElementException

# Chrome tarayıcısını başlat
print("🚀 Chrome tarayıcısı başlatılıyor...")
browser = webdriver.Chrome()

# Twitter/X ana sayfasına git
url = "https://x.com/"
print(f"📱 {url} adresine gidiliyor...")
browser.get(url)

# Sayfa yüklensin diye bekle
time.sleep(5)

# Aranacak hashtag'leri listele (istediğiniz gibi değiştirebilirsiniz)
hashtag_listesi = [
    "#python",
    "#javascript", 
    "#teknoloji",
    "#yapayZeka",
    "#selenium"
]

print(f"🔍 {len(hashtag_listesi)} hashtag aranacak: {hashtag_listesi}")

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
        
        # İsteğe bağlı: Arama sonuçlarının yüklenip yüklenmediğini kontrol et
        try:
            sonuc_kontrol = browser.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
            if len(sonuc_kontrol) > 0:
                print(f"📊 {len(sonuc_kontrol)} tweet bulundu!")
            else:
                print("⚠️ Tweet bulunamadı veya henüz yüklenmedi")
        except:
            print("⚠️ Sonuç kontrolü yapılamadı")
            
    except NoSuchElementException:
        print(f"❌ Arama kutusu bulunamadı! XPATH güncellemesi gerekebilir.")
        print("🔧 Alternatif yöntemler deneniyor...")
        
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
        print(f"⏳ Sonraki arama için {3} saniye bekleniyor...")
        time.sleep(3)

print("\n🎉 Tüm hashtag aramaları tamamlandı!")
print("🔍 Tarayıcıyı kapatmak için 10 saniye bekleniyor...")
time.sleep(10)

# Tarayıcıyı kapat
browser.quit()
print("👋 Program sonlandı!") 