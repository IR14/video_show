import cv2
cap = cv2.VideoCapture('C:/Users/Ilya/Desktop/love_shiba.mp4') # Just use any directory containing the video you want
ret = cap.set(3,1000) # (3,x) - width ~ (4,y) - height, so 640x480 by default
while(True):
    ret, frame = cap.read() # Capture frame-by-frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Our operations on the frame come here
    cv2.imshow('frame',gray) # Display the resulting frame
    if cv2.waitKey(25) & 0xFF == ord('q'): # Press <<q>> to close output window
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
