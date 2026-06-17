import pandas as pd
import matplotlib.pyplot as plt

'''
히스토그램
  : 변수가 하나인 단변수 데이터의 빈도수를 표현하는 그래프.
  x축을 같은 크기의 여러 구간으로 나누고, 각 구간에 속하는 데이터
  값의 갯수를 y축에 표시한다. 
'''
plt.style.use('classic')
# 자동차 연비 데이터를 데이터프레임으로 변환
df = pd.read_csv('../resData/auto-mpg.csv', header=None)
# 컬럼명 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
# '연비'를 통해 히스토그램 생성
# df['mpg'].plot(kind='hist', bins=10, color='coral', figsize=(10,5))
df['mpg'].plot(kind='hist', bins=15, color='coral', figsize=(10,5))
'''
bins 옵션으로 10개의 구간으로 나눠준다. 수치가 커지면 더 많이
세분환 할 수 있으므로 그래프의 폭이 좁아진다. 
'''
plt.title('Histogram')
plt.xlabel('mpg')
plt.show()