# Twitter Automation Tools - Selenium Tabanlı Bot Uygulamaları

Bu proje, Selenium kullanarak Twitter/X platformu üzerinde otomatik işlemler gerçekleştiren Python uygulamalarını içerir. Toplam 2 ana uygulama ve 1 çıktı dosyası bulunmaktadır.

## 📋 İçerik

### 🔧 Uygulamalar
1. **`auto_login.py`** - Twitter otomatik giriş botu
2. **`search_base_hashtag.py`** - Hashtag arama, tweet toplama ve beğeni botu
3. **`tweets.txt`** - Toplanan tweet'lerin kaydedildiği çıktı dosyası

---

## 🎯 Uygulamaların Amacı

### 1. Auto Login (`auto_login.py`)
**Amaç:** Twitter/X hesabına otomatik giriş yapmak

**Özellikler:**
- Chrome WebDriver kullanarak Twitter/X'e otomatik giriş
- Çoklu XPATH desteği (sayfada değişiklik olursa alternatif yollar dener)
- Hata durumlarında alternatif element arama stratejileri
- Giriş başarı kontrolü

**Kullanım Senaryoları:**
- Manuel giriş yapmak istemediğiniz durumlarda
- Diğer otomasyonlar için temel giriş işlemi olarak
- Test amaçlı hesap giriş kontrolü

### 2. Hashtag Search Bot (`search_base_hashtag.py`)
**Amaç:** Belirli hashtag'ler için tweet'leri otomatik olarak arayıp toplamak ve beğenmek

**Özellikler:**
- Otomatik Twitter giriş işlemi
- Çoklu hashtag araması yapabilme
- Tweet içeriklerini otomatik scraping
- Infinite scroll desteği (daha fazla tweet yüklemek için)
- Tweet'leri otomatik beğenme
- Toplanan tweet'leri dosyaya kaydetme
- Spam koruması (beğeni limitleri)
- Detaillı konsol logları

**Kullanım Senaryoları:**
- Belirli konulardaki tweet'leri toplamak
- Hashtag bazlı sosyal medya araştırması
- Otomatik içerik keşfi
- Engagement artırma (beğeni)

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

### ChromeDriver Kurulumu
1. Chrome sürümünüzü kontrol edin: `chrome://version/`
2. [ChromeDriver İndirme Sayfası](https://chromedriver.chromium.org/downloads)ndan uygun sürümü indirin
3. ChromeDriver'ı PATH'inize ekleyin veya proje klasörüne kopyalayın

---

## 🚀 Kullanım Kılavuzu

### 1. Auto Login Kullanımı

```python
# auto_login.py dosyasını çalıştırın
python auto_login.py
```

**Önemli:** Koda kullanıcı bilgilerinizi eklemeniz gerekiyor:
```python
# Satır 27 ve 61
kullanici_adi_kutusu.send_keys("KULLANICI_ADINIZ")

# Satır 95 ve 129  
sifre_kutusu.send_keys("SIFRENIZ")
```

### 2. Hashtag Search Bot Kullanımı

```python
# search_base_hashtag.py dosyasını çalıştırın
python search_base_hashtag.py
```

**Konfigürasyon:**

1. **Kullanıcı Bilgileri** (Satır 61 ve 130):
```python
kullanici_adi_kutusu.send_keys("KULLANICI_ADINIZ")
sifre_kutusu.send_keys("SIFRENIZ")
```

2. **Aranacak Hashtag'ler** (Satır 187):
```python
hashtag_listesi = [
    "#python",
    "#selenium", 
    "#automation",
    # Buraya istediğiniz hashtag'leri ekleyebilirsiniz
]
```

3. **Beğeni Limiti** (Satır 354):
```python
max_like = min(len(like_buttons), 20)  # Maksimum beğeni sayısı
```

### 3. Çıktı Dosyası (`tweets.txt`)

Bot çalıştığında tüm tweet'ler bu dosyaya şu formatta kaydedilir:
```
==================================================
HASHTAG: #python
ARAMA TARİHİ: 2025-01-15 14:30:25
==================================================

Tweet 1:
Python ile harika projeler geliştirebilirsiniz!...
------------------------------

Tweet 2:
Machine Learning için Python en iyi seçenektir...
------------------------------
```

---

## ⚙️ Gelişmiş Ayarlar

### Scroll ve Tweet Yükleme Ayarları
```python
max_scroll = 8  # Maksimum scroll sayısı (satır 233)
wait_time = random.uniform(2, 4)  # Beğeniler arası bekleme süresi (satır 388)
```

### Alternatif Element Arama
Her kritik işlem için alternatif XPATH'ler tanımlanmıştır:
- Kullanıcı adı kutusu: 14 farklı alternatif
- Şifre kutusu: 4 farklı alternatif  
- Butonlar: 5+ farklı alternatif
- Tweet elementleri: 9 farklı CSS selector

---

## ⚠️ Önemli Uyarılar ve Sınırlamalar

### 🚨 Yasal ve Etik Kullanım
- **Twitter'ın Kullanım Şartları'na uygun kullanın**
- **Rate limiting'e dikkat edin** (çok hızlı işlem yapmayın)
- **Spam davranışından kaçının**
- **Kişisel verileri koruyun**
- **Bu araçları sorumlu bir şekilde kullanın**

### 🔒 Güvenlik
- **Asla ana hesabınızı kullanmayın** - test hesabı oluşturun
- **Şifrelerinizi kodda saklamayın** - environment variables kullanın
- **Two-factor authentication aktifse botu kullanamayabilirsiniz**

### 🐛 Bilinen Sınırlamalar
- Twitter'ın sayfa değişiklikleri bot'u etkileyebilir
- CAPTCHA kontrolü mevcut değil
- Rate limiting protection temel seviyede
- Yalnızca Chrome tarayıcısı desteklenir - Kendi driver tarayıcınızı indiriğp kullanabailirsiniz(firefox gekodriver vs.)

---

## 🔧 Sorun Giderme

### Yaygın Sorunlar ve Çözümleri

1. **"Element bulunamadı" hatası:**
   - Twitter sayfası değişmiş olabilir
   - Alternatif XPATH'ler otomatik denenecek
   - Manuel olarak yeni elementleri inceleyip kodda güncelleyin

2. **ChromeDriver uyumsuzluğu:**
   - Chrome sürümünüzü güncelleyin
   - Uygun ChromeDriver sürümünü indirin

3. **Giriş yapamama:**
   - Kullanıcı adı/şifre kontrol edin
   - 2FA kapalı olduğundan emin olun
   - IP bloğu kontrolü yapın

4. **Tweet'ler alınamıyor:**
   - İnternet bağlantınızı kontrol edin
   - Hashtag'in doğru yazıldığından emin olun
   - CSS selector'lar güncellenmiş olabilir

---

## 📊 Performans İpuçları

### Optimizasyon Önerileri
- **Headless mod:** Daha hızlı çalışma için
```python
options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
```

- **Bekleme sürelerini ayarlayın:** Network hızınıza göre
- **Paralel processing:** Çoklu hashtag için
- **Database entegrasyonu:** Tweet'leri veritabanında saklama

---