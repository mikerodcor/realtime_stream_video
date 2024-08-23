import numpy as np
import datetime
import cv2
import os

vid_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

fechaHora = datetime.datetime.now()
idImage = 2
def calculate_moving_average(curve, radius):
    window_size= 2 * radius + 1
    kernel = np.ones(window_size) / window_size
    curve_padded = np.lib.pad(curve, (radius, radius), 'edge')
    smooted_curve = np.convolve(curve_padded, kernel, mode= 'same')
    return smooted_curve

def take_photo(idImg):
    path = 'C:/Users/rafal/PYCAM'
    imgName = f'cam_140_{idImg}.jpg'
    cv2.imwrite(imgName, frame)
    cv2.imshow('Current photo', frame )
    cv2.waitKey(4)
    idImgq=+1
    print(idImage)



frame_width = int(vid_capture.get(3))
frame_height = int(vid_capture.get(4))
frame_size = (frame_width,frame_height)
fps = 20

print('Resolution', frame_size)

if (vid_capture.isOpened() == False):
    print('Error device, camera not found')
else:
    fps = vid_capture.get(5)
    print('Frames per second : ', fps, 'FPS')

    frame_count = vid_capture.get(7)
    print('Frame count: ', frame_count)

    while (vid_capture.isOpened()):
        ret, frame = vid_capture.read()
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if cv2.waitKey(1) & 0xFF == ord('1'):
            vid_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
            vid_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

        if cv2.waitKey(1) & 0xFF == ord('2'):
            vid_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
            vid_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        if cv2.waitKey(1) & 0xFF == ord('3'):
            vid_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            vid_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        if cv2.waitKey(1) & 0xFF == ord(' '):
            take_photo(idImage)


        if cv2.waitKey(2) & 0xFF == ord('B'):
            brightness = vid_capture.get(cv2.CAP_PROP_BRIGHTNESS)
            vid_capture.set(cv2.CAP_PROP_BRIGHTNESS, brightness+10)
            print('\nBrightness: ', brightness)


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

        if cv2.waitKey(2) & 0xFF == ord('S'):
            sharpness = vid_capture.get(cv2.CAP_PROP_SHARPNESS)
            vid_capture.set(cv2.CAP_PROP_SHARPNESS, sharpness +6)
            print('Sharpness', sharpness)
        if cv2.waitKey(2) & 0xFF == ord('s'):
            sharpness = vid_capture.get(cv2.CAP_PROP_SHARPNESS)
            vid_capture.set(cv2.CAP_PROP_SHARPNESS, sharpness -6)
            print('Sharpness', sharpness)

        if cv2.waitKey(2) & 0xFF == ord('E'):
            exposure = vid_capture.get(cv2.CAP_PROP_EXPOSURE)

            exposure = vid_capture.set(cv2.CAP_PROP_EXPOSURE, exposure + 1)
            print('x', exposure)
        if cv2.waitKey(2) & 0xFF == ord('e'):
            exposure = vid_capture.get(cv2.CAP_PROP_EXPOSURE)
            exposure = vid_capture.set(cv2.CAP_PROP_EXPOSURE, exposure - 1)
            print('x', exposure)

        if cv2.waitKey(2) & 0xFF == ord('E'):
            hue = vid_capture.get(cv2.CAP_PROP_HUE)

            hue = vid_capture.set(cv2.CAP_PROP_HUE, hue + 1)
            print('x', hue)
        if cv2.waitKey(2) & 0xFF == ord('h'):
            hue = vid_capture.get(cv2.CAP_PROP_HUE)
            hue = vid_capture.set(cv2.CAP_PROP_HUE, hue - 1)
            print('x', hue)

        if cv2.waitKey(2) & 0xFF == ord('R'):
            saturation = vid_capture.get(cv2.CAP_PROP_SATURATION)
            saturation = vid_capture.set(cv2.CAP_PROP_SATURATION, saturation + 5)
            print('x', saturation)
        if cv2.waitKey(2) & 0xFF == ord('r'):
            saturation = vid_capture.get(cv2.CAP_PROP_SATURATION)
            saturation = vid_capture.set(cv2.CAP_PROP_SATURATION, saturation - 5)
            print('x', saturation)

vid_capture.release()
cv2.destroyAllWindows()
