# 모듈 임포트
import oracledb
import requests, json

# 오라클 접속을 위한 정보
host_name = 'localhost'
oracle_port = 1521
service_name = 'xe'

# 접속 정보를 통해 오라클 연결 및 conn객체 생성
conn = oracledb.connect(
  user='education',
  password='1234', 
  host=host_name,
  port=oracle_port,
  service_name=service_name
)
# 커서 생성
cursor = conn.cursor()

# OpenAPI의 요청URL과 파라미터 준비
url = 'https://openapi.gg.go.kr/Jnclluniv?'
params = dict(Type='json', pSize='300',
              KEY='37036b829e80435b9bd513cb9d7cdfd3')

# 요청 및 JSON데이터 가져오기
raw_data = requests.get(url=url, params=params)
binary_data = raw_data.content
json_data = json.loads(binary_data)

# 인파라미터가 있는 insert 쿼리문 작성 (반복문 밖에서 한 번만 정의)
sql = """insert into g_univ (idx, sigun, faclt, addr, latitude, longitude)
        Values (seq_board_num.nextval, :sigun, :faclt, :addr, :latitude, :longitude)"""

success_count = 0  # 성공 횟수 체크용 변수

# 데이터의 갯수만큼 반복
for jd in json_data['Jnclluniv'][1]['row']:
    # .get()을 사용하면 해당 키가 없을 때 에러 대신 None을 반환하여 안전합니다.
    SIGUN_NM = jd.get('SIGUN_NM') # 시군명
    FACLT_NM = jd.get('FACLT_NM') # 대학명
    REFINE_LOTNO_ADDR = jd.get('REFINE_LOTNO_ADDR') # 주소
    
    # 위도/경도가 빈 문자열("")이거나 None이면 DB에 맞게 처리되도록 설정
    REFINE_WGS84_LAT = jd.get('REFINE_WGS84_LAT') if jd.get('REFINE_WGS84_LAT') else None
    REFINE_WGS84_LOGT = jd.get('REFINE_WGS84_LOGT') if jd.get('REFINE_WGS84_LOGT') else None

    # ★ 중요: insert 처리를 for문 안으로 이동 ★
    try:
        cursor.execute(sql, sigun=SIGUN_NM, faclt=FACLT_NM,
                       addr=REFINE_LOTNO_ADDR,
                       latitude=REFINE_WGS84_LAT,
                       longitude=REFINE_WGS84_LOGT)
        success_count += 1
    except Exception as e:
        print(f"[{FACLT_NM}] insert 실행시 오류발생:", e)
        # 건별로 오류가 나더라도 다음 데이터는 계속 들어가도록 pass 하거나 rollback 처리
        conn.rollback() 

# 모든 반복이 끝난 후 한 번에 커밋 (속도 향상 및 트랜잭션 관리)
conn.commit()
print(f"총 {success_count}개의 레코드 입력 완료")

# 연결 종료
cursor.close()
conn.close()
    