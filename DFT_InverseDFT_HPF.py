import cv2
import numpy as np
from matplotlib import pyplot as plt


def read_img(img_path):
    global img
    img = cv2.imread(img_path, 0)

def hpf_method(frequency):

    # fft to convert the image to freq domain
    f = np.fft.fft2(img)

    # shift the center
    fshift = np.fft.fftshift(f)

    rows, cols = img.shape
    crow,ccol = int(rows/2), int(cols/2)
    # remove the low frequencies by masking with a rectangular window of size 60x60
    # High Pass Filter (HPF)
    print(frequency)
    fshift[crow-frequency:crow+frequency, ccol-frequency:ccol+frequency] = 0


    # shift back (we shifted the center before)
    f_ishift = np.fft.ifftshift(fshift)

    # inverse fft to get the image back
    img_back = np.fft.ifft2(f_ishift)

    img_back = np.abs(img_back)
    img_with_filter = img_back.copy()

    # plt.subplot(131),plt.imshow(img, cmap = 'gray')
    # plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    # plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
    # plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
    # plt.subplot(133),plt.imshow(img_back)
    # plt.title('Final Result'), plt.xticks([]), plt.yticks([])
    # plt.show()

    return img_with_filter
