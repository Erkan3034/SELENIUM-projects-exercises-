# EksiSözlük Selenium Scraper

Bu proje Selenium WebDriver kullanarak EksiSözlük'ten İstanbul konusuyla ilgili gönderileri otomatik olarak toplayan bir Python uygulamasıdır.

## 🔧 Gereksinimler

- Python 3.x
- Selenium
- Chrome tarayıcısı
- ChromeDriver

## 🚀 Kurulum

1. Gerekli paketleri yükleyin:
```bash
pip install selenium
```

2. ChromeDriver'ı indirin ve PATH'e ekleyin:
   - [ChromeDriver İndirme Sayfası](https://chromedriver.chromium.org/)
   - Chrome sürümünüzle uyumlu olanı seçin

## 📖 Kullanım

Scripti çalıştırmak için:

```bash
python app.py
```

## 🎯 Özellikler

- **Rastgele Sayfa Seçimi**: 1-1341 arasından rastgele sayfa numaraları seçer
- **Otomatik Bekleme**: Her sayfa değişiminde 3 saniye bekler
- **Veri Kaydetme**: Toplanan gönderileri `entries.txt` dosyasına kaydeder
- **Gerçek Zamanlı Çıktı**: İşlem sırasında gönderileri konsola yazdırır

## 📊 Çalışma Mantığı

1. Chrome tarayıcısı açılır
2. EksiSözlük'teki İstanbul konusu sayfalarına gidilir
3. 10 farklı rastgele sayfadan veri toplanır
4. Her sayfadaki `.content` CSS sınıfına sahip elementler seçilir
5. Gönderiler hem konsola yazdırılır hem de `entries.txt` dosyasına eklenir

## 📁 Çıktı

Uygulama çalıştıktan sonra:
- `entries.txt` dosyasında toplanan tüm gönderiler bulunur
- Her göndeри yeni satırda yer alır
- Dosya UTF-8 kodlamasında kaydedilir

## ⚠️ Dikkat Edilmesi Gerekenler

- İnternet bağlantınızın stabil olduğundan emin olun
- EksiSözlük'ün robots.txt dosyasına saygı gösterin
- Çok sık istek yapmayın (mevcut kodda 3 saniye bekleme var)
- ChromeDriver'ın güncel olduğundan emin olun

## 🛠️ Konfigürasyon

Kod içerisinde değiştirilebilir parametreler:

- `pageCount`: Kaç sayfa verisi toplanacağı (varsayılan: 10)
- `randomPage`: Rastgele sayfa aralığı (1-1341)
- `time.sleep(3)`: Sayfalar arası bekleme süresi