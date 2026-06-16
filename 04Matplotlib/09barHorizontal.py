# 라이브러리 임포트
from cProfile import label
from turtle import color

from numpy import size
import pandas as pd
import matplotlib.pyplot as plt

# 한글깨짐 처리를 위해 폰트매니저 임포트
# 한글깨짐처리 Start
from matplotlib import font_manager, markers, rc
from pyparsing import line
# 한글폰트 경로 설정
font_path = "../resData/malgun.ttf"
# 폰트 파일의 이름을 속성으로 지정
font_name = font_manager.FontProperties(fname=font_path).get_name()
# 폰트 적용
rc('font', family=font_name)
# 한글깨짐처리 end

# 데이터프레임 만들기
df = pd.read_excel('../resData/시도별_전출입_인구수.xlsx', engine='openpyxl', header=0)
# df = df.fillna(method='ffill') 
df = df.ffill()
print(df.head())

# 서울에서 경기로 전출할 데이터만 추출
mask = (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)
# print(df_seoul)
# sr_one = df_seoul.loc['경기도']
# print(sr_one)
# 데이터 전처리 완료

# 기존 연도를 1970 -> 2010으로 수정
col_years = list(map(str, range(2010, 2018)))
# 각 4개의 도를 선택해서 데이터 추출 / 연도 지정 
df4 = df_seoul.loc[['충청남도','경상북도', '강원도', '전라남도'], col_years]

# 앞에서 적용한 연도 사이에 이동한 인구수를 각 도별로 합산하여 새로운 열 추가
df4['합계'] = df4.sum(axis=1)
# 새롭게 생성한 '합계' 열을 오름차순으로 정렬하여 변수에 저장
df_total = df4[['합계']].sort_values(by='합계', ascending=True)
plt.style.use('ggplot')
# 수평방향의 막대그래프를 생성
df_total.plot(kind='barh', color='cornflowerblue', width=0.5, figsize=(10,5))

plt.title('서울 -> 타시도 인구 이동')
plt.ylabel('전입지')
plt.xlabel('이동 인구 수')

plt.show()

