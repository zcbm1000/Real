from flask import Flask, render_template, request
import urllib.request
import urllib.parse
import datetime
import json

app = Flask(__name__)

client_id = 'wIKTurHRqyCe1FodJ3fm'
client_secret = 'cg6uqa1Hsz'


# NAVER API 요청 함수
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header('X-Naver-Client-Id', client_id)
    req.add_header('X-Naver-Client-Secret', client_secret)

    try:
        response = urllib.request.urlopen(req)

        if response.getcode() == 200:
            print(f'[{datetime.datetime.now()}] Request Success')
            return response.read().decode('utf-8')

    except Exception as e:
        print(e)
        return None


# NAVER 뉴스 검색
def getNaverSearch(node, srcText, start, display):

    base = 'https://openapi.naver.com/v1/search'
    node = f'/{node}.json'

    parameters = f'?query={urllib.parse.quote(srcText)}&start={start}&display={display}'

    url = base + node + parameters

    responseDecode = getRequestUrl(url)

    if responseDecode is None:
        return None
    else:
        return json.loads(responseDecode)


# 뉴스 데이터 정리
def getPostData(post, jsonResult, cnt):

    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    pDate = datetime.datetime.strptime(
        post['pubDate'],
        '%a, %d %b %Y %H:%M:%S +0900'
    )

    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({
        'cnt': cnt,
        'title': title,
        'description': description,
        'org_link': org_link,
        'link': link,
        'pDate': pDate
    })


@app.route('/', methods=['GET', 'POST'])
def index():

    news_list = []

    if request.method == 'POST':

        srcText = request.form['keyword']

        node = 'news'
        cnt = 0
        jsonResult = []

        jsonResponse = getNaverSearch(node, srcText, 1, 10)

        while jsonResponse is not None and jsonResponse['display'] != 0:

            for post in jsonResponse['items']:

                cnt += 1
                getPostData(post, jsonResult, cnt)

            break

        # JSON 파일 저장
        with open(f'{srcText}_naver_news.json',
                  'w',
                  encoding='utf-8') as f:

            jsonFile = json.dumps(
                jsonResult,
                indent=4,
                ensure_ascii=False
            )

            f.write(jsonFile)

        news_list = jsonResult

    return render_template('index.html', news_list=news_list)


if __name__ == '__main__':
    app.run(debug=True)