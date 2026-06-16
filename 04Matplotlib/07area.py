# 라이브러리 임포트
from cProfile import label
from turtle import color

from numpy import size
import pandas as pd
import matplotlib.pyplot as plt

# 한글깨짐 처리를 위해 폰트매니저 임포트
# 한글깨짐처리 Start
from matplotlib import font_manager, markers, rc
from pyparsing import alphas, line
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

# 1970~2017년까지 문자열로 리스트 생성
col_years = list(map(str, range(1970, 2018)))
# 각 4개의 도를 선택해서 데이터 추출 / 연도 지정 
df4 = df_seoul.loc[['충청남도','경상북도', '강원도', '전라남도'], col_years]

# 데이터프레임을 전치해서 행과 열을 교환
df4 = df4.transpose()
plt.style.use('ggplot')
# 데이터프레임의 인덱스를 정수형으로 변경. map 함수의 첫번째 인수로 int 함수 사용.
df4.index = df4.index.map(int)

'''
면적그래프
    kind='area' : 면적그래프를 그리기 위한 옵션
    stackind : 그래프를 겹쳐서 표현할지 여부를 결정
    alpha : 투명도 설정. 0~1사이로 표현하고, 0에 가까울수록
    투명하게 표현된다. 
'''
# false 인 경우 그래프를 겹쳐서 표현
# df4.plot(kind='area', stacked=False, alpha=0.2, figsize=(20,10))
# 겹치지 않게 표현
df4.plot(kind='area', stacked=True, alpha=0.2, figsize=(20,10))

# 제목. 타이틀 등 설정
plt.title('서울 -> 타시도 인구 이동', size=30)
plt.ylabel('이동 인구 수', size=20)
plt.xlabel('기간', size=20)
plt.legend(loc='best', fontsize=15)

plt.show()
