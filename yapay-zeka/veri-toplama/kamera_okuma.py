import cv2
import os
import time

def main():
    print("Sıfır Atık Yapay Zeka - Otonom Veri Toplama Aracı")
    
    # Hedef klasörü oluştur
    output_dir = "dataset"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    cap = cv2.VideoCapture(0) # Birincil kamerayı aç
    if not cap.isOpened():
        print("Hata: Kamera açılamadı.")
        return

    print("Kamera açıldı. Görüntü kaydetmek için 's' tuşuna, çıkmak için 'q' tuşuna basın.")
    
    count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Görüntü alınamadı.")
            break
            
        cv2.imshow("Veri Toplama (Cikis: q, Kaydet: s)", frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):
            filename = os.path.join(output_dir, f"atik_{int(time.time())}_{count}.jpg")
            cv2.imwrite(filename, frame)
            print(f"Kaydedildi: {filename}")
            count += 1
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
