import matplotlib.pyplot as plt
import cv2
import os


def calculate_brightness(img_path):
    images = os.listdir(img_path)  # List of all images in the given img path

    # Calculating brightness score for every image in the specified path
    for i in images:
        img = cv2.imread(img_path + i)
        # Displaying the image to see the relevance of score with respect to the image
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.show()

        # Converting image to LAB Color model
        # The lightness value, L*, represents the darkest black at L* = 0,
        # and the brightest white at L* = 100. -> source : wikipedia
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

        # Splitting the LAB image to different channels
        l, a, b = cv2.split(lab)

        # Scaling to 0-10 range since l values are from 0-255
        l = l * (10 / 255)

        y, x, z = img.shape  # height, width and number of layers of image
        maxval = []

        count_percent = 9  # variable to pick certain parts of the given image
        count_percent = count_percent / 100
        row_percent = int(count_percent * x)  # Percentage of pixels width wise
        column_percent = int(count_percent * y)  # Percentage of pixels height wise

        for i in range(1, x - 1):
            if i % row_percent == 0:
                for j in range(1, y - 1):
                    if j % column_percent == 0:
                        img_segment = l[i:i + 3, j:j + 3]
                        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(img_segment)
                        maxval.append(maxVal)

        lenmaxVal = 0
        # Not considering 0 pixel values to calculate the average brightness,
        # since the dark/black pixels hamper the entire score
        for i, val in enumerate(maxval):
            if val == 0:
                lenmaxVal += 1
        lenmaxVal = len(maxval) - lenmaxVal
        if lenmaxVal > 0:
            avg_maxval = round(sum(maxval) / lenmaxVal)
        else:
            avg_maxval = 0

        print('>> Average Brightness: {}'.format(avg_maxval))