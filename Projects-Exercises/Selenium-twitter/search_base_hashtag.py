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

time.sleep(8)  # Daha uzun bekle

# Kullanıcı adı girişi
print("👤 Kullanıcı adı giriliyor...")
print("⏳ Sayfa tam yüklenmesi için bekle...")
time.sleep(3)

try:
    # Önce genel input arayalım
    kullanici_adi_kutusu = browser.find_element(By.XPATH, '//input[@name="text"]')
    kullanici_adi_kutusu.send_keys("Erkan_0630")  #kullanıcı adı 
    print("✅ Kullanıcı adı başarıyla girildi!")
except NoSuchElementException:
    print("❌ Kullanıcı adı kutusu bulunamadı! Alternatif yöntemler deneniyor...")
    
    alternatif_xpaths = [
        '//input[@name="text"]',
        '//input[@autocomplete="username"]',
        '//input[contains(@placeholder, "kullanıcı")]',
        '//input[contains(@placeholder, "username")]',
        '//input[contains(@placeholder, "Phone")]',
        '//input[contains(@placeholder, "email")]',
        '//input[@data-testid="ocfEnterTextTextInput"]',
        '//input[@type="text"]',
        '//label//input',
        '//div[@role="textbox"]',
        '//input[contains(@class, "r-30o5oe")]',
        '//input[contains(@class, "r-homxoj")]',
        '//*[@data-testid="LoginForm_Login_Input"]//input',
        '//div[contains(@class, "css-1dbjc4n")]//input[@type="text"]'
    ]
    
    element_bulundu = False
    for i, xpath in enumerate(alternatif_xpaths, 1):
        try:
            print(f"🔍 Alternatif {i}/{len(alternatif_xpaths)} deneniyor: {xpath[:50]}...")
            kullanici_adi_kutusu = browser.find_element(By.XPATH, xpath)
            kullanici_adi_kutusu.send_keys("Erkan_0630")  #kullanıcı adı 
            print(f"✅ Alternatif XPATH ile başarılı: {xpath}")
            element_bulundu = True
            break
        except NoSuchElementException:
            print(f"   ❌ Çalışmadı")
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
                
                # İlk 10 tweet'in içeriğini al ve dosyaya yaz
                print(f"📝 İlk 10 tweet içeriği alınıyor ve tweets.txt dosyasına yazılıyor...")
                
                # Dosyaya hashtag başlığı ekle
                with open("tweets.txt", "a", encoding="utf-8") as file:
                    file.write(f"\n{'='*50}\n")
                    file.write(f"HASHTAG: {hashtag}\n")
                    file.write(f"ARAMA TARİHİ: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                    file.write(f"{'='*50}\n\n")
                
                # Tweet içeriklerini almak için alternatif yöntemler deneyelim
                tweet_sayisi = 0
                max_tweet = 10
                
                # Birinci yöntem: Daha spesifik css-1jxf684 seçicisi
                try:
                    # Önce sadece tweet içindeki css-1jxf684 elementlerini dene
                    tweet_elementleri = browser.find_elements(By.CSS_SELECTOR, 'article .css-1jxf684')
                    
                    if not tweet_elementleri:
                        # Eğer bulamazsa genel css-1jxf684 kullan
                        tweet_elementleri = browser.find_elements(By.CSS_SELECTOR, '.css-1jxf684')
                        print(f"✅ Genel css-1jxf684 class'ı ile {len(tweet_elementleri)} element bulundu")
                    else:
                        print(f"✅ Spesifik article .css-1jxf684 ile {len(tweet_elementleri)} tweet bulundu!")
                    
                    if tweet_elementleri:
                        print(f"📝 İlk {min(max_tweet, len(tweet_elementleri))} element kontrol ediliyor...")
                        
                        for j, tweet in enumerate(tweet_elementleri[:max_tweet], 1):
                            try:
                                tweet_metni = tweet.text.strip()
                                
                                # Debug: Her elementin durumunu kontrol et
                                print(f"🔍 Element {j} kontrol ediliyor...")
                                print(f"   Text uzunluğu: {len(tweet_metni)} karakter")
                                
                                if tweet_metni and len(tweet_metni) > 15:  # En az 15 karakter olsun
                                    # Debug: İlk 50 karakteri göster
                                    print(f"   İçerik önizleme: {tweet_metni[:50]}...")
                                    
                                    with open("tweets.txt", "a", encoding="utf-8") as file:
                                        file.write(f"Tweet {j}:\n")
                                        file.write(f"{tweet_metni}\n")
                                        file.write("-" * 30 + "\n\n")
                                    
                                    print(f"✅ Tweet {j} kaydedildi")
                                    tweet_sayisi += 1
                                else:
                                    if len(tweet_metni) == 0:
                                        print(f"   ⚠️ Element {j} boş")
                                    else:
                                        print(f"   ⚠️ Element {j} çok kısa: '{tweet_metni}'")
                                        
                            except Exception as e:
                                print(f"⚠️ Tweet {j} alınırken hata: {e}")
                                continue
                    else:
                        print("⚠️ css-1jxf684 class'ı ile tweet bulunamadı, alternatif yöntemler deneniyor...")
                        raise Exception("CSS class bulunamadı")
                        
                except Exception:
                    # İkinci yöntem: Genel tweet seçicileri
                    print("🔄 Alternatif tweet seçicileri deneniyor...")
                    
                    alternatif_selectors = [
                        '[data-testid="tweetText"]',  # En güvenilir
                        'article div[data-testid="tweetText"]',  # Tweet içindeki metin
                        'div[data-testid="tweetText"] span',  # Span içindeki metin
                        '[data-testid="tweet"] div[lang]',  # Dil attribute'lu div
                        'article .css-1jxf684',  # Spesifik css class
                        '.css-1jxf684',  # Genel css class
                        'article [role="group"] + div div[lang]'  # En son çare
                    ]
                    
                    for selector in alternatif_selectors:
                        try:
                            tweet_elementleri = browser.find_elements(By.CSS_SELECTOR, selector)
                            if tweet_elementleri:
                                print(f"✅ Alternatif selector ile {len(tweet_elementleri)} tweet bulundu: {selector}")
                                
                                for j, tweet in enumerate(tweet_elementleri[:max_tweet], tweet_sayisi + 1):
                                    try:
                                        tweet_metni = tweet.text.strip()
                                        if tweet_metni and len(tweet_metni) > 10:  # Çok kısa olanları atla
                                            with open("tweets.txt", "a", encoding="utf-8") as file:
                                                file.write(f"Tweet {j}:\n")
                                                file.write(f"{tweet_metni}\n")
                                                file.write("-" * 30 + "\n\n")
                                            
                                            print(f"✅ Tweet {j} kaydedildi")
                                            tweet_sayisi += 1
                                            
                                            if tweet_sayisi >= max_tweet:
                                                break
                                    except Exception as e:
                                        continue
                                break  # Başarılı selector bulundu, döngüyü kır
                        except Exception:
                            continue
                
                if tweet_sayisi > 0:
                    print(f"🎉 Toplam {tweet_sayisi} tweet tweets.txt dosyasına kaydedildi!")
                else:
                    print("❌ Hiç tweet içeriği alınamadı!")
                    
            else:
                print("⚠️ Tweet bulunamadı veya henüz yüklenmedi")
        except Exception as e:
            print(f"⚠️ Sonuç kontrolü yapılamadı: {e}")
            
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