'''
폴리엄 라이브러리는 별도로 설치 필요함.
>> conda install -y folium

folium 라이브러리
  : 데이터를 지도로 시각화 해주는 라이브러리.
  코드를 실행하면 IDE에서 직접 지도가 표시되지 않고, HTML파일로
  저장되어 웹브라우저를 통해 확인해야한다. 웹서버(Tomcat등)가
  있다면 특정 경로를 지정해서 저장한 후 Spring등과 연동할 수 있다.
'''
import folium

# 맵생성 : 인수로지도 중앙의 위/경도와 줌 레벨 지정
seoul_map1 = folium.Map(location=[37.55,126.98], zoom_start=12)
seoul_map1.save('../saveFiles/seoul1.html')

# 타일 설정 : 산악지형 강조, 도로망 강조와 같은 표현이 가능함
seoul_map2 = folium.Map(location=[37.55,126.98], zoom_start=12,
                        tiles='CartoDB DarkMatter')
seoul_map2.save('../saveFiles/seoul2.html')

seoul_map3 = folium.Map(location=[37.55,126.98], zoom_start=15,
                        tiles='Esri.WorldImagery')
seoul_map3.save('../saveFiles/seoul3.html')

# 데이터프레임 사용을 위해 판다스 임포트
import pandas as pd
# 엑셀 파일을 데이터프레임으로 변환. 1행은 타이틀로 간주. 2행부터 가져옴.
df = pd.read_excel('../resData/서울지역_대학교_위치.xlsx',
                   engine='openpyxl')
# 컬럼명 추가
df.columns = ['학교명', '위도', '경도']
# 데이터프레임에 저장된 갯수만큼 반복하여 지도에 마커 추가
for name, lat, lng in zip(df.학교명, df.위도, df.경도):
  # 위경도는 리스트로 부여하고, popup(풍선도움말)은 학교명을 지정함
  folium.Marker([lat,lng], popup=name).add_to(seoul_map1)
# 마커가 추가된 Map을 HTML로 저장 
seoul_map1.save('../saveFiles/seoul_colleges1.html')

# 원형마커 및 옵션 설정(색깔, 투명도 등) 지정 
for name, lat, lng in zip(df.학교명, df.위도, df.경도):
  folium.CircleMarker([lat,lng], radius=10, color='brown', 
                      fill=True, fill_color='coral', 
                      fill_opacity=0.7, popup=name).add_to(seoul_map1)
seoul_map1.save('../saveFiles/seoul_colleges2.html')
