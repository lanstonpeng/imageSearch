import cv2
im2 = cv2.imread("asset/i1.jpg")
im = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
surfDetector = cv2.FeatureDetector_create("SURF")
surfDescriptorExtractor = cv2.DescriptorExtractor_create("SURF")
keypoints = surfDetector.detect(im)
(keypoints, descriptors) = surfDescriptorExtractor.compute(im,keypoints)
print (descriptors[0],len(descriptors[0]))

for kp in keypoints:
    x = int( kp.pt[0])
    y = int( kp.pt[1])
    #print (x,y)
    #cv2.circle(im2,(x,y),2,(0,0,255))

#cv2.imwrite('youku.png',im2)
'''
while True:
    cv2.imshow("description features",im2)
    if cv2.waitKey(10) == 27:
        break;
'''
