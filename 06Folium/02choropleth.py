import pandas as pd
import folium
import json

'''
Choropleth Map(코로프레스 맵)
  : 행정구역과 같이 지도상에 경계를 표시하기 위한 맵
'''
file_path = '../resData/경기도_인구_데이터.xlsx'
df = pd.read_excel(file_path, index_col='구분', engine= 'openpyxl')
# 모든 컬럼을 문자형으로 변환
df.columns = df.columns.map(str)

'''
경기도 사군구 경계 정보를 가진 geo-json 파일을 로드한다.
행정구역이 여러개의 위경도로 표현되어있다.
'''
geo_path = '../resData/경기도_행정구역_경계.json'
try:
  # 파일 오픈 시 다국어를 지원하는 utf-8 캐릭터셋으로 인코딩 처리
  geo_data = json.load(open(geo_path, encoding='utf-8'))
except:
  geo_data = json.load(open(geo_path, encoding='utf-8-sig'))  

# 폴리엄을 통해 지도 생성
g_map = folium.Map(location=[37.5502, 126.982], zoom_start=9)
# 연도 지정(파일명에 추가됨)
year = '2017'
'''
geo_data : 지도 데이터 혹은 파일의 경로
data : 시각화를 위한 데이터파일(여기서는 데이터프레임)
columns : 자동데이터와 매핑할 값(시각화 할 변수 지정)
key_on : 데이터 파일과 매핑할 값
'''
folium.Choropleth(geo_data=geo_data, 
                  data = df[year],
                  columns = [df.index, df[year]],
                  fill_color='PuBuGn', fill_opacity=0.7,
                  line_opacity=1,
                  key_on='feature.properties.name',
                  legend_name='경기도인구데이터',
                  ).add_to(g_map)
# 설정한 연도를 파일명에 적용해서 HTML로 저장
g_map.save('../saveFiles/gyonggi_population_' + year + '.html')  