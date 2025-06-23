# reCAPTCHA Çözümleri ve Stratejileri

## Problem
Selenium ile Google'a erişmeye çalıştığınızda reCAPTCHA ile karşılaşabilirsiniz. Bu, otomatik botları engellemek için Google'ın kullandığı bir güvenlik sistemi.

## Çözüm Stratejileri

### 1. Anti-Detection Teknikleri (`ap_improved.py`)
- Chrome driver'ı gizleme
- User agent değiştirme
- WebDriver özelliğini kaldırma
- İnsan benzeri yazma (random delays)

### 2. Alternatif Arama Motorları (`ap_simple.py`)
- **DuckDuckGo**: Genellikle reCAPTCHA kullanmaz
- **Bing**: Google'a göre daha az reCAPTCHA
- **Yahoo**: Alternatif seçenek

### 3. Manuel reCAPTCHA Çözme
- Script reCAPTCHA tespit ettiğinde 30 saniye bekler
- Bu sürede manuel olarak reCAPTCHA'yı çözebilirsiniz

## Kullanım

### Basit Versiyon (Önerilen)
```bash
python ap_simple.py
```

### Gelişmiş Versiyon
```bash
python ap_improved.py
```

## Ek Öneriler

### 1. Proxy Kullanımı
```python
chrome_options.add_argument('--proxy-server=http://proxy-ip:port')
```

### 2. Session Yönetimi
- Tarayıcı profilini kaydetme
- Cookie'leri saklama

### 3. Rate Limiting
- İstekler arasında bekleme
- Çok sık istek göndermeme

### 4. Undetected ChromeDriver
```bash
pip install undetected-chromedriver
```

```python
import undetected_chromedriver as uc
driver = uc.Chrome()
```

## En İyi Uygulamalar

1. **DuckDuckGo kullanın** - reCAPTCHA olmadan çalışır
2. **İnsan benzeri davranın** - random delays ekleyin
3. **User agent değiştirin** - gerçekçi tarayıcı bilgisi
4. **Çok sık istek göndermeyin** - rate limiting uygulayın
5. **Proxy kullanın** - IP rotasyonu yapın

## Hata Ayıklama

Eğer hala reCAPTCHA ile karşılaşıyorsanız:
1. Farklı arama motoru deneyin
2. Proxy kullanın
3. User agent'ı değiştirin
4. Daha uzun bekleme süreleri ekleyin 