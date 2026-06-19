import requests, json

url = 'https://openapi.gg.go.kr/GGEXPSDLV'

# pSize를 10으로 설정하여 딱 10개만 요청함.
params = dict(Type='json', pSize=10, pIndex=1, 
                                    key='0b7c671729a44ed49d789a7fb9393beb')

raw_data = requests.get(url=url, params=params)
binary_data = raw_data.content  
json_data = json.loads(binary_data)

# JSON 결과 구조에서 실제 데이터가 담긴 'row' 부분만 추출.
try:
    data_list = json_data['GGEXPSDLV'][1]['row']
    
    # 10개의 데이터를 하나씩 반복하며 출력.
    for index, row in enumerate(data_list, start=1):
        print(f"[{index}] {row}")
        
except (KeyError, IndexError):
    # API 오류가 나거나 데이터가 없을 때를 대비한 예외 처리.
    print("데이터를 가져오는 데 실패했거나 응답 구조가 올바르지 않습니다.")
    print(json_data)

print("종료")