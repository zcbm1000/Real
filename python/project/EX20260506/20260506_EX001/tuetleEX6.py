import turtle

t = turtle.Turtle()        # 그림 그리기 준비 완료
t.shape('turtle')          # 아이콘 설정 (거북이 모양)
t.pencolor('red')          # 펜 색상 설정

angle = int(input("회전할 각도를 입력하세요: "))
length = int(input("선의 길이를 입력하세요: "))

t.penup()                    # 펜을 들어올려서 이동시 선이 그려지지않도록 함
t.goto(-100, 100)            # 시작위치로 이동 (x,y), 좌표는 (0,0)에서 시작
t.pendown()                  # 펜을 내려서 이동시 선이 그려지도록 함

t.pencolor('blue')  
t.right(angle)                # 우측으로 지정각도만큼 회전
t.forward(length)             # 직진으로 지정거리만큼 이동

t.pencolor('green')  
t.left(angle)                 # 좌측으로 지정각도만큼 회전
t.forward(length)             # 직진으로 지정거리만큼 이동

t.pencolor('black')  
t.left(angle)                 # 좌측으로 지정각도만큼 회전
t.forward(length)             # 직진으로 지정거리만큼 이동

t.pencolor('purple')  
t.left(angle)                 # 좌측으로 지정각도만큼 회전
t.forward(length)             # 직진으로 지정거리만큼 이동

t.pencolor('orange')  
t.left(angle)                 # 좌측으로 지정각도만큼 회전
t.forward(length)             # 직진으로 지정거리만큼 이동

t.pencolor('red')  
t.left(angle)                 # 좌측으로 지정각도만큼 회전
t.forward(length)             # 직진으로 지정거리만큼 이동

