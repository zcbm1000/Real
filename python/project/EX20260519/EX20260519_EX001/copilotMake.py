members = []
login_fail = 0
running = True


def sign_up():
    print('\n[회원 가입]')
    member = {
        'ID': input('ID: '),
        'PW': input('PW: '),
        'Email': input('Email: '),
        'Phone': input('Phone: ')
    }
    members.append(member)
    print('✅ 회원 가입 완료')


def login():
    global login_fail, running
    print('\n[로그인]')
    member_id = input('ID: ')
    member_pw = input('PW: ')
    for member in members:
        if member_id == member['ID'] and member_pw == member['PW']:
            print('✅ 로그인 성공')
            login_fail = 0
            return
    login_fail += 1
    print(f'❌ 로그인 실패 ({login_fail}/3)')
    if login_fail >= 3:
        print('3회 실패로 프로그램을 종료합니다.')
        running = False


def print_member_info():
    print('\n[특정 회원 정보 출력]')
    member_id = input('ID: ')
    member_pw = input('PW: ')
    for member in members:
        if member_id == member['ID'] and member_pw == member['PW']:
            print('회원 정보:')
            for key, value in member.items():
                print(f' - {key}: {value}')
            return
    print('❌ 일치하는 회원이 없습니다.')


def print_all_info():
    print('\n[모든 회원 정보 출력]')
    if not members:
        print('등록된 회원이 없습니다.')
    else:
        for idx, member in enumerate(members, start=1):
            print(f'회원 {idx}:')
            for key, value in member.items():
                print(f' - {key}: {value}')


def choice_menu():
    print("\n메뉴:")
    print(" 1. 회원가입")
    print(" 2. 로그인")
    print(" 3. 특정 회원 정보 출력")
    print(" 4. 모든 회원 정보 출력")
    print(" 0. 종료")
    select = input("선택: ")
    if select.isdigit():   # 숫자인지 확인
        return int(select)
    else:
        return -1


def exit_program():
    global running
    print("프로그램을 종료합니다.")
    running = False


menu_actions = {
    1: sign_up,
    2: login,
    3: print_member_info,
    4: print_all_info,
    0: exit_program
}


while running:
    choice = choice_menu()
    action = menu_actions.get(choice)
    if action:
        action()
    else:
        print("❌ 잘못된 입력입니다. 다시 선택하세요.")
