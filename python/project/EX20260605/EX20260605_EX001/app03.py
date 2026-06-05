import cv2
import numpy as np

# # 원 생성
# circleBG = np.zeros((480, 640, 3), dtype=np.uint8)
# COLOR = (225, 225, 0)  # 색상
# RADIUS = 100  # 
# THINKNESS = 3   # 테두리 선 두께

# cv2.circle(circleBG,    (150, 150), RADIUS, COLOR, THINKNESS, cv2.LINE_AA)
# #         어디에그릴거니?                        색상     두께       선타입
# cv2.circle(circleBG,    (450, 150), RADIUS, COLOR, cv2.FILLED, cv2.LINE_AA)

# cv2.imshow('title-circle', circleBG)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # 사각형
# rectangleBG = np.zeros((480, 640, 3), dtype=np.uint8)
# COLOR = (225, 225, 0) # 색상
# THINKNESS = 3  # 테두리 선 두께

# cv2.rectangle(rectangleBG, (50, 100), (200, 200),COLOR, THINKNESS, cv2.LINE_AA)
# #             어디에그릴거니? 좌상단      우상단     색상     두께       선타입
# cv2.rectangle(rectangleBG, (450, 150), (50, 100),COLOR, cv2.FILLED, cv2.LINE_AA)

# cv2.imshow('title-rectangle', rectangleBG)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # 다각형
# polygonBG = np.zeros((480, 640, 3), dtype=np.uint8)

# COLOR = (225, 225, 0) # 색상
# THINKNESS = 3  # 테두리 선 두께

# points = np.array([
#     [50, 50],
#     [150, 150],
#     [50, 150]
# ])

# cv2.polylines(polygonBG,  [points],          True,               COLOR, THINKNESS, cv2.LINE_AA)
# #          어디에그릴거니?   어떤녀석그릴거니?    닫힌도형 or 열린도형    색상     두께       선타입

# cv2.imshow('title-polygon', polygonBG)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # 이미지 복사 저장
# robotImgGrayscale = cv2.imread('./res/img/robot.jpg', cv2.IMREAD_GRAYSCALE)
# robotImgGrayscale = cv2.resize(robotImgGrayscale, (384, 575))

# # cv2.imshow('title-robotImgGrayscale', robotImgGrayscale)

# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# result = cv2.imwrite('./save/img/robot_grayscale.jpg', robotImgGrayscale)
# print(f'result: {result}') # 저장 성공 = True , 저장 실패 = False


# 동영상 복사 저장
robotMOV = cv2.VideoCapture('./res/mov/robot.mp4')

# 코덱 정의
furcc = cv2.VideoWriter_fourcc(*'DIVX')  #  *'DIVX' == 'D', 'I', 'V', 'X'


width = int(robotMOV.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(robotMOV.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = robotMOV.get(cv2.CAP_PROP_FPS)



robotMovOutput = cv2.VideoWriter('./save/mov/robot_output.mp4', furcc, fps, (width, height))
while robotMOV.isOpened:
    result, frame = robotMOV.read()
    if not result:
        print('movie end!')
        break
    
    robotMovOutput.write(frame)

    frame = cv2.resize(frame, (384, 575))
    cv2.imshow('title-robotMOV', frame)

    if cv2.waitKey(1) == ord('q'):
        print('movie end!')
        break

robotMOV.release()
cv2.destroyAllWindows()

 