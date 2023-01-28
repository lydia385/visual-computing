import cv2
from sklearn.metrics import mean_squared_error

import numpy as np
img1 = cv2.imread("image.png")
img2 = cv2.imread("image072.png")
grayImg2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


# Set the block size and search neighborhood size
block_size = (16, 16)
#step
search_size = 32

def get_center(i,j):    
     return (i+block_size[0]//2,j+block_size[0]//2)



def meanSquaredError(img1, img2):
        squared_diff = (img1 -img2) ** 2
        summed = np.sum(squared_diff)
        num_pix = img1.shape[0] * img1.shape[1] #img1 and 2 should have same shape
        err = summed / num_pix
        return err

# def meanSquaredError(img1,img2):
#    h, w ,_ = img1.shape
#    diff = cv2.subtract(img1, img2)
#    err = np.sum(diff**2)
#    mse = err/(float(h*w))
#    return mse




img = cv2.imread("image072.png")
img2 = cv2.imread("image.png")

#create black image 
black_img = np.zeros((img.shape[0], img.shape[1], 3), dtype = np.uint8)
black_img = 255*black_img


prev_frame =  cv2.cvtColor(img, cv2.COLOR_YCrCb2BGR)
frame = cv2.cvtColor(img2, cv2.COLOR_YCrCb2BGR)

# les frames avec carres
prev_frame_carre =  np.copy (img)
frame_carre = np.copy(img2)



# Divide the frame(395, 703, 3) into blocks 16*16
for i in range(0,frame.shape[0]-16, block_size[0]):
    for j in range(0, frame.shape[1]-16, block_size[1]):
# for i in range(150,151, block_size[0]):
#     for j in range(120, 121, block_size[1]):
        i_base=i
        j_base=j
        print("luda",i_base,j_base)
        # Get the current block
        targetBlock  = prev_frame[i:i+block_size[0], j:j+block_size[1]]

        # Search for the most similar block in the previous frame
        min_mse = float("inf")
        min_x = 0
        min_y = 0
        search_size = 32
        while search_size>=16 and i_base<=frame.shape[0]+block_size[0] and j_base<= frame.shape[1]+block_size[1]:
            for x in range(i_base-search_size,i_base+search_size+1,search_size):
                for y in range(j_base-search_size,j_base+search_size+1,search_size):
                        if(x>=0 and y>=0 and x+block_size[0]<frame.shape[0] and y+block_size[1]<frame.shape[1]):
                            SearchBlock=frame[x:x+block_size[0],y:y+block_size[1]]
                            
                            #cv2.rectangle(frame_carre, (y, x), (y+block_size[1], x+block_size[0]), (255, 255, 255), 2)
                            #cv2.rectangle(frame_carre, (y, x), (y+16, x+16), (200, 0, 0), 2)
                            mse = meanSquaredError(targetBlock , SearchBlock)
                            if mse < min_mse:
                                min_mse = mse
                                min_x = x
                                min_y = y
                            #print(x,y,i_base,j_base,mse)
            

            i_base=min_x
            j_base=min_y
            #print("/n",i_base,j_base,i,j,block_size)
            search_size=search_size//2
            
        
        
        #print(i,j,min_x,min_y)
        if (min_mse>50):
         # Calculate the residual
         #black_img[i:i+block_size[0],j:j+block_size[1]] = np.subtract(img2[min_x:min_x+block_size[0],min_y:min_y+block_size[1]],img[i:i+block_size[0], j:j+block_size[1]])
         black_img[i:i+block_size[0],j:j+block_size[1]] = img[i:i+block_size[0], j:j+block_size[1]]
         #  img2[min_x:min_x+block_size[0],min_y:min_y+block_size[1]] + img[i:i+block_size[0], j:j+block_size[1]]
        else :
         # Surround the block with a square 
         cv2.rectangle(frame_carre, (min_y, min_x), (min_y+block_size[1], min_x+block_size[0]), (0, 255, 0), 2)
        
        cv2.rectangle(prev_frame_carre, (j, i), (j+block_size[1], i+block_size[0]), (255, 255, 255), 2)


    

     
  

# Display the frame

cv2.imshow("resultat", frame_carre)
cv2.imshow("origine", prev_frame_carre)
cv2.imshow("black image", black_img)
cv2.waitKey(0)
