from skimage.metrics import structural_similarity
import cv2


class ImageSimilarity:
    def __init__(self, image1, image2):
        self.image1 = image1
        self.image2 = image2

    # Works well with images of different dimensions
    def orb_sim(self):
        orb = cv2.ORB_create()

        # Detect key points and descriptors
        kp_a, desc_a = orb.detectAndCompute(self.image1, None)
        kp_b, desc_b = orb.detectAndCompute(self.image2, None)

        # Define the bruteforce matcher object
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        # Perform matches
        matches = bf.match(desc_a, desc_b)
        # Look for similar regions with distance < 50. Goes from 0 100
        similar_regions = [i for i in matches if i.distance < 50]
        if len(matches) == 0:
            return 0
        return len(similar_regions) / len(matches)

    # Needs images to be same dimensions
    def structural_sim(self):

        sim, diff = structural_similarity(self.image1, self.image2, full=True)
        return sim




