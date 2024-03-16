# projenizin ana dizininde yer alan utils.py dosyası
import cv2
import numpy as np

def add_circle_to_image(image_path):
    # OpenCV kullanarak resmi yükle
    image = cv2.imread(image_path)

    # Çemberin merkez koordinatları
    center_coordinates = (120, 50)

    # Çemberin yarıçapı
    radius = 20

    # Çember rengi (mavi renk)
    color = (255, 0, 0)

    # Çember kalınlığı
    thickness = 2

    # Çembri çiz
    image_with_circle = cv2.circle(image, center_coordinates, radius, color, thickness)

    # Değiştirilmiş görüntüyü kaydetmek isterseniz:
    # cv2.imwrite("modified_image.jpg", image_with_circle)

    # Numpy dizisini Django view'ine geri döndür
    return image_with_circle
