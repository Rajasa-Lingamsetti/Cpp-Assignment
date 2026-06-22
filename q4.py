# q4.py
# CS253 Assignment
# Question 4
# Name: Rajasa Lingamsetti
# Roll Number: 240596

import numpy as np

# Function to apply 3x3 convolution filter manually
def apply_filter(image, kernel):

    rows, cols = image.shape

    # Add zero padding of size 1 around image
    padded_image = np.pad(
        image,
        pad_width=1,
        mode="constant",
        constant_values=0
    )

    # Output image with same dimensions
    output = np.zeros((rows, cols), dtype=int)

    # Slide kernel over every pixel
    for i in range(rows):
        for j in range(cols):

            # Get current 3x3 window
            window = padded_image[i:i + 3, j:j + 3]

            # Multiply corresponding values and sum them
            value = np.sum(window * kernel)

            # Clip value so it remains between 0 and 255
            value = max(0, min(255, value))

            output[i][j] = int(value)

    return output


# Sample test
dummy_img = np.array([
    [10, 10, 10],
    [10, 50, 10],
    [10, 10, 10]
])

edge_kernel = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
])

print(apply_filter(dummy_img, edge_kernel))