# 웹페이지의 정보를 수집해야 하므로 requests 모듈 임포트
import requests, json

'''
경기 데이터 드림(https://data.gg.go.kr)에서 제공하는 Open API 중
'전문 및 대학교 현황'을 연동
'''
# API 요청url
url = 'https://openapi.gg.go.kr/Jnclluniv?'
# 요청시 필요한 파라미터. 딕셔너리를 통해 Key와 Value로 구분해서 작성.
params = dict(Type='json', pSize='20',
              KEY='37036b829e80435b9bd513cb9d7cdfd3')
# OpenAPI의 요청 URL과 파라미터를 이용해서 데이터 요청
raw_data = requests.get(url=url, params=params)
# 얻어온 Raw(로우)데이터를 JSON으로 변환
binary_data = raw_data.content
# 변환 완료된 JSON 데이터를 로드한다.
json_data = json.loads(binary_data)
print(json_data)

'''
JSON 데이터를 정렬한 후 노드를 분석하고 key를 찾았다면 아래와 같이
반복문을 통해 필요한 값을 파싱할 수 있다.
객체() 인 경우 key로 접근하고, 배열[] 인 경우 인덱스로 접근하면된다.
'''
for jd in json_data['Jnclluniv'][1]['row']:
  SIGUN_NM = jd['SIGUN_NM'] # 시군명
  FACLT_NM = jd['FACLT_NM'] # 대학명
  REFINE_LOTNO_ADDR = jd['REFINE_LOTNO_ADDR'] # 주소
  REFINE_WGS84_LAT = jd['REFINE_WGS84_LAT'] # 위도
  REFINE_WGS84_LOGT = jd['REFINE_WGS84_LOGT'] # 경도
  print(FACLT_NM, REFINE_WGS84_LAT, REFINE_WGS84_LOGT)
  