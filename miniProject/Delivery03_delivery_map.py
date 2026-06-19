import oracledb
import folium
import os

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

# 기본 지도 생성
delivery_apps = folium.Map(location=[37.40, 127.38], zoom_start=10)
loc = input('검색 주소를 입력하세요 (예: 수원시) : ')

sql = "SELECT * FROM delivery_apps WHERE sigun LIKE :loc"
search_keyword = f"%{loc}%"
cursor.execute(sql, loc=search_keyword)

for rs in cursor:
    idx = rs[0]
    sigun = rs[1]
    biznm = rs[2]
    bizno = rs[3]
    addr = rs[4]
    latitude = rs[5]
    longitude = rs[6]
    
    if latitude and longitude:
        folium.Marker([latitude, longitude], popup=biznm).add_to(delivery_apps)

# 상위 폴더에 saveFiles 폴더가 없다면 자동으로 만들어주는 안전장치
os.makedirs('../saveFiles', exist_ok=True)

# 파일 저장명 (예: delivery_map_수원시.html)
file_path = f'../saveFiles/delivery_map_{loc}.html'
delivery_apps.save(file_path)  

print(f'{file_path} 맵이 성공적으로 생성되었습니다.')

cursor.close()
conn.close()