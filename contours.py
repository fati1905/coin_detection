import cv2
import numpy as np





def filter_contours(contours, hierarchy, image):
    to_remove = []

    for i in range(len(contours)):
        contour = contours[i]
        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        values = np.max(box)

        if values / image.shape[1] > 0.9 and values / image.shape[0] > 0.9:
            hierarchy[0][i][3] = -2
            to_remove.append(i)
    for i in range(len(hierarchy[0])):
        if hierarchy[0][i][3] in to_remove:
            hierarchy[0][i][3] = -1

    return hierarchy


def get_all_segments(image):
    
    segments = []
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    ret, binary_image = cv2.threshold(gray_image, 75, 255, 0)
    contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    hierarchy = filter_contours(contours, hierarchy, image)[0]
    for i in range(len(contours)):
        contour = contours[i]
        [_, _, first_child, parent] = hierarchy[i]
        if parent != -1 or first_child == -1:
            continue
        if cv2.contourArea(contour) > 150:
            [X, Y, W, H] = cv2.boundingRect(contour)
            cropped_image = rgb_image[Y:Y + H, X:X + W]
            mask = np.zeros_like(cropped_image)  # create empty black image with img size
            mask = cv2.circle(mask, (
                int(cropped_image.shape[0] / 2),
                int(cropped_image.shape[0] / 2)),
                              int(cropped_image.shape[0] / 2), (255, 255, 255), -1)
            result = cv2.bitwise_and(cropped_image, mask)
            segments.append(cropped_image)

    return segments
