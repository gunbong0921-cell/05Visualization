import oracledb
import requests
import json

# Oracle DB 연결 설정
host_name = 'localhost'
oracle_port = 1521
service_name = 'xe'

conn = oracledb.connect(
    user='education',
    password='1234', 
    host=host_name,
    port=oracle_port,
    service_name=service_name
)
cursor = conn.cursor()

# API 요청 설정 (pSize=100으로 100개만 요청)
url = 'https://openapi.gg.go.kr/GGEXPSDLV'
params = dict(Type='json', pSize=100, pIndex=1, KEY='0b7c671729a44ed49d789a7fb9393beb')

raw_data = requests.get(url=url, params=params)
binary_data = raw_data.content  
json_data = json.loads(binary_data)

# SQL 쿼리문 수정 (VALEUS 오타 수정 및 :bizno 추가)
sql = '''INSERT INTO delrverStore (STORE_SEQ, SIGUN, BIZNM, BIZNO, ADDR, LATITUDE, LONGITUDE)
         VALUES (seq_board_num.NEXTVAL, :sigun, :biznm, :bizno, :addr, :latitude, :longitude)'''

try:
    # 데이터 파싱 및 저장 루프
    for jd in json_data['GGEXPSDLV'][1]['row']:
        SIGUN = jd.get('SIGUN')
        BIZNM = jd.get('BIZNM')
        BIZNO = jd.get('BIZNO')
        # 기존 코드에서 ADDR에 BIZNO를 넣던 오류 수정 및 None 값 대비 안전하게 .get() 사용
        ADDR = jd.get('REFINE_ROADNM_ADDR') if jd.get('REFINE_ROADNM_ADDR') else jd.get('REFINE_LOTNO_ADDR') 
        REFINE_WGS84_LAT = jd.get('REFINE_WGS84_LAT')
        REFINE_WGS84_LOGT = jd.get('REFINE_WGS84_LOGT')          
        
        try:
            # SQL 바인딩 변수와 파이썬 변수 매핑
            cursor.execute(sql, sigun=SIGUN, biznm=BIZNM, bizno=BIZNO, addr=ADDR, 
                           latitude=REFINE_WGS84_LAT, longitude=REFINE_WGS84_LOGT)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print("Insert 에러 발생:", e)

except KeyError as e:
    print("API 응답 구조에 문제가 있거나 데이터를 찾을 수 없습니다:", e)

# 연결 종료
cursor.close()
conn.close()
print("DB저장 종료")

