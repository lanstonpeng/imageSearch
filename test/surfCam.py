import cv2

#Create object to read images from camera 0
cam = cv2.VideoCapture(0)

#Initialize SURF object
surf = cv2.SURF(85)

#Set desired radius
rad = 2

while True:
    #Get image from webcam and convert to greyscale
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Detect keypoints and descriptors in greyscale image
    keypoints, descriptors = surf.detect(gray)

    #Draw a small red circle with the desired radius
    #at the (x, y) location for each feature found
    for kp in keypoints:
        x = int(kp.pt[0])
        y = int(kp.pt[1])
        cv2.circle(img, (x, y), rad, (0, 0, 255))

    #Display colour image with detected features
    cv2.imshow("features", img)

    #Sleep infinite loop for ~10ms
    #Exit if user presses <Esc>
    if cv2.waitKey(10) == 27:
        break
