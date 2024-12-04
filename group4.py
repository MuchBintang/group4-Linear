print("Hello, World!")
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
image = cv2.imread('Logo Python.jpg')  # Ganti 'input_image.png' dengan nama file gambar kamu
if image is None:
    print("Error: Gambar tidak ditemukan!")
else:
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for proper display

    # 1. Rotation
    rows, cols = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)  # Rotate 45 degrees
    rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))

    # 2. Scaling
    scaled_image = cv2.resize(image, None, fx=0.5, fy=0.5)  # Scale 50%

    # 3. Translation
    M_translation = np.float32([[1, 0, 100], [0, 1, 50]])  # Shift 100px right, 50px down
    translated_image = cv2.warpAffine(image, M_translation, (cols, rows))

    # 4. Skewing (Shearing)
    M_skewing = np.float32([[1, 0.5, 0], [0.5, 1, 0]])  # Shear on X and Y axes
    skewed_image = cv2.warpAffine(image, M_skewing, (cols, rows))

    # Display results
    plt.figure(figsize=(10, 8))

    # Original Image
    plt.subplot(2, 2, 1)
    plt.title("Original Image")
    plt.imshow(image)

    # Rotated Image
    plt.subplot(2, 2, 2)
    plt.title("Rotated Image")
    plt.imshow(rotated_image)

    # Scaled Image
    plt.subplot(2, 2, 3)
    plt.title("Scaled Image")
    plt.imshow(scaled_image)

    # Translated Image
    plt.subplot(2, 2, 4)
    plt.title("Translated Image")
    plt.imshow(translated_image)

    plt.tight_layout()
    plt.show()
