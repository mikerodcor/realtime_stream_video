import numpy as np
import datetime
import cv2 as cv
import os



vid_capture = cv.VideoCapture(0, cv.CAP_DSHOW)
vid_capture.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
vid_capture.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
chessboardSize = (7, 14)

frame_width = int(vid_capture.get(3))
frame_height = int(vid_capture.get(4))
frame_size = (frame_width,frame_height)
fps = 20

corners = np.array([
    [[506, 40]], [[544, 38]], [[584, 37]], [[623, 37]], [[662, 38]], [[705, 40]], [[743, 42]],
    [[500, 59]], [[540, 57]], [[581, 57]], [[622, 57]], [[664, 57]], [[707, 59]], [[748, 51]],
    [[493, 81]], [[535, 79]], [[578, 79]], [[622, 79]], [[665, 79]], [[712, 81]], [[754, 83]],
    [[486, 105]], [[530, 103]], [[575, 103]], [[621, 103]], [[667, 103]], [[715,105]], [[760, 107]],
    [[479, 132]], [[525, 131]], [[572, 130]], [[620, 130]], [[668, 130]], [[720, 132]],  [[767, 135]],
    [[470, 165]], [[518, 164]], [[569, 163]], [[619, 163]], [[670, 164]], [[724, 165]], [[774, 168]],
    [[460, 200]], [[512, 199]], [[564, 198]], [[618, 198]], [[673, 199]], [[730, 201]], [[781, 203]],
    [[451, 239]], [[505, 238]], [[561, 238]], [[618, 238]], [[675, 238]], [[735, 240]], [[789, 242]],
    [[442, 283]], [[498, 282]], [[557, 282]], [[617, 282]], [[677, 283]], [[740, 284]], [[798, 285]],
    [[431, 331]], [[491, 332]], [[552, 332]], [[616, 333]], [[680, 334]], [[747, 334]], [[807, 334]],
    [[422, 385]], [[484, 386]], [[549, 387]], [[615, 388]], [[682, 389]], [[753, 388]], [[818, 388]],
    [[411, 448]], [[476, 351]], [[545, 454]], [[614, 454]], [[685, 454]], [[759, 453]], [[826, 451]],
    [[403, 511]], [[470, 516]], [[541, 512]], [[614, 521]], [[688, 521]], [[765, 518]],  [[833, 514]],
    [[395, 578]], [[495, 585]], [[538, 590]], [[614, 591]], [[691, 591]], [[771, 587]], [[840, 582]]
], dtype=np.float32)

objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboardSize[0], 0:chessboardSize[1]].T.reshape(-1, 2)

objPoints = [objp]  # List of object point arrays
imgPoints = [corners]  # List of image point arrays



def perpectiveTransform( pts1, pts2, img):
    matrix = cv.getPerspectiveTransform(pts1, pts2)
    result = cv.warpPerspective(img, matrix, (591, 886))
    return result


idImage = 2
def calculate_moving_average(curve, radius):
    window_size= 2 * radius + 1
    kernel = np.ones(window_size) / window_size
    curve_padded = np.lib.pad(curve, (radius, radius), 'edge')
    smooted_curve = np.convolve(curve_padded, kernel, mode= 'same')
    return smooted_curve

def undistorVideo(mx, my):
    dst = cv.remap(frame, mx, my, cv.INTER_LINEAR)
    fps = cv.CAP_PROP_FPS
    print("FPS: ",fps)
    # Resize image distorted and transformed
    resizedst = cv.resize(dst, (1280, 720))
    pt1 = np.float32([[491, 58], [823, 58], [365, 664], [945, 664]])
    pt2 = np.float32([[0, 0], [591, 0], [0, 873], [465.6, 873]])
    ptfm = perpectiveTransform(pt1, pt2, resizedst)

    return  ptfm


def take_photo(idImg):
    path = 'C:/Users/rafal/PYCAM'
    imgName = f'cam_140_{idImg}.jpg'
    cv.imwrite(imgName, frame)
    cv.imshow('Current photo', frame )
    cv.waitKey(4)
    idImg=+1
    print(idImage)




print('Resolution', frame_size)


if (vid_capture.isOpened() == False):
    print('Error device, camera not found')
else:
    fps = vid_capture.get(5)
    print('Frames per second : ', fps, 'FPS')

    frame_count = vid_capture.get(7)
    print('Frame count: ', frame_count)

    while (vid_capture.isOpened()):

        frame_width = int(vid_capture.get(3))
        frame_height = int(vid_capture.get(4))
        frame_size = (frame_width, frame_height)

        ret, frame = vid_capture.read()
        vid_capture.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
        vid_capture.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
        chessboardSize = (7, 14)
        ret, cameraMatrix, dist, rvecs, tvecs = cv.calibrateCamera(objPoints, imgPoints, frame_size, None, None)

        mapx, mapy = cv.initUndistortRectifyMap(cameraMatrix, dist, None, None, (1480, 920), 5)

        distFrame = undistorVideo(mapx, mapy)
        cv.imshow('Frame', distFrame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
      #  if (cv.waitKey(5) & 0xFF == ord('T') and frame_size == (1280, 720) or frame_size == (591, 886)):


        if cv.waitKey(1) & 0xFF == ord('1'):
            vid_capture.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
            vid_capture.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)

        if cv.waitKey(1) & 0xFF == ord('2'):
            vid_capture.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
            vid_capture.set(cv.CAP_PROP_FRAME_HEIGHT, 720)

        if cv.waitKey(1) & 0xFF == ord('3'):
            vid_capture.set(cv.CAP_PROP_FRAME_WIDTH, 640)
            vid_capture.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

        if cv.waitKey(1) & 0xFF == ord(' '):
            take_photo(idImage)

       #Implements the logic to get undistort video capture
       # if (cv.waitKey(3) & 0xFF == ord)

        if cv.waitKey(2) & 0xFF == ord('B'):
            brightness = vid_capture.get(cv.CAP_PROP_BRIGHTNESS)
            brightness =+ 10
            vid_capture.set(cv.CAP_PROP_BRIGHTNESS, brightness)
            print('\nBrightness: ', brightness)


        if cv.waitKey(2) & 0xFF == ord('b'):
            brightness = vid_capture.get(cv.CAP_PROP_BRIGHTNESS)
            brightness =- 10
            vid_capture.set(cv.CAP_PROP_BRIGHTNESS, brightness)
            print('\nBrightness: ', brightness)

        if cv.waitKey(2) & 0xFF == ord('C'):
            contrast = vid_capture.get(cv.CAP_PROP_CONTRAST)
            contrast =+ 1
            vid_capture.set(cv.CAP_PROP_CONTRAST, contrast)
            print('\nContrast:', contrast)
        if cv.waitKey(2) & 0xFF == ord('c'):
            contrast = vid_capture.get(cv.CAP_PROP_CONTRAST)
            contrast =- 1
            vid_capture.set(cv.CAP_PROP_CONTRAST, contrast)
            print('\nContrast:', contrast)

        if cv.waitKey(2) & 0xFF == ord('S'):
            sharpness = vid_capture.get(cv.CAP_PROP_SHARPNESS)
            sharpness =+ 6
            vid_capture.set(cv.CAP_PROP_SHARPNESS, sharpness)
            print('Sharpness', sharpness)
        if cv.waitKey(2) & 0xFF == ord('s'):
            sharpness = vid_capture.get(cv.CAP_PROP_SHARPNESS)
            sharpness =- 6
            vid_capture.set(cv.CAP_PROP_SHARPNESS, sharpness)
            print('Sharpness', sharpness)

        if cv.waitKey(2) & 0xFF == ord('E'):
            exposure = vid_capture.get(cv.CAP_PROP_EXPOSURE)
            exposure =+ 1
            exposure = vid_capture.set(cv.CAP_PROP_EXPOSURE, exposure)
            print('x', exposure)
        if cv.waitKey(2) & 0xFF == ord('e'):
            exposure = vid_capture.get(cv.CAP_PROP_EXPOSURE)
            exposure =-1
            exposure = vid_capture.set(cv.CAP_PROP_EXPOSURE, exposure)
            print('x', exposure)

        if cv.waitKey(2) & 0xFF == ord('H'):
            hue = vid_capture.get(cv.CAP_PROP_HUE)
            hue =+ 1
            hue = vid_capture.set(cv.CAP_PROP_HUE, hue)
            print('x', hue)
        if cv.waitKey(2) & 0xFF == ord('h'):
            hue = vid_capture.get(cv.CAP_PROP_HUE)
            hue =- 1
            hue = vid_capture.set(cv.CAP_PROP_HUE, hue)
            print('x', hue)

        if cv.waitKey(2) & 0xFF == ord('R'):
            saturation = vid_capture.get(cv.CAP_PROP_SATURATION)
            saturation =+ 5
            saturation = vid_capture.set(cv.CAP_PROP_SATURATION, saturation)
            print('x', saturation)
        if cv.waitKey(2) & 0xFF == ord('r'):
            saturation = vid_capture.get(cv.CAP_PROP_SATURATION)
            saturation =- 5
            saturation = vid_capture.set(cv.CAP_PROP_SATURATION, saturation)
            print('x', saturation)

vid_capture.release()
cv.destroyAllWindows()
