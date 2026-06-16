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

# 행과 열을 전치
df4 = df4.transpose()
# 스타일 설정
plt.style.use('ggplot')
# 데이터프레임의 인덱스를 정수형으로 변경
df4.index = df4.index.map(int)
# 막대그래프를 세로형(수직방향)으로 생성. 막대의 두께, 색깔 설정.
df4.plot(kind='bar', figsize=(20,10), width=0.7,
         color=['orange','green','skyblue','blue'])

# 타이틀, 범례 설정
plt.title('서울 -> 타시도 인구 이동', size=30)
plt.ylabel('이동 인구 수', size=20)
plt.xlabel('기간', size=20)
plt.ylim(5000, 30000)
plt.legend(loc='best', fontsize=15)

plt.show()
