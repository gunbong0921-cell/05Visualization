# 판다스 모듈 임포트
import pandas as pd
# 웹페이지의 정보를 얻어오기 위해 requests 모듈 임포트
import requests

# JSON 파일의 내용을 데이터프레임으로 변환
df1 = pd.read_json('../resData/sample.json')
print(df1)

print("="*30) 

# 인덱스만 출력
print(df1.index)
# 라벨형 인덱스를 통해 요소에 접근
print("마지막데이터:", df1.loc['Paul', 'c++'])
print("첫번째컬럼:")
# 컬럼 출력시에는 데이터프레임의 이름을 사용
print( df1['algol'])
print("첫번째행")
# 행을 출력할때는 loc(혹은 iloc) 함수 사용
print(df1.loc['Jerry'])

print("="*30)

# Fake API 사이트를 지정해서 페이지의 정보를 얻어온다.
url = 'https://jsonplaceholder.typicode.com/users'
# 웹에 접속해야 하므로 requests 모듈 사용
response = requests.get(url)
# 응답코드가 200이면 정상 접속된 상태로 접속
if response.status_code==200:
  # JSON 데잍를 얻어온 후 데이터프레임으로 변환
  # jsonData = response.text
  # df2 = pd.read_json(jsonData)
  jsonData = response.json()
  df2 = pd.DataFrame(jsonData)
  df2.set_index('id', inplace=True)
  # id컬럼을 인덱스로 지정한 후 원본에 저장
  print(df2)
else:
    print("API 연동 중 오류발생")
    print(response.status_code)