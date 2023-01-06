import cv2
import numpy as np


# Load the video
video = cv2.VideoCapture("video.mp4")

# Set the block size and search neighborhood size
block_size = (16, 16)
search_size = 32

# Set the color for the squares around the similar blocks
color = (0, 255, 0)


def MSE(img1,img2):
        squared_diff = (img1 -img2) ** 2
        summed = np.sum(squared_diff)
        num_pix = img1.shape[0] * img1.shape[1] #img1 and 2 should have same shape
        err = summed / num_pix
        return err
# Initialize the previous frame
_, prev_frame = video.read()
prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

while True:
    # Read the next frame
    _, frame = video.read()
    if frame is None:
        break

    # Convert the frame to grayscale
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Divide the frame into blocks 16*16
    for i in range(0, frame.shape[0], block_size[0]):
        for j in range(0, frame.shape[1], block_size[1]):
            # Get the current block
            block = frame[i:i+block_size[0], j:j+block_size[1]]

            # Search for the most similar block in the previous frame
            min_mse = float("inf")
            min_x = 0
            min_y = 0
            for x in range(i-search_size[0], i+search_size[0]//2+1, block_size[0]):
                for y in range(j-search_size[1]//2, j+search_size[1]//2+1, block_size[1]):
                    ref_block = prev_frame[x:x+block_size[0], y:y+block_size[1]]
                    mse = cv2.meanSquaredError(block, ref_block)[0]
                    if mse < min_mse:
                        min_mse = mse
                        min_x = x
                        min_y = y

            # Calculate the residual
            residual = block - prev_frame[min_x:min_x+block_size[0], min_y:min_y+block_size[1]]

            # Surround the similar block with a square of the same color
            cv2.rectangle(frame, (min_y, min_x), (min_y+block_size[1], min_x+block_size[0]), color, 2)

    # Display the frame
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    # Update the previous frame
    prev_frame = frame

# Release the video
video.release()
