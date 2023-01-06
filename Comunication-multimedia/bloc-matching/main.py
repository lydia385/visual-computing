import cv2
import numpy as np
img1 = cv2.imread("image.png")
img2 = cv2.imread("image072.png")
grayImg2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


block_size = (16, 16)
#step
search_size = 32

def get_center(i,j):    
     return (i+block_size[0]//2,j+block_size[0]//2)
i=0


def meanSquaredError(img1,img2):
        squared_diff = (img1 -img2) ** 2
        summed = np.sum(squared_diff)
        num_pix = img1.shape[0] * img1.shape[1] #img1 and 2 should have same shape
        err = summed / num_pix
        return err


img = cv2.imread("image072.png")
img2 = cv2.imread("image.png")


prev_frame =  cv2.cvtColor(img, cv2.COLOR_YCrCb2BGR)
frame = cv2.cvtColor(img2, cv2.COLOR_YCrCb2BGR)


# Divide the frame into blocks 16*16
for i in range(100, 101, block_size[0]):
    for j in range(100, 101, block_size[1]):
        # Get the current block
        targetBlock  = prev_frame[i:i+block_size[0], j:j+block_size[1]]
        #center=get_center(block(i,j))

        # Search for the most similar block in the previous frame
        min_mse = float("inf")
        min_x = 0
        min_y = 0
        search_size = 32
        while search_size!=1:
            for x in range(i-search_size,i+search_size*2,search_size):
                for y in range(j-search_size,j+search_size*2,search_size):
                        if(x>=0 and y>=0 and (x!=i or y!=j)):
                            SearchBlock=frame[x:x+block_size[0],y:y+block_size[1]]
                            #cv2.rectangle(prev_frame, (y, x), (y+block_size[1], x+block_size[0]), (0, 255, 0), 2)
                            print(x,y)
                            mse = meanSquaredError(targetBlock , SearchBlock)
                            if mse < min_mse:
                                min_mse = mse
                                min_x = x
                                min_y = y
            i=min_x
            j=min_y
            search_size=search_size//2
    
        # Calculate the residual
        # residual = block - prev_frame[min_x:min_x+block_size[0], min_y:min_y+block_size[1]]

        # # Surround the similar block with a square of the same color
        cv2.rectangle(frame, (min_y, min_x), (min_y+block_size[1], min_x+block_size[0]), (0, 255, 0), 2)
        cv2.rectangle(prev_frame, (100, 100), (100+block_size[1], 100+block_size[0]), (0, 255, 0), 2)

# Display the frame


cv2.imshow("resultat", frame)
cv2.imshow("origine", prev_frame)
cv2.waitKey(0)
