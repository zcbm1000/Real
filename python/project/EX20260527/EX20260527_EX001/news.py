import urllib.request
import datetime
import json

client_id = 'wIKTurHRqyCe1FodJ3fm'
client_secret = 'cg6uqa1Hsz'

# NAVER에서 데이터 가져오는 함수
def getRequestUrl(url): 
    req = urllib.request.Request(url)
    req.add_header ('X-naver-Client-Id', client_id)
    req.add_header ('X-naver-Client-secret', client_secret)
   
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print(f'[{datetime.datetime.now()}] URL REQUEST SUCCESS')
            # print(f'resoponse data: {response.read().decode('utf-8')}')    # decode 란 바이트 코드를 문자열로 변환하는 것 인코딩과 반댓말
                                                                             # encode 란 문자열을 바이트 코드로 변환하는 것 디코딩과 반댓말
            return response.read().decode('utf-8')
                                                                       
    except Exception as e:
        print(f'[{datetime.datetime.now()}] Error: {e}')
        return None
    
# NAVER에서 데이터 검색하는 함수
def getNaverSearch(node, srcText, start, display):
    base = 'https://openapi.naver.com/v1/search'
    node = f'/{node}.json'    # news.json
    parameters = f'?query={urllib.parse.quote(srcText)}&start={start}&display={display}'
    
    url = base + node + parameters
    respnseDecode = getRequestUrl(url)

    if respnseDecode == None:
        return None
    else:
        return json.loads(respnseDecode)
    
def getPostData(post, jsonResult, cnt):
    title =  post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']
    pDate = datetime.datetime.strptime(post['pubDate'],  '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')
 
    jsonResult.append({
        'cnt': cnt,
        'title': title,
        'description': description,
        'org_link': org_link,
        'link': link,
        'pDate': pDate
    })

def main():           
    node = 'news'                                                           # 크롤링 대상 지정
    srcText = input('검색어를 입력해 주세요.')                    
    cnt = 0
    jsonResult = []                                                         # json 이란 데이터 교환 형식 (프로그램기리 데이터를 주고 받기 쉽게 만든 텍스트 형식)
    
    jsonResponse = getNaverSearch(node, srcText, 1, 100)
    # print(f'jsonrespones: {jsonResponse}')
    # print(f'jsonrespones total: {jsonResponse['total']}')
    # print(f'jsonrespones items 0 : {jsonResponse['items'][0]}')
    # print(f'jsonrespones items 0 title: {jsonResponse['items'][0]['title']}')
    # print(f'jsonrespones items 0 description: {jsonResponse['items'][0]['description']}')

    while jsonResponse != None and jsonResponse['display'] != 0:
          for post in jsonResponse['items']:
              cnt += 1
              getPostData(post, jsonResult, cnt)

          jsonResponse = getNaverSearch(node, srcText, jsonResponse['start'] + jsonResponse['display'], 100)
    
    # 파일로 저장(날씨_naver_news.json)
    with open(f'{srcText}_naver_{node}.json', 'w', encoding='utf8') as f:
        jsonfile = json.dump(jsonResult, indent=4, sort_keys=True, ensure_ascii=False )
        f.write(jsonfile)

if __name__ == '__main__':
    main()