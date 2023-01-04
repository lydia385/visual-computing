import cv2

img1 = cv2.imread("image.png")
img2 = cv2.imread("image072.png")
grayImg2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


blocksize = 16

def get_center(i,j):    
     return (i+blocksize//2,j+blocksize//2)
i=0
while i<=img1.shape[0]-blocksize:
    j=0
    while j<=img1.shape[1]-blocksize:
        targetimage =grayImg2[i:i+blocksize,j:j+blocksize]
        print(get_center(i,j))
        j+=blocksize
    i+=blocksize