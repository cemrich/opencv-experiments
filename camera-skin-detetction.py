import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # convert to hsv color format
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # blur the image to remove small artifacts
    blur = cv2.blur(hsv, (20, 20))

    # detect skin colored pixels
    mask_red = cv2.inRange(blur, (150, 0, 0), (180, 255, 255))
    mask_sb = cv2.inRange(blur, (0, 40, 50), (180, 110, 255))
    mask = cv2.bitwise_and(mask_red, mask_sb)

    # blur the image to remove small artifacts
    mask = cv2.blur(mask, (20, 20))

    # apply mask
    result = cv2.bitwise_and(hsv, hsv, None, mask)

    # Display the resulting frame
    cv2.imshow('frame', cv2.cvtColor(result, cv2.COLOR_HSV2BGR))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
