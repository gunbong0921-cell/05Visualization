# 라이브러리 임포트
from turtle import color

from numpy import size
import pandas as pd
import matplotlib.pyplot as plt

# 한글깨짐 처리를 위해 폰트매니저 임포트
# 한글깨짐처리 Start
from matplotlib import font_manager, markers, rc
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
print(df_seoul)
sr_one = df_seoul.loc['경기도']
print(sr_one)

# 그래프 스타일 지정하기 : ggplot과 같은 스타일은 URL참조
# https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
plt.style.use('ggplot')

# 그래프의 캔버스 사이즈를 14:5 비율로 설정
# 그래프 설정 추가 Start
plt.figure(figsize=(14, 5))
# x축 라벨을 수직방향으로 설정해서 텍스트가 겹쳐지는것을 방지
# vertical 과 90은 동일한 설정. 즉 정수형태로 각도를 부여할 수 있다.
plt.xticks(sr_one.index.astype(int), rotation='vertical')
# plt.xticks(sr_one.index.astype(int), rotation=90)
# plt.xticks(sr_one.index.astype(int), rotation=60)
# plt.xticks(sr_one.index.astype(int), rotation=320)
# 그래프 설정 추가 end

# x, y축 데이터를 plot 함수에 입력
# 마커와 마커사이즈를 지정하여 깍은선 부분에 표시(추가)
plt.plot(sr_one.index.astype(int), sr_one.values, marker='o', markersize=10)

# 타이틀 및 라벨설정
plt.title('서울 -> 경기 인구 이동', size=30)
plt.xlabel('기간', size=20)
plt.ylabel('이동 인구수', size=20)

# 범례 표시(그래프 이미지 내부에 설명 문구가 추가됨)
# 범례 추가
plt.legend(labels=['서울->경기'], loc='best') # 디폴트 값
# plt.legend(labels=['서울->경기'], loc='upper left') # 좌측 상단
# plt.legend(labels=['서울->경기'], loc='lower right') # 우측 하단

# Y측에 표시할 데이터의 범위를 짖어(최소, 최댓값)
plt.ylim(50000, 800000)

# 첫번째 화살표 표시
plt.annotate('', 
             xytext=(1972, 290000), # 시작
             xy=(1990, 620000), # 종료
             xycoords='data',
            #  화살표의 속성(스타일, 색깔, 굷기)
             arrowprops=dict(arrowstyle='->', color='skyblue', lw=2),
             )
# 두번째 화살표
plt.annotate('', 
             xytext=(2000, 580000), 
             xy=(2017, 450000), 
             xycoords='data',
             arrowprops=dict(arrowstyle='->', color='olive', lw=5),
             )
# 텍스트 주석 표시
'''
va : 글자를 수직(세로) 방향에서 정렬하는 속성
    center, top, bottom, baseline 등
ha : 수평(좌우) 방향에서 정렬하는 속성
    center, left, right 등    
'''
plt.annotate('인구이동 증가(1970-1995)', 
             xy=(1980, 450000), 
             rotation=25, 
             va='baseline',
             ha='center', 
             fontsize=15,
             color = 'black'
             )
plt.annotate('인구이동 감소(1995-2017)', 
             xy=(2010, 560000), 
             rotation=10, 
             va='baseline',
             ha='center', 
             fontsize=15,
             color = 'black'
             )

# 그래프 출력
plt.show()