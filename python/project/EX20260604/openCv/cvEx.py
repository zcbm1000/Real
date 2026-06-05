import cv2

# # 버전 확인
# print(cv2.__version__) # 4.13.0 버전

# # 이미지 불러와서 출력하기
# airplaneImg = cv2.imread('./res/img/airplane.jpg') # 이미지 읽기


# print(f'airplaneImg shape: {airplaneImg.shape}')   # 이미지 크기(6000, 4000, 3)(세로,가로,채널 수)
# airplaneImg = cv2.resize(airplaneImg, (600,400))   # 사이즈 조절(가로 600, 세로 400)
# # cv2.imshow(윈도우 이름,출력할 이름)
# cv2.imshow('title_airplane', airplaneImg)          # 이미지 출력ㄴ
# cv2.waitKey(0)                                     # 3000은 밀리세컨드 3초동안 이미지 출력 | 0은 키입력할때까지 대기
# cv2.destroyAllWindows()                            # 모든 창 닫기



# # 읽기 옵션
# airplaneImgColor = cv2.imread('./res/img/airplane.jpg', cv2.IMREAD_COLOR) # 이미지 읽기
# airplaneImgColor = cv2.resize(airplaneImgColor, (600,400))   # 사이즈 조절(가로 600, 세로 400)

# airplaneImgGray = cv2.imread('./res/img/airplane.jpg', cv2.IMREAD_GRAYSCALE) # 이미지 읽기
# airplaneImgGray = cv2.resize(airplaneImgGray, (600,400))   # 색상 사이즈 조절(가로 600, 세로 400)

# airplaneImgUnChanged = cv2.imread('./res/img/airplane.jpg', cv2.IMREAD_UNCHANGED) # 이미지 읽기
# airplaneImgUnChanged = cv2.resize(airplaneImgUnChanged, (600,400))   # 색상 사이즈 조절(가로 600, 세로 400)

# cv2.imshow('airplaneImgColor', airplaneImgColor)
# cv2.imshow('airplaneImgGray', airplaneImgGray)
# cv2.imshow('airplaneImgUnChanged', airplaneImgUnChanged)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# airplaneImgUnChanged = cv2.imread('./res/img/airplane.jpg', cv2.IMREAD_GRAYSCALE) # 이미지 읽기
# airplaneImgUnChanged = cv2.resize(airplaneImgUnChanged, (600,400))   # 색상 사이즈 조절(가로 600, 세로 400)


# # 동영상 불러와서 출력하기
# openCv에서 동영상을 불러오는것은
# 동영상 → 프레임 추출 → 이미지화 → 출력
''''''
# take_offMov = cv2.VideoCapture('./res/mov/take_off.mp4')
# while take_offMov.isOpened(): # 동영상 파일이 열려있다면
#     result, frame = take_offMov.read()
#     if not result:
#         print('End Frame')
#         break
    
#     # 사이즈 조정
#     frame = cv2.resize(take_offMov, (600,400))

#     print(f'Frame: {frame}')
#     cv2.imshow('title-airplaneFrame', frame)

#     if cv2.waitKey(1) == ord('q'): # 1ms 동안 기다린다 사용자가 q를 입력하면 중단함
#         break

# take_offMov.release()     # 외부 자원 해제
# cv2.imshow('take_off', take_offMov)
''''''

# 캠에서 동양상 실시간으로 불러오기

take_offMov = cv2.VideoCapture(0)
while take_offMov.isOpened(): # 동영상 파일이 열려있다면
    result, frame = take_offMov.read()
    if not result:
        print('End Frame')
        break
    
    # 사이즈 조정
    frame = cv2.resize(take_offMov, (600,400))

    print(f'Frame: {frame}')
    cv2.imshow('title-airplaneFrame', frame)

    if cv2.waitKey(1) == ord('q'): # 1ms 동안 기다린다 사용자가 q를 입력하면 중단함
        break

take_offMov.release()     # 외부 자원 해제
cv2.imshow('take_off', take_offMov)


