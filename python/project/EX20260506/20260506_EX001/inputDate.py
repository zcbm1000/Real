# 데이터 입력(input Data)
# input() 함수는 사용자로부터 입력을 받을 때 사용한다.


# print('데이터를 입력하세요.')
# inputData = input()
# print(inputData)



# print('정수를입력하세요')
# inputInteger = input()           # 55
# print(inputInteger)              # 55
# print(type(inputInteger))        # Int? No, STR



# print('실수를 입력하세요.')        
# inputFloat = input()            # 3.1415
# print(inputFloat)               # 3.1415
# print(type(inputFloat))         # Float? No, STR



# print('논리형데이터를 입력하세요.')        
# inputBoolean = input()            # True
# print(inputBoolean)               # True
# print(type(inputBoolean))         # Bool? No, STR



# inputBoolean = input('논리형데이터를 입력하세요.\n')
# print(inputBoolean)
# print(type(inputBoolean))



# print('논리형데이터를 입력하세요.', end='')
# inputBoolean = input()            # True
# print(inputBoolean)               # True
# print(type(inputBoolean))         # Bool? No, STR





# 자료형을 변환해야 합니다. (자료형변환, Data Type Casting)

# str을 in로 변환하는 예시

# userInputData = input('사용자야 정수를 입력해라~')     # 1번 데이터로 가정
# print(userInputData)                                # 1번 데이터를 출력
# print(type(userInputData))                          # 1번 데이터의 자료형을 출력함
# int(userInputData)                                  # 1번을 복사하여 다르곳에 정수형으로 변환하여 저장 2번으로 가정
# userInputData = int(userInputData)                  # 1번= 2번으로 가정을함
# print(type(userInputData))                          # 2번을 출력함



# # str을 bool로 변환하는 예시

# userInputData = input('True or False?')   # 1번데이터로 가정
# print(userInputData)                      # 1번 데이터를 출력
# print(type(userInputData))                # 1번 데이터의 자료형을 출력함
# bool(userInputData)                       # 1번을 복사하여 다르곳에 논리형으로 변환하여 저장 2번으로 가정
# userInputData = bool(userInputData)       # 1번= 2번으로 가정을함   
# print(type(userInputData))                # 2번을 출력함 


# str을 float로 변환하는 예시

# userInputData = input('실수를 입력하세요.')   # 1번데이터로 가정
# print(userInputData)                        # 1번 데이터를 출력
# print(type(userInputData))                  # 1번 데이터의 자료형을 출력함
# float(userInputData)                        # 1번을 복사하여 다르곳에 실수형으로 변환하여 저장 2번으로 가정
# userInputData = float(userInputData)        # 1번= 2번으로 가정을함   
# print(type(userInputData))                  # 2번을 출력함

# userInputData = 'True'
# userInputData = bool(userInputData)
# print(type(userInputData))

x = 3.141592
y = int(x)
print(y)
print(float(y))


