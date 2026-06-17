import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "../resData/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

'''
박스플롯
  : 범주형 데이터의 분포를 파악하기에 적합한 그래프.
  최소, 최대, 1분위값, 중간값, 2분위값, 이상치 등의 정보를
  한꺼번에 제공한다.
'''
# 사용가능한 스타일 목록 확인하기
print(plt.style.available)
plt.style.use('fast') # fast / ggplot
# 마이너스 부호 출력 설정
plt.rcParams['axes.unicode_minus']=False

# 연비 데이터를 데이터프레임으로 변환
df = pd.read_csv('../resData/auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 캔버스의 크기 설정
fig = plt.figure(figsize=(15, 5))
# Axe 객체 생성(1행 2열)
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
'''
각 Axe 객체에 boxplot 함수로 그래프 생성. 제조국가별 연비 분포를
데이터로 적용한다.
'''
# 수직형으로 설정(디폰트 값)
ax1.boxplot(x=[df[df['origin']==1]['mpg'],
               df[df['origin']==2]['mpg'],
               df[df['origin']==3]['mpg']],
            tick_labels=['USA', 'EU', 'JAPAN'])
# 수평형으로 출력. vert 옵션을 False로 지정.
ax2.boxplot(x=[df[df['origin']==1]['mpg'],
               df[df['origin']==2]['mpg'],
               df[df['origin']==3]['mpg']],
            tick_labels=['USA', 'EU', 'JAPAN'],
            vert=False)

# 타이틀 설정
ax1.set_title('제조국가별 연비 분포(수직 박스 플롯)')
ax2.set_title('제조국가별 연비 분포(수평 박스 플롯)')

'''
그래프의 상단 혹은 우측에 o로 표시되는 값이 있는데, 보통 관측되는
데이터의 범위를 많이 벗어난 값으로 '이상치'라고 표현한다.
'''
plt.show()