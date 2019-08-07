import cv2

vidcap = cv2.VideoCapture('permam.mp4')
success,image = vidcap.read()
count = 0
success = True
frame_list=[]
while success:
    cv2.imwrite("./dataset/frame%d.jpg" % count, image)     #
    success,image = vidcap.read()
    print ('Read a new frame: ', success)
    count += 1
    print(count)
    