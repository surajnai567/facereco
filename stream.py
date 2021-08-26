import numpy as np
import cv2
import dlib
from threading import Thread
from queue import Queue
import time

# go to the setting find ip cam username and password if it is not empty use
# first one
# cap = cv2.VideoCapture('http://username:password@ip:port/video')
capture = cv2.VideoCapture(1)
#capture = cv2.VideoCapture(0)
detector = dlib.full_object_detection()
queue = Queue()


def capture_frame(cap):
    while cap.isOpened():
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        res = detector(gray)
        print(res)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


capture_frame(capture)
def process_frame():
    while 1:
        if not queue.empty():
            frame = queue.get()
            cv2.imshow('frame', frame)
            res = detector(frame, 0)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


if __name__ == "__main__":
    #capture_frame(capture)
    #capture = Thread(target=capture_frame, args=[capture]).start()
    #process = Thread(target=process_frame).start()
    pass

