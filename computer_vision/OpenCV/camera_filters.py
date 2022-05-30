import cv2
import sys
import numpy

PREVIEW = 0
BLUR = 1
FEATURES = 2
CANNY = 3

feature_para = dict(
    maxCorners=500,
    qualityLevel=0.2,
    minDistance=15,
    blockSize=9
)

s = 0
if len(sys.argv) < 1:
    s = sys.argv[1]

image_filter = PREVIEW
alive = True
win_name= "Camera"

source = cv2.VideoCapture(s)

while alive:
    has_frames, frame = source.read()
    if not has_frames:
        break

    if image_filter == PREVIEW:
        result = frame
    elif image_filter == CANNY:
        result = cv2.Canny(frame, 145, 150)
    elif  image_filter == BLUR:
        result = cv2.blur(frame, (13,13))
    elif image_filter == FEATURES:
        result = frame
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(frame_gray, **feature_para)
        if corners is not None:
            for x,y in numpy.float32(corners).reshape(-1, 2):
                cv2.circle(result, (x,y), 10, (0,255,0), 1)
    
    cv2.imshow(win_name, result)

    key = cv2.waitKey(1)
    if key == ord("q") or key == ord("Q") or key == 27:
        