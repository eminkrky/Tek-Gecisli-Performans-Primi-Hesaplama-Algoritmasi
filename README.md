Soru:

Bir teknoloji şirketi, çalışanlarına aylık bazda performans primi vermektedir. Primin hesaplanması şu kurallara göre yapılmaktadır:
	•	Çalışanlar her ay belirli sayıda proje tamamlamaktadır.
	•	Tamamlanan her proje, zorluk seviyesine göre puanlanmaktadır (1 ile 10 arasında).
	•	Aylık toplam performans puanı, tamamlanan projelerin zorluk seviyelerinin toplamına eşittir.
	•	Eğer bir çalışan bir ay içinde X veya daha fazla toplam performans puanı toplarsa, o ay için prim alır.
	•	Prim miktarı, çalışanın tamamladığı projeler içindeki en yüksek zorluk seviyesine sahip projenin puanının 3 katı kadardır.

Görev:
Verilen bir çalışanın tamamladığı projelerin zorluk seviyeleri listesi ve şirketin belirlediği X değeri (prim almak için gereken minimum puan), çalışanın o ay prim alıp almayacağını ve alıyorsa ne kadar prim alacağını hesaplayan bir algoritma yazınız.

Örnek Girdi:
Projelerin Zorluk Seviyeleri: [4, 7, 5, 10, 3]
Minimum Gerekli Puan (X): 20

Örnek Çıktı:
Çalışan prim alır.
Prim miktarı: 30

Açıklama:
	•	Toplam performans puanı = 4 + 7 + 5 + 10 + 3 = 29 (20’den fazla olduğu için prim alır).
	•	En yüksek proje puanı 10 olduğundan, prim miktarı 10 * 3 = 30 olur.

Bu algoritmayı Python ile nasıl yazarsınız? 
