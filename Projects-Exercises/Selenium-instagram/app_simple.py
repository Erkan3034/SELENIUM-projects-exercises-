from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import loginInfo

print("📸 Instagram Takipçi Listeleme Botu (Basit Versiyon) Başlatılıyor...")

# Firefox yerine Chrome kullanacağız (daha stabil)
browser = webdriver.Chrome()
browser.maximize_window()

try:
    # Instagram ana sayfasına git
    print("🌐 Instagram'a gidiliyor...")
    browser.get("https://www.instagram.com/")
    time.sleep(3)

    # Giriş yap linkine tıkla (eğer ana sayfadaysak)
    try:
        print("🔗 'Giriş Yap' linkine tıklanıyor...")
        giris_yap_link = browser.find_element(By.XPATH, "//a[contains(text(), 'Log in') or contains(text(), 'Giriş')]")
        giris_yap_link.click()
        time.sleep(2)
    except:
        print("ℹ️ Zaten giriş sayfasında veya direkt giriş formu var")

    # Kullanıcı adı ve şifre gir
    print("👤 Giriş bilgileri giriliyor...")
    username_input = browser.find_element(By.NAME, "username")
    password_input = browser.find_element(By.NAME, "password")
    
    username_input.clear()
    username_input.send_keys(loginInfo.username)
    
    password_input.clear()
    password_input.send_keys(loginInfo.password)
    
    # Giriş butonuna tıkla
    print("🚪 Giriş yapılıyor...")
    login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    time.sleep(8)
    
    # Bildirim dialoglarını kapat
    print("📱 Bildirimler kapatılıyor...")
    try:
        # "Şimdi Değil" butonlarını bul ve tıkla
        not_now_buttons = browser.find_elements(By.XPATH, "//button[contains(text(), 'Not Now') or contains(text(), 'Şimdi Değil')]")
        for button in not_now_buttons:
            if button.is_displayed():
                button.click()
                time.sleep(2)
    except:
        pass

    # Profil sayfasına git
    print("👤 Profil sayfasına gidiliyor...")
    profile_url = f"https://www.instagram.com/{loginInfo.username}/"
    browser.get(profile_url)
    time.sleep(5)

    # Takipçiler butonunu bul ve tıkla
    print("👥 Takipçiler butonuna tıklanıyor...")
    
    # Takipçi sayısını içeren linki bul
    try:
        followers_link = browser.find_element(By.XPATH, f"//a[contains(@href, '/{loginInfo.username}/followers/')]")
        followers_link.click()
    except:
        # Alternatif yöntem: direkt URL'ye git
        print("🔄 Direkt takipçi sayfasına gidiliyor...")
        followers_url = f"https://www.instagram.com/{loginInfo.username}/followers/"
        browser.get(followers_url)
    
    time.sleep(5)

    print("📜 Takipçi listesi yükleniyor ve scroll yapılıyor...")
    
    # JavaScript ile scroll yaparak tüm takipçileri yükle
    js_scroll_command = """
    // Modal pencereyi bul
    var followersModal = document.querySelector('div[role="dialog"] div[style*="overflow"]');
    if (!followersModal) {
        // Alternatif: sayfanın kendisi
        followersModal = document.body;
    }
    
    // En alta scroll yap
    if (followersModal.scrollTo) {
        followersModal.scrollTo(0, followersModal.scrollHeight);
    } else {
        window.scrollTo(0, document.body.scrollHeight);
    }
    
    // Scroll yüksekliğini döndür
    return followersModal.scrollHeight || document.body.scrollHeight;
    """
    
    # Infinite scroll - tüm takipçiler yüklenene kadar
    len_of_page = browser.execute_script(js_scroll_command)
    match = False
    scroll_count = 0
    max_scrolls = 50  # Maksimum scroll sayısı
    
    while not match and scroll_count < max_scrolls:
        scroll_count += 1
        print(f"   📜 Scroll {scroll_count}/{max_scrolls} - Sayfa yüksekliği: {len_of_page}")
        
        last_count = len_of_page
        time.sleep(2)  # Bekleme süresi
        len_of_page = browser.execute_script(js_scroll_command)
        
        if last_count == len_of_page:
            print(f"   ✅ Scroll tamamlandı! (Sayfa yüksekliği değişmedi)")
            match = True
        
        # Ekstra güvenlik: çok fazla scroll'da dur
        if scroll_count >= max_scrolls:
            print(f"   ⚠️ Maksimum scroll sayısına ulaşıldı")
            break
    
    time.sleep(3)  # Final yükleme için bekle
    
    print("👥 Takipçi isimleri toplanıyor...")
    
    # Takipçi isimlerini çek - birden fazla CSS selector dene
    followers_list = []
    
    # CSS selectors to try (Instagram güncel class'ları)
    selectors_to_try = [
        "._ap3a._aaco._aacw._aacx._aad7._aade",  # Sizin verdiğiniz class'lar
        "._aacl._aaco._aacw._aacx._aad7._aade",  # Alternatif
        ".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.notranslate._a6hd",  # Daha detaylı
        "a[href*='/']",  # Genel link selektor
        "div[role='dialog'] a",  # Modal içindeki linkler
    ]
    
    for i, selector in enumerate(selectors_to_try, 1):
        try:
            print(f"   🔍 Selector {i}/{len(selectors_to_try)} deneniyor...")
            
            if selector.startswith(".") or selector.startswith("_"):
                followers = browser.find_elements(By.CSS_SELECTOR, selector)
            else:
                followers = browser.find_elements(By.CSS_SELECTOR, selector)
            
            if followers:
                print(f"   ✅ {len(followers)} element bulundu!")
                
                for follower in followers:
                    try:
                        follower_text = follower.text.strip()
                        if follower_text and len(follower_text) > 0:
                            # Takipçi adını temizle (sadece username'i al)
                            username_only = follower_text.split('\n')[0] if '\n' in follower_text else follower_text
                            if username_only not in followers_list and len(username_only) > 0:
                                followers_list.append(username_only)
                    except:
                        continue
                
                if followers_list:
                    print(f"   🎉 {len(followers_list)} takipçi ismi toplandı!")
                    break
                        
        except Exception as e:
            print(f"   ❌ Selector {i} başarısız: {e}")
            continue
    
    # Dosyaya yaz
    if followers_list:
        print(f"💾 {len(followers_list)} takipçi 'followers.txt' dosyasına yazılıyor...")
        
        with open("followers.txt", "w", encoding="UTF-8") as file:
            file.write(f"INSTAGRAM TAKİPÇİ LİSTESİ - {loginInfo.username}\n")
            file.write(f"Tarih: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("=" * 50 + "\n\n")
            
            for i, follower in enumerate(followers_list, 1):
                file.write(f"{i}. {follower}\n")
            
            file.write(f"\n{'-'*50}\n")
            file.write(f"Toplam Takipçi Sayısı: {len(followers_list)}\n")
            file.write(f"Scroll Sayısı: {scroll_count}\n")
        
        print(f"✅ İşlem tamamlandı! {len(followers_list)} takipçi kaydedildi.")
    else:
        print("❌ Hiç takipçi bulunamadı!")

except Exception as e:
    print(f"❌ Bir hata oluştu: {e}")

finally:
    print("⏳ Tarayıcı 10 saniye sonra kapanacak...")
    time.sleep(10)
    browser.quit()
    print("👋 Program sonlandı!") 