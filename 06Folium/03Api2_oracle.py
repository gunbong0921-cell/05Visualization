'''
오라클 사용을 위한 모듈 임포트
설치 >> conda install -y oracledb
'''
import oracledb

# 오라클 접속을 위한 기본정보
host_name = 'localhost'
oracle_port = 1521
service_name = 'xe'
# 접속정보를 통해 오라클 연결 및 conn 객체 생성
conn = oracledb.connect(
  user='education',
  password='1234', 
  host=host_name,
  port=oracle_port,
  service_name=service_name
)
# 쿼리문 실행을 위한 커서 생성
cursor = conn.cursor()

# 입력 데이터(하드코딩으로 준비)
SIGUN_NM = "나의시군"
FACLT_NM = "코스모대학교"
REFINE_LOTNO_ADDR = "서울시 금첨구 가산동 월드메르디앙"
REFINE_WGS84_LAT = 37.1234
REFINE_WGS84_LOGT = 126.1234

# 인파라미터가 있는 insert 쿼리문 작성. 인파라미터는 :변수명과 같이 작성.
sql = """insert into g_univ (idx, sigun, faclt, addr,
                latitude, longitude)
        Values (seq_board_num.nextval,  :sigun, :faclt, :addr,
                :latitude, :longitude)"""
try:
  # 쿼리문 실행 시 인파라미터에 값 설정
  cursor.execute(sql, sigun=SIGUN_NM, faclt=FACLT_NM,
                 addr=REFINE_LOTNO_ADDR,
                 latitude=REFINE_WGS84_LAT,
                 longitude=REFINE_WGS84_LOGT)
  # 쿼리문 실행에 문제가 없다면 커밋해서 실제 테이블에 적용 
  conn.commit()
  print("1개의 레코드 입력")
except Exception as e:
  # 예외가 발생된다면 롤백
  conn.rollback()
  print("insert 실행시 오류발생", e)
# 모든 작업이 완료되면 DB연결 해제
conn.close() 
   