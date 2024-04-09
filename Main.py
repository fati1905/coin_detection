import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model

from contours import get_all_segments


def classify(model, coinimage, i):
    img_size = 100

    # Check if the input image is not None and not empty
    if coinimage is None or coinimage.size == 0:
        return None  # Return None if the image is empty

    my_image_resized = cv2.resize(coinimage, (img_size, img_size))
    probabilities = model.predict(np.array([my_image_resized]))
    labels = ['2e', '1e', '50c', '20c', '10c', '5c', '2c', '1c']
    index = np.argsort(probabilities[0, :])
    return labels[index[7]]


def main():
    image = cv2.imread("melange/m (17).jpg")
    segments = get_all_segments(image)
    if os.path.isdir('coins_model'):
        model = load_model('coins_model.h5')
        print("Model loaded")
    else:
        print("Model not found")
        return
    d = {}
    coin_number = 0
    cents = 0
    euros = 0
    for cropped_image in segments:
        m = classify(model, cropped_image, coin_number)
        if m.endswith('c'):
            cents = cents + int(m[:-1])
        else:
            euros = euros + int(m[:-1])
        print(m)
        if m in d:
            d[m] += 1
        else:
            d[m] = 1
        plt.clf()  # Clear current plot
        plt.imshow(cropped_image)
        plt.savefig(f'coins_contours/contour_{coin_number}_{m}.png')
        coin_number += 1
        print("Somme of money: ", euros + (cents / 100), 'Euro, ', 'avec ', cents % 100, ' Cents')


if __name__ == '__main__':
    main()
