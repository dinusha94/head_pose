import argparse
import cv2
import numpy as np
import os.path as osp
import headpose


def main():
    
    cap = cv2.VideoCapture(0)
    cap.set(3, 720)
    cap.set(4, 480)
    
    # Initialize head pose detection
    hpd = headpose.HeadposeDetection(1, 'model/shape_predictor_68_face_landmarks.dat')

    count = 0
    while(cap.isOpened()):
        # Capture frame-by-frame
        #print('\rframe: %d' % count, end='')
        ret, frame = cap.read()
        

        frame = cv2.flip(frame, 1)
        frame, angles = hpd.process_image(frame)
        print(angles)
            # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            headpose.t.summary()
            break

        count += 1

    # When everything done, release the capture
    cap.release()
    if isVideo: out.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    
    main()
