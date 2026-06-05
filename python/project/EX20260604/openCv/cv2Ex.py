import cv2
import numpy as np

# ## 스케치북 생성
# # 세로 480, 가로 640 3채널

# sketchbookImg = np.zeros((480, 640, 3), dtype=np.uint8)
# cv2.imshow('title-sketchbookImg', sketchbookImg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # 흰색 스케치북 
# sketchbookImg = np.zeros((480, 640, 3), dtype=np.uint8)
# sketchbookImg[:] = (0, 0, 0)    # R G B 0~255
# cv2.imshow('title-sketchbookImg', sketchbookImg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# # 특정 영역 색칠하기
# sketchbookImg =np.zeros((480, 640, 3), dtype = np.uint8)
# sketchbookImg[:] = (0, 0, 0)

# sketchbookImg [100:200, 300:400] = (255,255,255)

# sketchbookImg [300:400, 100:200] = (0,255,255)

# cv2.imshow('title-sketchbookImg', sketchbookImg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# 직선 만들기
sketchbookImg =np.zeros((480, 640, 3), dtype = np.uint8)
sketchbookImg[:] = (0, 0, 0)

COLOR_4 = (0, 0, 255)  # RED
COLOR_8 = (0, 255, 0)  # GREEN
COLOR_A = (255, 0, 0)  # BLUE
THINKNESS = 3   

cv2.line('sketchbookImg', (10, 10), (400, 400), COLOR_4, THINKNESS, cv2.LINE_4)         
           # 만들 위치     # 시작 점   # 끝나는 점 # 색상    #  두꼐     # 라인 타입

cv2.line('sketchbookImg', (10, 10), (400, 400), COLOR_4, THINKNESS, cv2.LINE_8)      
           # 만들 위치     # 시작 점   # 끝나는 점 # 색상    #  두꼐     # 라인 타입
cv2.line('sketchbookImg', (10, 10), (400, 400), COLOR_4, THINKNESS, cv2.LINE_AA)      

cv2.imshow('title-sketchbookImg', sketchbookImg)
cv2.waitKey(0)
cv2.destroyAllWindows()




