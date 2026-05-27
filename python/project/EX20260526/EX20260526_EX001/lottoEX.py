# Quiz 로또 당첨게임

'''
1부터 45까지의 정수6개를 입력하고 컴퓨터에서는 1부터 45까지의 난수를 발생시킨다
사용자가 입력한 정수와 컴퓨타 정수를 비교하여 일치하는지 확인하는 프로그램
'''


import random

userNums = []
randNums = []
collect  = [] 

def setUNumbers(ns):                                 # setter 리스트에 어떠한 데이터를 세팅하는 함수   |   set + 변수명
    global userNums
    userNums = ns
    

def getUNumbers():                                   # getter 리스트에 저장한 데이터를 가져오는 함수   |   get + 변수명 
    return userNums


def setRNumbers():
    global randNums
    randNums = random.sample(range(1,46), 6)         # 1부터 46미만의 숫자중 6개의 난수를 발생시켜 randNums에 할당함


def getRNumbers():
    return randNums


def compareNumbers():
    global userNums
    global randNums
    global collect

    collect = []
    for item in userNums:
        if randNums.count(item) != 0:
            collect.append(item)

    return collect



























