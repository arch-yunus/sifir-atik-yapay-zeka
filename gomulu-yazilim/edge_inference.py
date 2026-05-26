# Gömülü Sistem Edge Inference (Faz-2 Entegrasyonu)
import time
import requests
from datetime import datetime
import random # Test aşamasında model simülasyonu için

# Backend API Adresi (FastAPI sunucusunun çalıştığı adres)
BACKEND_URL = "http://localhost:8000/api/detect"

def init_gpio():
    print("GPIO Pinleri başlatılıyor (Pnömatik valfler için)...")
    # Örnek: RPi.GPIO kurulumu

def run_inference(frame):
    """
    Kameradan alınan frame burada TFLite modelinden geçirilir.
    Şu an simülasyon amacıyla rastgele tespit dönmektedir.
    """
    print("Görüntü modelden geçiriliyor...")
    # TFLite inference simülasyonu
    classes = ["PET", "HDPE", "Metal", "Reject"]
    detected_class = random.choice(classes)
    confidence = random.uniform(80.0, 99.9)
    return detected_class, confidence

def actuate(waste_type):
    if waste_type == "PET":
        print("Valf 1 tetikleniyor - PET ayrıştırıldı.")
    elif waste_type == "HDPE":
        print("Valf 2 tetikleniyor - HDPE ayrıştırıldı.")
    elif waste_type == "Metal":
        print("Valf 3 tetikleniyor - Metal ayrıştırıldı.")
    else:
        print("Diğer atık, bantta devam ediyor (Reject).")

def send_to_backend(waste_type, confidence):
    """Tespit verisini Web Dashboard'un backendine gönderir."""
    payload = {
        "type": waste_type,
        "confidence": confidence,
        "timestamp": datetime.now().strftime("%H:%M:%S")
    }
    try:
        response = requests.post(BACKEND_URL, json=payload, timeout=2)
        if response.status_code == 200:
            print(f"[API] Veri başarıyla gönderildi: {waste_type}")
        else:
            print(f"[API] Veri gönderilemedi. Hata Kodu: {response.status_code}")
    except Exception as e:
        print(f"[API] Sunucuya ulaşılamadı: {e}")

def main():
    print("Edge Inference başlatıldı...")
    init_gpio()
    
    try:
        while True:
            # Gerçekte kameradan frame okuma yapılır (cv2.VideoCapture)
            frame = None 
            
            # 1. Kameradan model çıkarımı yap
            waste_type, confidence = run_inference(frame)
            
            # 2. Fiziksel donanımı (Servo/Valf) tetikle
            actuate(waste_type)
            
            # 3. İstatistikleri arayüze (Backend'e) ilet
            send_to_backend(waste_type, confidence)
            
            # Bant akışını simüle et
            print("-" * 30)
            time.sleep(random.uniform(2, 5))
            
    except KeyboardInterrupt:
        print("Sistem durduruluyor.")
    finally:
        print("GPIO ve Kamera Temizlendi.")

if __name__ == "__main__":
    main()
