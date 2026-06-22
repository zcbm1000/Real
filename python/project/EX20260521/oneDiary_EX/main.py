from config_dir import config
from member_dir import session
from db_dir     import member_DB
from db_dir     import diary_db
from member_dir import dummy
import copy

if config.DEV_MOD:
    dummy.memberDummyInit()
    print(f'memberDB: {member_DB.memberDB}')
    print(f'diaryDb: {diary_db.diaryDB}')

flag = True

while flag:

    menuNum = ''
    if session.signInedMemberId == '':
        # sign out상태
        menuNum = int(input('1. sign_up  2. sign_in  6. write  7. read  0. end\n 선택:'))
    else:
        # sign in 상태
        menuNum = int(input('3. modify  4. delete  5. sign_out  6. write  7. read  0. end\n 선택:'))

    if menuNum == config.SIGN_UP:
        print('1. sign_up')
        uId    = input('please input new member id \nid:')
        uPw    = input('please input new member pw \npw:')
        uMail  = input('please input new member mail \nmail:')
        uPhone = input('please input new member phone \n phone:')
        
        member_DB.memberDB[uId] = {
            'uId': uId,
            'uPw': uPw,
            'uMail': uMail,
            'uPhone': uPhone
        }

        print('New Member Sign_Up Success!!')

        if config.DEV_MOD:
            print(f'memberDB: {member_DB.memberDB}')
        
        diary_db.diaryDB[uId] = []
        if config.DEV_MOD:
            print(f'diaryDB: {diary_db.diaryDB}')

        print(f'memberDB: {member_DB.memberDB}')
        print(f'diaryDB: { diary_db.diaryDB}')

    elif menuNum == config.SIGN_IN:
        print('2. sign_in')   
        uId    = input('please input member\nid:')
        uPw    = input('please input member\npw:')
        
        if uId in member_DB.memberDB:
            if member_DB.memberDB[uId]['uPw'] == uPw:
                print('Sign_In Success!!')
                session.signInedMemberId = uId

            else:
                print('Sign_In Failed\n pw error')    
        else:
            print('Sign_In Failed\n id error')    

    elif menuNum == config.MEMBER_MODIFY:
        print('3. modify')
        '''
        id, pw, mail, phone 중에서 어떤 정보를 수정하게 가능할지 정해야함.
        id     수정 불가  이미 탈퇴한 회원의 id 라도 변경 사용 불가
        pw     수정 가능  복잡하게 수정이 가능
        email  수정 가능  단순하게 수정이 가능
        phone  수정 가능  단순하게 수정이 가능
        '''
        uPw    = input('please input member pw')
        uMail  = input('please input member mail')
        uPhone = input('please input member phone')

        '''
        member_DB 모듈에 있는 memberDB 딕셔너리에서 회원정보를 변경한다.
        그러나 memberDB 딕셔너리 내에는 'gildong', 'chanho' 회원 등이 있음
        현재 로그인 되어있는 회원 정보를 불러와 그 정보를 수정한다.
        로그인 되어있는 회원은 session.signInedMemberId 에 있음 
        아이디를 가져와 사용하면 된다.
        '''
        currentSignInedMemberID = session.signInedMemberId   
        memberInfo = member_DB.memberDB[currentSignInedMemberID]
       
        if config.DEV_MOD: print(f'memberInfo: {memberInfo}')
        memberInfo['uPw'] = uPw 
        memberInfo['uMail'] = uMail
        memberInfo['uPhone'] = uPhone

    elif menuNum == config.MEMBER_DELETE:
        print('4. delete')
        '''
        현재 로그인 되어있는 회원의 ID를 session.signInedMemberId 에서 불러와서
        해당 회원의 정보를 member_DB.memberDB 에서 삭제한다.
        '''
        currentSignInedMemberID = session.signInedMemberId
        del member_DB.memberDB[currentSignInedMemberID]

        print('Member info deleted!!')  
        session.signInedMemberId = ''    
        if config.DEV_MOD: print(f'member_DB.memberDB: {member_DB.memberDB}')

    elif menuNum == config.SIGN_OUT:
        print('5. sign_out')
        session.signInedMemberId = ''
        print('Sign_Out Success!!') 


    elif menuNum == config.DIARY_WRITE:
        print('6. write')

        if session.signInedMemberId == '':
            print('Sorry! Please Sign_In!!')

        else:    
            while True:
                diaryTxt = input('일기를 작성하세요.(10자 이내) \n 내용:')
                if len(diaryTxt) > 10:
                    print(f'10자를 초과하였습니다.({len(diaryTxt)})')      
                else:
                    diary_db.diaryDB[session.signInedMemberId].append(diaryTxt)      
                    if config.DEV_MOD: print(f'diary_db.diaryDB: {diary_db.diaryDB}')
                    break


    elif menuNum == config.DIARY_READ:
        print('7. read')
                
        if session.signInedMemberId == '':
            print('Sorry! Please sign-in!!')
        else:
            currentSignInedMemberID = session.signInedMemberId
            myDiaries = diary_db.diaryDB[currentSignInedMemberID]

            deepCopyedDiaries = copy.deepcopy(myDiaries)
            deepCopyedDiaries.reverse()     # 순서 바뀐다.
            for idx, diaryTxt in enumerate(deepCopyedDiaries):
                print(f'({idx+1}): {diaryTxt}')


    elif menuNum == config.SYSTEM_OUT:
        print('0. end')
        flag = False








