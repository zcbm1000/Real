from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello Flask - TK</h1>"

# http://192.168.1.186:5000/hello
@app.route('/hello')
def hello():
    return "Hello Student!!"

# http://192.168.1.186:5000/me
@app.route('/me')
# 함수 이름은 상관없다 . 어차피 실행되기 때문에
def me():
    return '나는 flask 개발자 입니다.'

# http://192.168.1.186:5000/about
@app.route('/about')
def about():
    return '소개 페이지'

# http://192.168.1.186:5000/users/1
# 동적 URL 처리(Path Parameter)
# int       정수
# string    문자열
# float     실수
# path      전체 경로
@app.route('/users/<int:user_id>')
def get_user(user_id):
    print(f'user_id: {user_id}')    # 1
    return f'{user_id} 사용자 조회' 

# string
# http://192.168.1.186:5000/users/gildong
@app.route('/users/<string:name>')
def get_name(name):
    return f'{name}님 요청'

# float
# http://192.168.1.186:5000/pi/3.14
@app.route('/pi/<float:pi>')
def get_pi(pi):
    return f'pi:{pi}'

# path      전체 경로(중간에 /가 있어도 문자열 끝까지 모두 받는다.)
# http://192.168.1.186:5000/files/images/cat.jpg
@app.route('/files/<path:filepath>')        # filepath = images/cat.jpg
def files(filepath):
    return f'filepath: {filepath}'          # filepath: images/cat.jpg

# GET
# 1. 경로 변수(path variavble)
## http://192.168.1.186:5000/search/7
# @app.route('/search/<int:No>', methods = ['GET'])
# def search(No):
#     return f'{No} 사용자'

# 2. 쿼리 스트링(query string)
# http://192.168.1.186:5000/search?uNo=7
@app.route('/search')
def search():
    uNo = request.args.get('uNo')
    return f'{uNo} 사용자'

# request
# http://192.168.1.186:5000/search?keyword=weather&age=20      >> 쿼리 스트링(query string)
@app.route('/search')
def searchkey():
    keyword = request.args.get('keyword')
    age = request.args.get('age')
    return f'keyword: {keyword}, age: {age}'

# POST
# http://192.168.1.186:5000/login_form
@app.route('/login_form', methods = ['GET'])
def login_form():
    str = ''
    str += '<form action="/login" method="post">'
    str += '    <input type="text" name="u_id" placeholder="ID를 입력하세요."> '
    str += '<br>'
    str += '    <input type="password" name="u_pw" placeholder=PW를 입력하세요."> '
    str += '<br>'
    str += '    <input type="submit" value="SIGNUP">'
    str += '</form>'

    return str

@app.route('/login', methods=["POST"])
def login_confrim():
    u_id = request.form.get('u_id')
    u_pw = request.form.get('u_pw')

    if u_id == 'gildong' and u_pw == '1234':
        return f'{u_id}님 로그인 성공'
    else:
        return f'{u_id}님 로그인 실패'


if __name__ == '__main__':
    # host 누구나 들어올 수 있게
    app.run(debug=True, host='0.0.0.0')