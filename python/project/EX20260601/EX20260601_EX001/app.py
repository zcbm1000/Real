import config
from member import member_service
from bank import bank_service
from memo import memo_service

def main():
    flag = True
    while flag:
        menuNum = int(input('1.MEMBER    2.BANK    3.MEMO    4.TODO    99.SYSTEM-OUT'))
        if menuNum == config.MEMBER_SERVICE:
            # memberService = member_service.MemberService()
            # memberService.run()
            member_service.MemberService().run()
    
        elif menuNum == config.BANK_SERVICE:
            # bankService = bank_service.BankService()
            # bankService.run()
            bank_service.BankService().run()

        elif menuNum == config.MEMO_SERVICE:
            # menuService = menu_service.menuService()
            # menuService.run()
            memo_service.MemoService().run()
            
        elif menuNum == config.TODO_SERVICE:
            # todoService = todo_service.todoService()
            # todoService.run()
            pass

        elif menuNum == config.SYSTEM_OUT:
            flag = False

if __name__ == "__main__":
    main()

















