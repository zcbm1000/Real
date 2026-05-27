
# from config_dir import config
# from member_dir import session

flag = True

while flag:

    if session.signInedMemberId == '':
        # sign out상태
        print('sign_out 상태')
        menuNum = int(input('1. sign_up  2. sign_in  0. end'))
        
    else:
        # sign in 상태
        print('sign_in  상태')
        menuNum = int(input('3. modify  4. delete  5. sign_out  0. end'))


    if menuNum == config.SIGN_UP:
        print('1. sign_up')
        
    elif menuNum == config.SIGN_IN:
        print('2. sign_in')   

    elif menuNum == config.MEMBER_MODIFY:
        print('3. modify')

    elif menuNum == config.MEMBER_DELETE:
        print('4. delete')

    elif menuNum == config.SIGN_OUT:
        print('5. sign_out') 

    elif menuNum == config.SYSTEM_OUT:
        print('0. end')
        flag = False








