# Instagram Takipçi Listeleme Botu - Selenium Tabanlı Otomasyon

Bu proje, Selenium kullanarak Instagram platformu üzerinde otomatik takipçi listesi çekme işlemi gerçekleştiren Python uygulamasını içerir.

## 📋 İçerik

### 🔧 Uygulama
- **`app.py`** - Instagram takipçi listesi çekme botu
- **`followers.txt`** - Çekilen takipçi listesinin kaydedildiği çıktı dosyası (otomatik oluşturulur)

---

## 🎯 Uygulamanın Amacı

### Instagram Follower Scraper (`app.py`)
**Amaç:** Instagram hesabına giriş yapıp takipçi listesini otomatik olarak çekip kaydetmek

**Ana İşlevler:**
1. **Otomatik Instagram Girişi**
   - Kullanıcı adı ve şifre ile otomatik giriş
   - Çoklu XPATH desteği (sayfada değişiklik olursa alternatif yollar)
   - Çerez ve bildirim kontrolü

2. **Profil Sayfası Navigasyonu**
   - Otomatik profil sayfasına yönlendirme
   - URL tabanlı direkt erişim alternatifi

3. **Takipçi Listesi Çekme**
   - Modal pencere kontrolü
   - Infinite scroll desteği
   - Akıllı bekleme mekanizması
   - Takipçi adlarını otomatik kaydetme

4. **Veri Kaydetme**
   - `followers.txt` dosyasına düzenli format ile kaydetme
   - Tarih/saat damgası
   - Özet istatistikler

**Kullanım Senaryoları:**
- Takipçi listesi analizi
- Sosyal medya araştırması
- İçerik stratejisi geliştirme
- Follower audit işlemleri
- Rekabet analizi

---

## 🛠️ Kurulum ve Gereksinimler

### Gerekli Kütüphaneler
```bash
pip install selenium
```

### Sistem Gereksinimleri
- **Python 3.6+**
- **Google Chrome tarayıcısı**
- **ChromeDriver** (Chrome sürümünüze uygun)
- **Kararlı internet bağlantısı**

### ChromeDriver Kurulumu
1. Chrome sürümünüzü kontrol edin: `chrome://version/`
2. [ChromeDriver İndirme Sayfası](https://chromedriver.chromium.org/downloads)ndan uygun sürümü indirin
3. ChromeDriver'ı PATH'inize ekleyin veya proje klasörüne kopyalayın

---

## 🚀 Kullanım Kılavuzu

### 1. Konfigürasyon

Kodu çalıştırmadan önce aşağıdaki yerlerde kullanıcı bilgilerinizi güncellemeniz gerekiyor:

**Kullanıcı Adı Ayarları:**
```python
# Satır 38 ve 52
kullanici_adi_kutusu.send_keys("KULLANICI_ADINIZ")

# Satır 179 ve 190 (profil sayfası için)
profil_linki = browser.find_element(By.XPATH, '//a[contains(@href, "/KULLANICI_ADINIZ/")]')
profil_url = "https://www.instagram.com/KULLANICI_ADINIZ/"
```

**Şifre Ayarları:**
```python
# Satır 77 ve 89
sifre_kutusu.send_keys("SIFRENIZ")
```

### 2. Uygulamayı Çalıştırma

```bash
python app.py
```

### 3. İşlem Adımları

Bot çalıştığında şu adımları otomatik olarak gerçekleştirir:

1. **🔐 Giriş İşlemi**
   - Instagram ana sayfasına git
   - Çerezleri kabul et (varsa)
   - Kullanıcı adı ve şifre gir
   - Giriş yap

2. **👤 Profil Navigasyonu**
   - Profil sayfasına git
   - Sayfa yüklenmesini bekle

3. **👥 Takipçi Listesi**
   - Takipçiler butonuna tıkla
   - Modal pencereyi aç
   - Takipçi listesini yükle

4. **📜 Veri Çekme**
   - Infinite scroll ile tüm takipçileri yükle
   - Her takipçiyi `followers.txt` dosyasına kaydet
   - İşlem sonunda özet bilgileri ekle

### 4. Çıktı Dosyası Formatı

```
INSTAGRAM TAKİPÇİ LİSTESİ
Tarih: 2025-01-15 16:30:45
==================================================

1. takipci_kullanici_adi_1
2. takipci_kullanici_adi_2
3. takipci_kullanici_adi_3
...

--------------------------------------------------
ÖZET BİLGİLER:
Toplam Takipçi Sayısı: 250
İşlem Tarihi: 2025-01-15 16:45:20
Scroll Adımı Sayısı: 15
```

---

## ⚙️ Gelişmiş Ayarlar

### Scroll ve Yükleme Kontrolü
```python
max_scroll = 50  # Maksimum scroll sayısı (satır 249)
time.sleep(random.uniform(2, 4))  # Scroll arası bekleme süresi (satır 301)
```

### WebDriverWait Ayarları
```python
WebDriverWait(browser, 10)  # Modal pencere bekleme süresi (satır 238)
```

### Alternatif Element Arama Stratejileri

**Kullanıcı Adı Kutusu:** 7 farklı alternatif XPATH
**Şifre Kutusu:** 5 farklı alternatif XPATH
**Giriş Butonu:** 6 farklı alternatif XPATH
**Takipçiler Butonu:** 6 farklı alternatif XPATH
**Takipçi Elementleri:** 3 farklı CSS selector

---

## ⚠️ Önemli Uyarılar ve Sınırlamalar

### 🚨 Yasal ve Etik Kullanım
- **Instagram'ın Kullanım Şartları'na uygun kullanın**
- **Rate limiting'e dikkat edin** (çok hızlı işlem yapmayın)
- **Kişisel verileri koruyun ve saklayın**
- **Bu aracı sorumlu bir şekilde kullanın**
- **Başkalarının gizliliğine saygı gösterin**

### 🔒 Güvenlik ve Gizlilik
- **Asla ana hesabınızı kullanmayın** - test hesabı oluşturun
- **Şifrelerinizi kodda saklamayın** - environment variables kullanın
- **Two-factor authentication aktifse özel ayar gerekebilir**
- **Çekilen veriyi güvenli saklayın**
- **GDPR ve veri koruma kurallarına uyun**

### 🐛 Bilinen Sınırlamalar
- **Instagram'ın sayfa değişiklikleri** bot'u etkileyebilir
- **CAPTCHA kontrolü** mevcut değil
- **Rate limiting protection** temel seviyede
- **Yalnızca Chrome tarayıcısı** desteklenir (Firefox GeckoDriver vs. kullanabilirsiniz)
- **Büyük takipçi listelerinde** uzun sürebilir
- **Özel hesaplar** için çalışmayabilir

---

## 🔧 Sorun Giderme

### Yaygın Sorunlar ve Çözümleri

1. **"Element bulunamadı" hatası:**
   ```
   ❌ Çözüm: Instagram sayfası değişmiş olabilir
   ✅ Alternatif XPATH'ler otomatik denenecek
   🔧 Gerekirse yeni element'leri manuel olarak kodda güncelleyin
   ```

2. **Giriş yapamama:**
   ```
   🔍 Kontrol listesi:
   - Kullanıcı adı/şifre doğru mu?
   - 2FA kapalı mı?
   - Hesap kilitli değil mi?
   - IP adresi bloklu değil mi?
   ```

3. **Takipçiler yüklenmiyor:**
   ```
   📱 Olası nedenler:
   - Hesap özel olabilir
   - İnternet bağlantısı yavaş
   - Instagram rate limit uyguluyor
   - Modal pencere açılmamış
   ```

4. **Incomplete follower list:**
   ```
   ⚙️ Çözümler:
   - max_scroll sayısını artırın
   - Bekleme sürelerini uzatın
   - İnternet bağlantısını kontrol edin
   ```

---

## 📊 Performans İpuçları

### Optimizasyon Önerileri

1. **Headless Mode (Daha Hızlı):**
```python
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
```

2. **Scroll Ayarları:**
```python
# Daha büyük hesaplar için
max_scroll = 100  # Artırın

# Daha hızlı internet için
time.sleep(random.uniform(1, 2))  # Bekleme süresini azaltın
```

3. **Bandwidth Optimizasyonu:**
```python
options.add_argument('--disable-images')  # Görselleri devre dışı bırak
options.add_argument('--disable-javascript')  # JS'yi kısıtla (dikkatli kullanın)
```

---

## 🛡️ Güvenlik Önlemleri

### Recommended Security Practices

1. **Environment Variables Kullanımı:**
```python
import os
username = os.getenv('INSTAGRAM_USERNAME')
password = os.getenv('INSTAGRAM_PASSWORD')
```

2. **Test Hesabı Oluşturun:**
   - Ana hesabınızı asla kullanmayın
   - Bot testi için ayrı hesap açın
   - Minimum takipçi/takip ile test edin

3. **VPN/Proxy Kullanımı:**
   - Farklı IP adreslerinden test edin
   - Rate limiting'i minimize edin

---

## 📈 Gelecek Özellikler (TODO)

- [ ] **Multi-platform desteği** (Firefox, Safari)
- [ ] **GUI arayüz** (Tkinter/PyQt)
- [ ] **Configuration file** desteği (.json/.yaml)
- [ ] **Proxy rotation** sistemi
- [ ] **CAPTCHA handling** entegrasyonu
- [ ] **Database integration** (SQLite/MongoDB)
- [ ] **Export options** (CSV, JSON, Excel)
- [ ] **Follower analytics** (growth tracking)
- [ ] **Scheduled running** (cron job desteği)
- [ ] **Email notifications** (işlem tamamlama)
- [ ] **Resume functionality** (kesinti durumunda devam)
- [ ] **Batch processing** (çoklu hesap)

---

## 🤝 Katkıda Bulunma

Bu projeyi geliştirmek için:

1. **Fork** edin
2. **Feature branch** oluşturun (`git checkout -b feature/YeniOzellik`)
3. **Commit** yapın (`git commit -am 'Takipçi export özelliği eklendi'`)
4. **Push** edin (`git push origin feature/YeniOzellik`)
5. **Pull Request** açın

### Katkı Alanları
- 🐛 Bug fixes
- ✨ Yeni özellikler
- 📚 Dokümantasyon geliştirme  
- 🧪 Test coverage artırma
- 🔧 Performance optimizations

---

## 📜 Lisans ve Sorumluluk

Bu proje **eğitim amaçlı** hazırlanmıştır. 

**⚠️ UYARI:** 
- Instagram'ın Terms of Service'ini ihlal etmemeye dikkat edin
- Bu aracın kötüye kullanımından geliştiriciler sorumlu değildir
- Veri toplama işlemlerinde yasal düzenlemelere uyun
- Başkalarının gizliliğine saygı gösterin

---

## 🆘 Destek ve İletişim

Sorunlarınız için:
- **GitHub Issues** açın
- **Code review** talep edin
- **Documentation** geliştirme önerileri gönderin
- **Feature requests** bildirin

---

**⚡ Bu aracı sorumlu, etik ve yasal kurallara uygun bir şekilde kullanın!**

---

## 📞 Acil Durum Kılavuzu

Bot çalışırken sorun yaşarsanız:

1. **Tarayıcıyı kapatmayın** - işlem devam edebilir
2. **Konsol çıktısını kaydedin** - hata ayıklamak için
3. **followers.txt dosyasını yedekleyin** - kısmi veri kaybını önlemek için
4. **İnternet bağlantısını kontrol edin**
5. **Instagram'dan logout olduğunuzu kontrol edin**

**🚨 Bot durdurmak için:** `Ctrl+C` (Terminal'de) veya tarayıcıyı kapatın. 