from db_dir import member_DB 
from db_dir import diary_db
ids    = ['gildong', 'chanho']
pws    = ['1234', '0000']
mails  = ['gildong@gmail.com', 'chanho@naver.com']
phones = ['010-1111-1111', '010-2222-2222']


def memberDummyInit():
    for n in range(len(ids)):
        member_DB.memberDB[ids[n]] = {
            'uId'   : ids[n],
            'uPw'   : pws[n],
            'uMail' : mails[n],
            'uPhone': phones[n]
        }       

        diary_db.diaryDB[ids[n]] = []
