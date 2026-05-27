


'''
처음 프로그램이 실행되면 다음과 같은 메뉴를 출력
메뉴: 1 회원가입   2. 로그인   3. 특정 회원 정보 출력   4. 모든 회원 정보 출력   0. 종료
'1. 회원가입'을 선택하면 회원 ID, PW ,Email, Phone 정보를 입력받아 가입을 진행함.
'2. 로그인'을 선택하면 ID, PW 를 입력바아 로그인 성공, 실패를 출력함 3회 실패시 프로그램 종료
'3. 특정 회원 정보 출력'을 선택하면 회원 ID,PW 를 입력받아 일치하는 회원 정보를 모두 출력
'4. 모든 회원 정보 출력'을 선택하면 가입되어 있는 모든 회원 정보를 출력한다.
'0. 종료'를 선택하면 프로그램을 종료시킨다.
'''

members = []
loginFail = 0
flag = True


def signIn_members():
    print('회원 가입창 입니다.')
    member_Id = input('Id를 입력하세요')
    member_Pw = input('Pw를 입력하세요')
    member_Email = input('Email를 입력하세요')
    member_Phone = input('Phone를 입력하세요')

    member = {
    'ID'   : member_Id,
    'PW'   : member_Pw,
    'Email': member_Email,
    'Phone': member_Phone
    }
    members.append(member)
    print('회원 가입이 완료되었습니다.')


def logIn():
    loginFail = 0
    print('로그인 창입니다.')
    member_Id = input('Id를 입력하세요')
    member_Pw = input('Pw를 입력하세요')
    for member in members:
        if member_Id == member['ID'] and member_Pw == member['PW']:
            print('로그인에 성공하였습니다')
            loginFail = 0
            return    
    loginFail += 1
    print(f'로그인 실패횟수: {loginFail} / 3')

    if loginFail >= 3:
        print('3회 로그인 실패로 프로그램을 종료합니다.')
        flag = False
 
def printMemberInfo():
    print('출력할 회원 정보를 입력하세요.')
    member_Id = input('ID를 입력하세요.')
    member_Pw = input('Pw를 입력하세요.')
    for member in members:
        if member_Id == member['ID'] and member_Pw == member['PW']:
            print('회원정보:', member)
            return
    print('일치하는 회원이 없습니다.')

def printAllInfo():
    print('등록된 모든 회원 정보를 출력합니다.')
    if not members:
        print('등록된 회원이 없습니다.')
    else:
        for member in members:
            print(member)    

def choiceMenu():
    return int(input('\n메뉴: 1. 회원가입  2. 로그인  3. 특정 회원 정보 출력  4. 모든 회원 정보 출력  0. 종료\n 선택: '))
while flag:
    select = choiceMenu()
    if select == 1:
        signIn_members()
    elif select == 2:
        logIn()
    elif select == 3:
        printMemberInfo()
    elif select == 4:
        printAllInfo()
    elif select == 0:
        print('프로그램을 종료합니다.')
        flag = False
    else:
        print('잘못된 입력입니다. 다시 선택하세요.')