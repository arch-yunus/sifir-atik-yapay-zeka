# Malzeme Listesi (BOM) ve Maliyet Analizi

Bu döküman, sıfır atık yapay zeka sisteminin temel bir kurulumu için gerekli asgari bileşenleri listeler. Fiyatlar tahmini olup, bölgeye ve tedarikçiye göre değişiklik gösterebilir.

## 1. İşlemci / Uç Cihaz (Edge Device)
Yapay zeka çıkarımı (inference) ve sensör kontrolü için.

| Bileşen | Önerilen Model | Alternatif | Tahmini Maliyet | Not |
| :--- | :--- | :--- | :--- | :--- |
| **Geliştirme Kartı** | Raspberry Pi 4 (4GB/8GB) | Jetson Nano 2GB | $50 - $100 | Jetson Nano, GPU sayesinde daha hızlı inference sağlar ancak RPi daha bulunabilirdir. |
| **SD Kart** | 32GB Class 10 MicroSD | 64GB | $10 | Hızlı okuma/yazma (A1/A2) tercih edilmeli. |
| **Güç Kaynağı** | 5V 3A Type-C Adaptör | - | $10 | Sistem kararlılığı için kaliteli adaptör şart. |

## 2. Görüntü ve Sensörler
Atığı tanımak için.

| Bileşen | Önerilen Model | Tahmini Maliyet | Not |
| :--- | :--- | :--- | :--- |
| **Kamera** | 1080p USB WebCam veya PiCamera V2 | $15 - $30 | Yüksek FPS (min 30) ve iyi ışık duyarlılığı önemlidir. |
| **Kızılötesi Sensör** | TCRT5000 veya basit IR Engel | $2 | Atığın banttan geçtiğini anlamak (tetikleyici) için. |

## 3. Mekanik ve Aktüatörler
Ayrıştırma eylemini gerçekleştirmek için.

| Bileşen | Önerilen Model | Tahmini Maliyet | Not |
| :--- | :--- | :--- | :--- |
| **Servo Motor** | MG996R (Metal Dişli) | $5 - $10 | Küçük çaplı sistemlerde hava valfi yerine yönlendirici kol olarak kullanılabilir. |
| **Pnömatik Valf** | 12V Solenoid Valf | $15 - $25 | Endüstriyel hız için (ekstra hava kompresörü gerektirir). |
| **Röle Kartı** | 5V 2 Kanal Röle | $3 | Mikrodenetleyicinin valfleri/motorları sürebilmesi için. |

## 4. Toplam Tahmini Maliyet
- **Sadece Görsel & Servo Sistem (Başlangıç):** ~$90 - $120
- **Pnömatik ve Jetson Nano (İleri Seviye):** ~$200 - $250

*(Not: Bu listeye yapısal malzemeler -ör. alüminyum profiller, bant motoru- dahil edilmemiştir.)*
