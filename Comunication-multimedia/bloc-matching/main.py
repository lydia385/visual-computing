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
k=0
v=255


def meanSquaredError(img1,img2):
        squared_diff = (img1 -img2) ** 2
        summed = np.sum(squared_diff)
        num_pix = img1.shape[0] * img1.shape[1] #img1 and 2 should have same shape
        err = summed / num_pix
        return err


img = cv2.imread("image072.png")
img2 = cv2.imread("image.png")

#create black image 
black_img = np.zeros((img.shape[0], img.shape[1], 3), dtype = np.uint8)
black_img = 255*black_img


prev_frame =  cv2.cvtColor(img, cv2.COLOR_YCrCb2BGR)
frame = cv2.cvtColor(img2, cv2.COLOR_YCrCb2BGR)

print(frame.shape)
#(395, 703, 3)
# Divide the frame into blocks 16*16
for i in range(0, frame.shape[0]-16, block_size[0]):
    for j in range(0, frame.shape[1]-16, block_size[1]):
        cv2.rectangle(img, (j, i), (j+block_size[1], i+block_size[0]), (k, k, k), 2)
        i_base=i
        j_base=j
        # Get the current block
        targetBlock  = prev_frame[i:i+block_size[0], j:j+block_size[1]]
        #center=get_center(block(i,j))

        # Search for the most similar block in the previous frame
        min_mse = float("inf")
        min_x = 0
        min_y = 0
        mse1=[]
        miin=[]
        search_size = 32
        while search_size!=1 and i_base<=frame.shape[0]+block_size[0] and j_base<= frame.shape[1]+block_size[1]:
            for x in range(i-search_size,i+search_size*2-1,search_size):
                for y in range(j-search_size,j+search_size*2-1,search_size):
                        if(x>=0 and y>=0 and (x!=i or y!=j) and x+block_size[0]<frame.shape[0] and y+block_size[1]<frame.shape[1]):
                           # print(i,j,search_size)
                            SearchBlock=frame[x:x+block_size[0],y:y+block_size[1]]
                            #cv2.rectangle(img2, (y, x), (y+block_size[1], x+block_size[0]), (100, 0 ,0), 2)
                            mse = meanSquaredError(targetBlock , SearchBlock)
                            if mse < min_mse:
                                mse1.append([mse,x,y])
                                min_mse = mse
                                min_x = x
                                min_y = y
           
            i_base=min_x
            j_base=min_y
            search_size=search_size//2
            
        
        
        # Calculate the residual
        print(i,j,min_x,min_y)
        black_img[i:i+block_size[0],j:j+block_size[1]] =  img2[i:i+block_size[0],j:j+block_size[1]] - img[min_x:min_x+block_size[0], min_y:min_y+block_size[1]]
    

    # Surround the similar block with a square of the same color
        cv2.rectangle(img2, (min_y, min_x), (min_y+block_size[1], min_x+block_size[0]), (k, k, k), 2)
        # cv2.rectangle(img, (j, i), (j+block_size[1], i+block_size[0]), (0, k, 0), 2)
        k+=20
  

# Display the frame


cv2.imshow("resultat", img2)
cv2.imshow("origine", img)
cv2.imshow("black image", black_img)
cv2.waitKey(0)
