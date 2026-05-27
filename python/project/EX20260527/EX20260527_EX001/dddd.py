import datetime
import json  
import urllib.parse
import urllib.request

client_id = "PC4EDXNa5QvtIhIBMJ53"
client_secret = "7NhctXVyRI"


def getRequestUrl(url):
    
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    return req


def getNaverSearch(node, srcText, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = f"/{node}.json"
    parameters = (
        f"?query={urllib.parse.quote(srcText)}&start={start}&display={display}"
    )
    url = base + node + parameters
    req = getRequestUrl(url)

    try:
        # ⚠️ urlopen은 모두 '소문자'입니다!
        response = urllib.request.urlopen(req)

        if response.getcode() == 200:
            print(f"[{datetime.datetime.now()}] URL REQUEST SUCCESS!!")

            # response.read() 뒤에 .decode('utf-8')을 붙여야 한글이 깨지지 않습니다.
            raw_data = response.read().decode("utf-8")

            # 파이썬 딕셔너리로 변환 후 보기 좋게 출력
            json_data = json.loads(raw_data)
            print("response data:", json.dumps(json_data, indent=4, ensure_ascii=False))

    except Exception as e:
        # 에러가 나면 pass하지 않고 왜 에러가 났는지 출력하도록 수정
        print(f"에러 발생: {e}")


def main():
    node = "news"  # 크롤링 하는 대상을 지정
    srcText = input("검색어 입력 : ")
    jsonResponse = getNaverSearch(node, srcText, 1, 10)  # 테스트용으로 10개만 출력


if __name__ == "__main__":
    main()
