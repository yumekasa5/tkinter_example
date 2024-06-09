import cv2
import numpy as np

base_dir_path = r"D:\Work\git_repo\tkinter_example"
image_num = 20
width = 512

# Create a test image
for i in range(image_num):
    # Generate a random image with average brightness
    img = np.random.randint(0, 256, (width, width, 3), dtype=np.uint8)

    # Calculate the average brightness of the image
    avg_brightness = np.mean(img)

    # Adjust the brightness to the desired average brightness
    img = img * (width * width * 3) / (avg_brightness * 256)

    # Ensure that the image values are within the valid range
    img = np.clip(img, 0, 255)

    # Convert the image to the appropriate data type
    img = img.astype(np.uint8)
    cv2.imwrite(base_dir_path + r"\tests\test_images\test_image_" + str(i) + ".jpg", img)
    print("test_image_" + str(i) + ".jpg is created.")