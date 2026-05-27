# Quiz) 주사위 합을 합산하여 가장 높은 사람이 이기는 프로그램
'''
3명이 주사위를 5번씩 굴려서 나온 합 을 구하는 프로그램
합이 가장 큰 사람이 게임의 승자가됨
class를 이용하여 만들것
'''

'''
from our_dice import Dice

def sortNumbers(*numbers):
    list = sorted(numbers)
    list.sort(reverse= True)
    return list

gamer1Dice = Dice() 
gamer2Dice = Dice() 
gamer3Dice = Dice() 


for i in range(5):
    gamer1Dice.playDice()
    gamer2Dice.playDice()
    gamer3Dice.playDice()

    print(f'gamer1: {gamer1Dice.getNumbers()}')
    print(f'gamer2: {gamer2Dice.getNumbers()}')
    print(f'gamer3: {gamer3Dice.getNumbers()}')

print(f'sum of gamer1: {gamer1Dice.getSum()}')
print(f'sum of gamer2: {gamer2Dice.getSum()}')
print(f'sum of gamer3: {gamer3Dice.getSum()}')

sortedNumbers = sortNumbers(gamer1Dice.getSum(),
            gamer2Dice.getSum(),
            gamer3Dice.getSum())


print(f'1등: {sortedNumbers[0]}')
print(f'2등: {sortedNumbers[1]}')
print(f'3등: {sortedNumbers[2]}')



for idx, item in enumerate(sortedNumbers):
    if idx == 0:
        print(f'{idx + 1}등: {item}')
    else:
        print(f'{idx + 1}등: {item}')    
'''










