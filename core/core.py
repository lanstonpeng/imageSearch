import cv2
import numpy as np

gallarySet = ["images/B.jpg","images/i2.jpg","images/i1.jpg"]

class Engine(object):
    def __init__(self):
        self.kp = None
        self.descritors = None
    def loadImage(self,imgName):
        # Load the images
        img =cv2.imread(imgName)
        return img

    def greytifyImg(self,img):
        # Convert them to grayscale
        imggrey =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        return imggrey

    def extractSURF(self,imggrey):
        # SURF extraction
        self.surf = cv2.FeatureDetector_create("SURF")
        self.surfDescriptorExtractor = cv2.DescriptorExtractor_create("SURF")
        self.kp = self.surf.detect(imggrey)
        self.kp, self.descritors = self.surfDescriptorExtractor.compute(imggrey,self.kp)
    def trainKNN(self):
        samples = np.array(self.descritors)
        responses = np.arange(len(self.kp),dtype = np.float32)
        self.knn = cv2.KNearest()
        self.knn.train(samples,responses)
    def matching(self):
        originalMatch = []
        templateMatch = []
        result = []
        for modelImage in gallarySet:
            templateImg = self.loadImage(modelImage)
            templateGrey = self.greytifyImg(templateImg)
            #match points count
            match = 0
            #unmatch points count
            unmatch = 0

            keys = self.surf.detect(templateGrey)
            keys,desc = self.surfDescriptorExtractor.compute(templateGrey, keys)
            
            for idx , des in enumerate(desc):
                des = np.array(des,np.float32).reshape((1,128))
                retval, results, neigh_resp, dists = self.knn.find_nearest(des,1)
                res,dist =  int(results[0][0]),dists[0][0]

                if dist < 0.1:
                    match +=1
                else:
                    unmatch+=1
                x,y = self.kp[res].pt
                originalMatch.append( (int(x),int(y)) )

                x,y = keys[idx].pt
                templateMatch.append( (int(x),int(y)) )
            result.append(match*1.0/(match + unmatch))
        #print match,unmatch
        #return match,unmatch,originalMatch,templateMatch
        return result


#engine = Engine()
#img = engine.loadImage("images/cropped.jpg")
#imggrey = engine.greytifyImg(img)
#engine.extractSURF(imggrey)
#engine.trainKNN()
#engine.matching()
