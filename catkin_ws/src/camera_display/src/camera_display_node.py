#!/usr/bin/env python

import rospy
import cv2 as cv

# def image_callback(msg):
#     #bridge = CvBridge()
#     #cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
#     #cv2.imshow("Camera", cv_image)
#     cv2.imshow("Camera", cv_image)
#     cv2.waitKey(1)

''' Movido a main
def camera_display():
    while True:
    #rospy.Subscriber("/camera_topic", Image, image_callback)
    #rospy.Subscriber('/camera/image_raw', Image, image_callback)

        if not vid.isOpened():
            print("Cannot open camera")
            exit()

        ret, cv_image = vid.read()
        cv.imshow("Camera", cv_image)
        if cv.waitKey(1) == ord('q'):
            #
            # exit()
            break
'''

if __name__ == '__main__':
    vid = cv.VideoCapture(0)
    while True:

        if not vid.isOpened():
            print("Cannot open camera")
            exit()

        ret, cv_image = vid.read()
        cv.imshow("Camera", cv_image)
        if cv.waitKey(1) == ord('q'):
            #
            # exit()
            break
    vid.release()
    cv.destroyAllWindows()