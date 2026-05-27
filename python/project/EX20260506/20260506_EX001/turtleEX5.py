import turtle

t = turtle.Turtle()        # 그림 그리기 준비 완료
t.shape('turtle')          # 아이콘 설정 (거북이 모양)

angle = int(input("회전할 각도를 입력하세요: "))
length = int(input("선의 길이를 입력하세요: "))

t.goto(-100, 100)            # 시작위치로 이동 (x,y), 좌표는 (0,0)에서 시작

t.right(angle)                # 우측으로 지정각도만큼 회전
t.forward(length)             # 직진으로 지정거리만큼 이동

t.left(angle)                 # 좌측으로 지정각도만큼 회전
t.forward(length)             # 직진으로 지정거리만큼 이동

t.left(angle)                 # 좌측으로 지정각도만큼 회전
t.forward(length)             # 직진으로 지정거리만큼 이동

t.left(angle)                 # 좌측으로 지정각도만큼 회전
t.forward(length)             # 직진으로 지정거리만큼 이동

t.left(angle)                 # 좌측으로 지정각도만큼 회전
t.forward(length)             # 직진으로 지정거리만큼 이동

