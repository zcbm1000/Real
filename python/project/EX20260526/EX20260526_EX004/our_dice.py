
import random


class Dice:
    def __init__(self):                             #
        self.numbers = []                           # 굴려진 주사위를 담는 리스트

    def playDice(self):                             # 주사위를 굴리는 기능
        self.numbers.append(random.randint(1,6))    # 

    def getNumbers(self):
        return self.numbers
    
    def getSum(self):
        return sum(self.numbers)
    
    













