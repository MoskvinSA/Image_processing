import numpy as np
import cv2 as cv
import os
from matplotlib import pyplot as plt

def CalcOfDamageAndNonDamage (image_name):
    image = image_name

    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (7,7))
    image_erode = cv.erode(image, kernel)

    hsv_img = cv.cvtColor(image_erode, cv.COLOR_BGR2HSV)

    markers = np.zeros((image.shape[0], image.shape[1]), dtype = 'int32')
    markers[90:140, 90:140] = 255
    markers[236:255, 0:20] = 1
    markers[0:20, 0:20] = 1
    markers[0:20, 236:255] = 1
    markers[236:255, 236:255] = 1

    leafs_area_BGR = cv.watershed(image_erode, markers)

    healthy_part = cv.inRange(hsv_img, (36,25,25), (86, 255, 255))
    ill_part = leafs_area_BGR - healthy_part

    mask = np.zeros_like(image, np.uint8)
    mask[leafs_area_BGR > 1] = (255, 0, 255)
    mask[ill_part > 1] = (0, 0, 255)
    return mask

def main():
    path = os.getcwd() + '/Lab2/_test/'

    img_list = []
    for image in os.listdir(path):
        img_list.append(cv.imread(path + image))

    num_result = 0
    for img in img_list:
        # IMAGE
        b, g, r = cv.split(img)
        rgb_img = cv.merge([r,g,b])

        # Non-Local Means Filter
        dst = cv.fastNlMeansDenoisingColored(img, None, 80,7,21)
        b,g,r = cv.split(dst)
        rgb_dst = cv.merge([r,g,b])

        # Bilateral Filter
        bil = cv.bilateralFilter(img, 25,50,50)
        b, g, r = cv.split(bil)
        bilateral = cv.merge([r,g,b])

        # Damage
        img_test_dst = CalcOfDamageAndNonDamage(rgb_dst)
        img_test_img = CalcOfDamageAndNonDamage(rgb_img)
        img_test_bil = CalcOfDamageAndNonDamage(bilateral)

        # Image output display
        fig = plt.gcf()
        plt.subplot(231), plt.imshow(rgb_img)
        plt.subplot(232), plt.imshow(rgb_dst)
        plt.subplot(233), plt.imshow(bilateral)
        plt.subplot(234), plt.imshow(img_test_img)
        plt.subplot(235), plt.imshow(img_test_dst)
        plt.subplot(236), plt.imshow(img_test_bil)
        #plt.show()

        # Image output folder
        fig.savefig(path[0:-6] + 'output/' + str(num_result) + '.jpg')
        num_result = num_result + 1


if __name__ == '__main__':
    main()