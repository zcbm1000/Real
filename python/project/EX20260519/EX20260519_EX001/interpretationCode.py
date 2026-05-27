
members = []
# members를 리스트로 지정함 (지정하기 전이기에 현재는 비어있음)

loginFail = 0
# loginFail 을 0으로 할당함(로그인 실패시 사용할거기에 현재횟수는 0 실패시 추가1개씩 올리면됨)

flag = True
# flag 에 True를 할당함(나중에 while 문에서 false로 바꿀수도 있음)


def signIn_members():
# 회원가입 기능을 아래와 같이 지정함

    print('회원 가입창 입니다.')
#  '회원 가입창 입니다.' 를 출력해서 보여줌

    member_Id = input('Id를 입력하세요')
#   member_Id 는 사용자가 직접 입력하도록함

    member_Pw = input('Pw를 입력하세요')
#   member_Pw 는 사용자가 직접 입력하도록함

    member_Email = input('Email를 입력하세요')
#   member_Email 는 사용자가 직접 입력하도록함

    member_Phone = input('Phone를 입력하세요')
#   member_Phone 는 사용자가 직접 입력하도록함

    member = {
    'ID'   : member_Id,
    'PW'   : member_Pw,
    'Email': member_Email,
    'Phone': member_Phone
    }
#   member 라는 딕셔너리를 지정하고 딕셔너리 내부로 입력했던 내용들을 할당함.

    members.append(member)
#   members 끝에 지정한member 딕셔너리를 추가함

    print('회원 가입이 완료되었습니다.')
#    '회원 가입이 완료되었습니다.' 를 출력함


def logIn():
# login 기능을 아래와 같이 지정함

    global loginFail, flag
#   global 코드를 이용 (전역변수를 활용할거기때문에)

    print('로그인 창입니다.')
#   '로그인 창입니다.' 를 출력함
    
    member_Id = input('Id를 입력하세요')
#   member_Id 는 사용자가 직접 입력하도록함
     
    member_Pw = input('Pw를 입력하세요')
#   member_Pw 는 사용자가 직접 입력하도록함

    for member in members:
#   for문을 이용하여 members 리스트에 들어 있는 회원 딕셔너리를 하나씩 꺼내서 member 변수에 담는다.

        if member_Id == member['ID'] and member_Pw == member['PW']:
#       만약 membeb_Id 가 member의 딕셔너리안에있는 'ID' 값과 같은지 비교 and member_Pw 가 member 딕셔너리 안에있는 'Pw'값과 같은지 비교
          
            print('로그인에 성공하였습니다')
#           만약 같다면, '로그인에 성공하였습니다. 를 출력함

            loginFail = 0
#           만약 같다면, loginFail 의 변수를 0으로 초기화함.           

            return
#           만약 같다면, logIn() 를 종료 한 후 메뉴창으로 돌려놓음 
 
            
    loginFail += 1
#   로그인 실패시 loginFail 의 횟수를1회 추가함

    print(f'로그인 실패횟수: {loginFail} / 3')
#   로그인 실패횟수: 시도횟수 / 3 를 출력함. 

    if loginFail >= 3:
#   만약 로그인 실패횟수가 3회 이상이라면
        
        print('3회 로그인 실패로 프로그램을 종료합니다.')
#       '3회 로그인 실패로 프로그램을 종료합니다.' 를 출력
        
        flag = False
#       flag 를 false 로돌림 (그러면 while 문에서 false 가되기에 메뉴 출력이 없이 프로그램이 종료됨)

def printMemberInfo():
# printMemberInfo 의 기능을 아래와 같이 지정함
     
    print('출력할 회원 정보를 입력하세요.')
#   '출력할 회원 정보를 입력하세요' 를 출력함    

    member_Id = input('ID를 입력하세요.')
#   member_Id 는 사용자가 직접 입력하도록함  
  
    member_Pw = input('Pw를 입력하세요.')
#   member_Pw 는 사용자가 직접 입력하도록함
    
    for member in members:
#   for문을 이용하여 members 리스트에 들어 있는 회원 딕셔너리를 하나씩 꺼내서 member 변수에 담는다.
        
        if member_Id == member['ID'] and member_Pw == member['PW']:
#       만약 membeb_Id 가 member의 딕셔너리안에있는 'ID' 값과 같은지 비교 and member_Pw 가 member 딕셔너리 안에있는 'Pw'값과 같은지 비교
                      
            print('회원정보:', member)
#           만약 같다면, '회원정보: member에 담아놓은 딕셔너리를 출력함

            return
#           만약 같다면, printMemberInfo() 를 종료한 후 메뉴창으로 돌려놓음
        
    print('일치하는 회원이 없습니다.')
#   만약 if 가 아니라면 '일치하는 회원이 없습니다.'를 출력함     

def printAllInfo():
# printAllInfo 의 기능을 아래와 같이 지정함
    
    print('등록된 모든 회원 정보를 출력합니다.')
#   '등록된 모든 회원 정보를 출력합니다.' 를 출력함
    
    if not members:
#   만약 member 가 비어있다면('members 가 아니라면' 이라고 해석하기보다 파이썬에서는 이게맞을것같음)
      
        print('등록된 회원이 없습니다.')
        # members 가 비어있다면'등록된 회원이 없습니다.' 를 출력함(members 는 딕셔너리이기때문에)

    else:
#   그렇지 않다면 
    
        for member in members:
#       for문을 이용하여 members 리스트에 들어 있는 회원 딕셔너리를 하나씩 꺼내서 member 변수에 담는다.

            print(member)
#           member: 'member 에 담아놓은 딕셔너리' 를 출력한다.                

def choiceMenu():
# coiceMenu 의 기능을 아래와 같이 지정함 
    
    return int(input('\n메뉴: 1. 회원가입  2. 로그인  3. 특정 회원 정보 출력  4. 모든 회원 정보 출력  0. 종료\n 선택: '))
#   사용자가 메뉴를 보고 입력한 '문자열'을 '정수형'으로 변환하여 반환함

while flag:
# 조건이 falg 인동안 실행을 함(8열에 flag = True 로 지정을 해놨기에 사실상 while True 상태)  

    select = choiceMenu()
# select 에 142열에 입력한 정수형 숫자가 할당이됨 
    
    if select == 1:
#   만약 select 가 1과 같다면
        
        signIn_members()
#       12열에 지정한 함수 기능을 실행한다.
        
    elif select == 2:
#   그렇지 않고  select 가 2와 같다면
   
        logIn()
#       45열에 지정한 함수 기능을 실행한다.

    elif select == 3:
#   그렇지 않고  select 가 3과 같다면
        
        printMemberInfo()
#       91열에 지정한 함수 기능을 실행한다.

    elif select == 4:
#   그렇지 않고  select 가 4와 같다면
        
        printAllInfo()
#       118열에 지정한 함수 기능을 실행한다.

    elif select == 0:
#   그렇지 않고  select 가 0과 같다면  
      
        print('프로그램을 종료합니다.')
#       '프로그램을 종료합니다.' 를 출력한다.

        flag = False
#       8열에 지정한 flag를 False 로 바꾼다.
       
    else:
#   위에 해당사항이 없다면
    
        print('잘못된 입력입니다. 다시 선택하세요.')
#       '잘못된 입력입니다. 다시 선택하세요.' 를 출력한다.
