import lottoEX as lm                                # lottoEX 라는 모듈을 lm으로 부르기로함

nums = [] 

print('1부터 45까지의 정수 6개를 입력')
nums.append(int(input('1 번째 숫자 입력:')))          # 사용자로부터 1번째 번호를 입력 받아 nums에 추가를함.
nums.append(int(input('2 번째 숫자 입력:')))          # 사용자로부터 2번째 번호를 입력 받아 nums에 추가를함.
nums.append(int(input('3 번째 숫자 입력:')))          # 사용자로부터 3번째 번호를 입력 받아 nums에 추가를함.
nums.append(int(input('4 번째 숫자 입력:')))          # 사용자로부터 4번째 번호를 입력 받아 nums에 추가를함.
nums.append(int(input('5 번째 숫자 입력:')))          # 사용자로부터 5번째 번호를 입력 받아 nums에 추가를함.
nums.append(int(input('6 번째 숫자 입력:')))          # 사용자로부터 6번째 번호를 입력 받아 nums에 추가를함.


lm.setUNumbers(nums)                                # 사용자가 선택한 번호 6개
lm.setRNumbers()                                    # 컴퓨터가 선택한 번호 6개

print(f'이번주 로또 번호: {lm.getRNumbers()}')        # 

print(f'내가 선택한 로또번호: {lm.getUNumbers()}')

print(f'일치하는 번호: {lm.compareNumbers()}')
















