from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd

URL = "https://www.hepsiburada.com/ara?q=laptop"

print(f"'{URL}' adresine Selenium ile gidiliyor...")

try: 
    # ChromeDriver'ı otomatik olarak indirip yönetmek için webdriver_manager'ı kullanıyoruz.
    driver_service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') # Tarayıcıyı arayüz olmadan arkaplanda çalıştırabilmek için gerekli
    options.add_argument('--disable-gpu') # headless argümanı ile beraber gerekli
    options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36')
    driver = webdriver.Chrome(service = driver_service, options=options)
    driver.get(URL)

    # Sayfanın tamamen yüklenmesi için biraz bekleme süresi eklenmeli. Özellikle JS ile yüklenen içerikler için önemlidir
    time.sleep(10) # 10 saniye koydum. ayarlanabilir.

    html_icerigi = driver.page_source
    print("Sayfa içeriği alındı.")

    driver.quit() # Tarayıcıyı kapat.

    soup = BeautifulSoup(html_icerigi, "html.parser")
    urunler_listesi = []

    # --- BURAYA VERİ AYIKLAMA KODU GELECEK ---
    import re # Fiyatları temizlemek için regular expression

    # Hepsiburada'da ürün kartları için olası seçiciler:
    # 1. data-test-id="product-card" olan elementler
    # 2. 'li' etiketleri ve class'ı 'productListContent-' ile başlayanlar
    # Bu seçicileri kendi güncel Hepsiburada HTML yapına göre doğrulaman/güncellemen gerekebilir.
    
    urun_kartlari = soup.find_all(attrs={"data-test-id": "product-card"})
    if not urun_kartlari:
        print("  'data-test-id=\"product-card\"' ile ürün kartı bulunamadı.")
        print("  'li' etiketleri ve 'productListContent-' class'ı deneniyor...")
        urun_kartlari = soup.find_all('li', class_=lambda value: value and value.startswith('productListContent-'))

    print(f"Toplam {len(urun_kartlari)} potansiyel ürün kartı bulundu.")

    for kart_index, kart in enumerate(urun_kartlari):
        ad = "N/A"
        fiyat_float = 0.0
        urun_linki = "N/A"

        # Ürün Adı
        ad_elementi = kart.find(attrs={'data-test-id': 'product-card-name'})
        if not ad_elementi:
            ad_elementi = kart.find('h2', class_=lambda x: x and x.startswith('title-module_titleRoot_'))
        if not ad_elementi:
            ad_elementi = kart.find('h3', class_=lambda x: x and x.startswith('title-module_titleRoot_'))

        if ad_elementi:
            ad = ad_elementi.text.strip()
        else:
            print(f"    {kart_index+1}. ürün için ad bulunamadı.")

        # Ürün Fiyatı
        fiyat_elementi = kart.find('div', attrs={'data-test-id': lambda x: x and x.startswith('price-current-price')})
        if not fiyat_elementi:
            fiyat_elementi = kart.find('div', attrs={'data-test-id': lambda x: x and x.startswith('final-price')})

        if fiyat_elementi:
            fiyat_str = fiyat_elementi.text.strip()
            fiyat_rakamlar = re.findall(r'[\d,\.]+', fiyat_str)
            if fiyat_rakamlar:
                fiyat_temiz_str = fiyat_rakamlar[0].replace('.', '').replace(',', '.')
                try:
                    fiyat_float = float(fiyat_temiz_str)
                except ValueError:
                    print(f"    Fiyat dönüştürülemedi: {fiyat_str} -> {fiyat_temiz_str}")
            else:
                print(f"    Fiyattan rakam çıkarılamadı: {fiyat_str}")
        else:
            print(f"    {kart_index+1}. ürün için fiyat bulunamadı.")

        # Ürün Linki
        link_elementi = kart.find('a', href=True)
        if link_elementi:
            link_value = link_elementi.get('href') # .get('href') None dönebilir, ['href'] hata verir
            if link_value:
                urun_linki = link_value
                if not urun_linki.startswith('http'):
                    urun_linki = "https://www.hepsiburada.com" + urun_linki
            else:
                 print(f"    {kart_index+1}. ürün için href değeri bulunamadı.")
        else:
            print(f"    {kart_index+1}. ürün için link elementi (<a>) bulunamadı.")

        if ad != "N/A" and fiyat_float > 0:
            urunler_listesi.append({'ad': ad, 'fiyat': fiyat_float, 'link': urun_linki})
            # print(f"  Eklendi: Ad: {ad}, Fiyat: {fiyat_float:.2f} TL, Link: {urun_linki}") # İstersen bu print'i açabilirsin
        else:
            print(f"    {kart_index+1}. ürün (Ad: {ad}, Fiyat: {fiyat_float}) yetersiz bilgi nedeniyle atlandı.")

    # Döngü bittikten sonra, yani hala try bloğunun içindeyiz:
    if urunler_listesi:
        df = pd.DataFrame(urunler_listesi)
        print("\n--- Toplanan Veriler (İlk 5) ---")
        print(df.head())
        try:
            df.to_csv("hepsiburada_laptoplar_selenium.csv", index=False, encoding='utf-8-sig')
            print("\nVeriler 'hepsiburada_laptoplar_selenium.csv' dosyasına başarıyla kaydedildi.")
        except Exception as e_csv:
            print(f"CSV dosyasına yazılırken hata oluştu: {e_csv}")
    else:
        print("\nHiçbir ürün verisi çekilemedi veya listeye eklenemedi.")

    # Try bloğunun sonu

except Exception as e:
    print(f"Selenium ile işlem sırasında bir hata oluştu: {e}")
    if 'driver' in locals() and driver is not None:
        driver.quit()