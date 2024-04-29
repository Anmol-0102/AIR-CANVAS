# All the imports go here
import cv2
import numpy as np
import mediapipe as mp
from collections import deque

# Giving different arrays to handle color points of different colors
bpoints = [deque(maxlen=1024)]  # blue color
gpoints = [deque(maxlen=1024)]  # green color
rpoints = [deque(maxlen=1024)]  # red color
ypoints = [deque(maxlen=1024)]  # yellow color
wpoints = [deque(maxlen=1024)]  # White color
ppoints = [deque(maxlen=1024)]  # Purple color
opoints = [deque(maxlen=1024)]  # Orange color

# These indexes will be used to mark the points in particular arrays of specific color
blue_index = 0
green_index = 0
red_index = 0
yellow_index = 0
white_index = 0
purple_index = 0
orange_index = 0

# The kernel to be used for dilation purpose
kernel = np.ones((10, 10), np.uint8)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255),
          (255, 255, 255), (128, 0, 128), (0, 165, 255)]
colorIndex = 0

# Here is code for Canvas setup
paintWindow = np.zeros((1200, 1000, 3)) + 255
paintWindow = cv2.rectangle(paintWindow, (30, 1), (120, 45), (0, 0, 0), 2)
paintWindow = cv2.rectangle(paintWindow, (140, 1), (235, 45), (255, 0, 0), 2)
paintWindow = cv2.rectangle(paintWindow, (255, 1), (350, 45), (0, 255, 0), 2)
paintWindow = cv2.rectangle(paintWindow, (370, 1), (465, 45), (0, 0, 255), 2)
paintWindow = cv2.rectangle(paintWindow, (485, 1), (580, 45), (0, 255, 255), 2)
paintWindow = cv2.rectangle(paintWindow, (600, 1), (695, 45), (0, 0, 0), 2)
paintWindow = cv2.rectangle(paintWindow, (715, 1), (810, 45), (128, 0, 128), 2)
paintWindow = cv2.rectangle(paintWindow, (830, 1), (925, 45), (0, 165, 255), 2)

cv2.putText(paintWindow, "CLEAR", (39, 23), cv2.FONT_HERSHEY_SIMPLEX,
            0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "BLUE", (165, 23), cv2.FONT_HERSHEY_SIMPLEX,
            0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "GREEN", (278, 23), cv2.FONT_HERSHEY_SIMPLEX,
            0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "RED", (400, 23), cv2.FONT_HERSHEY_SIMPLEX,
            0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "YELLOW", (500, 23), cv2.FONT_HERSHEY_SIMPLEX,
            0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "WHITE", (630, 23), cv2.FONT_HERSHEY_SIMPLEX,
            0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "PURPLE", (745, 23), cv2.FONT_HERSHEY_SIMPLEX,
            0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "ORANGE", (850, 23), cv2.FONT_HERSHEY_SIMPLEX,
            0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.namedWindow('Paint', cv2.WINDOW_AUTOSIZE)

# initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

# Initialize the webcam
cap = cv2.VideoCapture(0)
ret = True
while ret:
    # Read each frame from the webcam
    ret, frame = cap.read()

    # Increase the size of live video
    frame = cv2.resize(frame, (1000, 800))

    x, y, c = frame.shape

    # Flip the frame vertically
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frame = cv2.rectangle(frame, (30, 1), (120, 45), (0, 0, 0), 2)
    frame = cv2.rectangle(frame, (140, 1), (235, 45), (255, 0, 0), 2)
    frame = cv2.rectangle(frame, (255, 1), (350, 45), (0, 255, 0), 2)
    frame = cv2.rectangle(frame, (370, 1), (465, 45), (0, 0, 255), 2)
    frame = cv2.rectangle(frame, (485, 1), (580, 45), (0, 255, 255), 2)
    frame = cv2.rectangle(frame, (600, 1), (695, 45), (255, 255, 255), 2)
    frame = cv2.rectangle(frame, (715, 1), (810, 45), (128, 0, 128), 2)
    frame = cv2.rectangle(frame, (830, 1), (925, 45), (0, 165, 255), 2)
    
    cv2.putText(frame, "CLEAR", (39, 23), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "BLUE", (165, 23), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "GREEN", (278, 23), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "RED", (400, 23), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "YELLOW", (500, 23), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "WHITE", (630, 23), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "PURPLE", (735, 23), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "ORANGE", (850, 23), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 0), 2, cv2.LINE_AA)

    # Get hand landmark prediction
    result = hands.process(framergb)

    # post-process the result
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                lmx = int(lm.x * 1000)
                lmy = int(lm.y * 800)
                landmarks.append([lmx, lmy])

            # Drawing landmarks on frames
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)
        fore_finger = (landmarks[8][0], landmarks[8][1])
        center = fore_finger
        thumb = (landmarks[4][0], landmarks[4][1])
        cv2.circle(frame, center, 3, (0, 255, 0), -1)

        if (thumb[1] - center[1] < 40):
            bpoints.append(deque(maxlen=512))
            blue_index += 1
            gpoints.append(deque(maxlen=512))
            green_index += 1
            rpoints.append(deque(maxlen=512))
            red_index += 1
            ypoints.append(deque(maxlen=512))
            yellow_index += 1
            wpoints.append(deque(maxlen=512))
            white_index += 1
            ppoints.append(deque(maxlen=512))
            purple_index += 1
            opoints.append(deque(maxlen=512))
            orange_index += 1

        elif center[1] <= 55:
            if 30 <= center[0] <= 120:  # Clear Button
                bpoints = [deque(maxlen=512)]
                gpoints = [deque(maxlen=512)]
                rpoints = [deque(maxlen=512)]
                ypoints = [deque(maxlen=512)]
                wpoints = [deque(maxlen=512)]
                ppoints = [deque(maxlen=512)]
                opoints = [deque(maxlen=512)]

                blue_index = 0
                green_index = 0
                red_index = 0
                yellow_index = 0
                white_index = 0
                purple_index = 0
                orange_index = 0

                paintWindow[67:, :, :] = 255
            elif 140 <= center[0] <= 235:
                colorIndex = 0  # Blue
            elif 255 <= center[0] <= 350:
                colorIndex = 1  # Green
            elif 370 <= center[0] <= 465:
                colorIndex = 2  # Red
            elif 485 <= center[0] <= 580:
                colorIndex = 3  # Yellow
            elif 600 <= center[0] <= 695:
                colorIndex = 4  # White
            elif 715 <= center[0] <= 810:
                colorIndex = 5  # Purple
            elif 830 <= center[0] <= 925:
                colorIndex = 6  # Orange
        else:
            if colorIndex == 0:
                bpoints[blue_index].appendleft(center)
            elif colorIndex == 1:
                gpoints[green_index].appendleft(center)
            elif colorIndex == 2:
                rpoints[red_index].appendleft(center)
            elif colorIndex == 3:
                ypoints[yellow_index].appendleft(center)
            elif colorIndex == 4:
                wpoints[white_index].appendleft(center)
            elif colorIndex == 5:
                ppoints[purple_index].appendleft(center)
            elif colorIndex == 6:
                opoints[orange_index].appendleft(center)

    # Append the next deques when nothing is detected to avoid messing up
    else:
        bpoints.append(deque(maxlen=512))
        blue_index += 1
        gpoints.append(deque(maxlen=512))
        green_index += 1
        rpoints.append(deque(maxlen=512))
        red_index += 1
        ypoints.append(deque(maxlen=512))
        yellow_index += 1
        wpoints.append(deque(maxlen=512))
        white_index += 1
        ppoints.append(deque(maxlen=512))
        purple_index += 1
        opoints.append(deque(maxlen=512))
        orange_index += 1

    # Draw lines of all the colors on the canvas and frame
    points = [bpoints, gpoints, rpoints, ypoints, wpoints, ppoints, opoints]
    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(1, len(points[i][j])):
                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue
                
                cv2.line(frame, points[i][j][k - 1],
                         points[i][j][k], colors[i], 2)
                
                cv2.line(paintWindow, points[i][j][k - 1],
                         points[i][j][k], colors[i], 2)

    cv2.imshow("Output", frame)
    cv2.imshow("Paint", paintWindow)

    if cv2.waitKey(1) == ord('q'):
        break

# release the webcam and destroy all active windows
cap.release()
cv2.destroyAllWindows()
