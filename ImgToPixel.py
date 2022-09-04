import cv2

# Input image
img = cv2.imread('image.jpg')

# Get input size
height, width = img.shape[:2]

# Desired "pixelated" size
w, h = (64, 64)

# Resize input to "pixelated" size
temp = cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)

# Initialize output image
output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

cv2.imshow('Input', img)
cv2.imshow('Output', output)

cv2.imwrite("pixel_image.png", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
