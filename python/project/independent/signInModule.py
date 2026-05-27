
def signIn(users):
    while True:
        print('로그인을 위해 ID 와 PW를 입력하세요.')
        inputId = input('ID를 입력하세요.\nID: ')
        
        for user in users:
            if user['ID'] == inputId:
                signInFail = 0
                while signInFail < 3:
                    inputPW = input('PW를 입력하세요.\nPW: ')
                    if inputPW == user['PW']:
                        print(f'로그인에 성공하였습니다.\n{user["ID"]}님 환영합니다.')
                        return True
                    else:
                        signInFail += 1
                        print(f'로그인 실패: 올바르지 않은 PW 입니다.\n남은 시도 횟수 {3 - signInFail}회')
                print('PW 입력 3회 실패로 로그인 기능을 종료합니다.')
                return False
        
        print('올바르지 않은 ID 입니다.\nID를 다시 확인 후 입력하세요.')



# ---------------------------------------------------------------------- #
'''
    elif userSelectedMunuNum == SIGN_IN:            # 2.로그인 
        signInCount = 1
        while True:
            uId = input('Input member ID: ')
            uPw = input('Input member PW: ')

            if uId in members:
                uInfo = members[uId]
                if uInfo['uPw'] == uPw:
                    print('SIGN-IN SUCCESS!!')
                else:
                    print('SIGN-IN FAIL!!')
                    signInCount += 1
                    if signInCount > 3:
                        print('3회 이상 틀렸어요!!')
                        break
            else:
                print('존재 하지 않은 ID입니다. 다시 확인하세요.')
'''





