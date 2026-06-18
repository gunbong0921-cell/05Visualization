# 모듈 임포트
import folium
import oracledb

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

univ_map = folium.Map(location=[37.40,127.38], zoom_start=10)
univ_map.save('../saveFiles/univ_map.html')

sql = "select * from g_univ order by idx asc"
cursor.execute(sql)
for rs in cursor:
  idx = rs[0]
  sigun = rs[1]
  faclt = rs[2]
  addr = rs[3]
  latitude = rs[4]
  longitude = rs[5]
  folium.Marker([latitude,longitude],
                popup=faclt).add_to(univ_map)
  print(faclt, latitude, longitude)
  
  univ_map.save('../saveFiles/univ_map_marker.html')
  print("맹비 생성되었습니다.")