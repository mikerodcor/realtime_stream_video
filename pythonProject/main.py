from platform import java_ver

import cv2

vid_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)


def change_video_properties(brightness):#, contrast, saturation, exposure, sharpness):
    vid_capture.set(cv2.CAP_PROP_BRIGHTNESS, int(brightness))


def take_photo():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite('webcamphoto1.jpg', frame)
    cap.release()


if (vid_capture.isOpened() == False):
    print('Error device, camera not found')
else:
    fps = vid_capture.get(5)
    print('Frames per second : ', fps, 'FPS')

    frame_count = vid_capture.get(7)
    print('Frame count : ', frame_count)

    while (vid_capture.isOpened()):
        ret, frame = vid_capture.read()
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
#Change parameters
        if cv2.waitKey(2) & 0xFF == ord('B'):
            brightness = vid_capture.get(cv2.CAP_PROP_BRIGHTNESS)
            vid_capture.set(cv2.CAP_PROP_BRIGHTNESS, brightness+10)
            print('\nBrightness: ', brightness)
        #, contrast, saturation, exposure, sharpness)

        if cv2.waitKey(2) & 0xFF == ord('b'):
            brightness = vid_capture.get(cv2.CAP_PROP_BRIGHTNESS)
            vid_capture.set(cv2.CAP_PROP_BRIGHTNESS, brightness-10)
            print('\nBrightness: ', brightness)

        if cv2.waitKey(2) & 0xFF == ord('C'):
            contrast = vid_capture.get(cv2.CAP_PROP_CONTRAST)
            vid_capture.set(cv2.CAP_PROP_CONTRAST, contrast + 1)
            print('\nContrast:', contrast)
        if cv2.waitKey(2) & 0xFF == ord('c'):
            contrast = vid_capture.get(cv2.CAP_PROP_CONTRAST)
            vid_capture.set(cv2.CAP_PROP_CONTRAST, contrast - 1)
            print('\nContrast:', contrast)

vid_capture.release()
cv2.destroyAllWindows()
