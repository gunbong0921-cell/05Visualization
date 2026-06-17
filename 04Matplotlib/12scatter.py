import pandas as pd
import matplotlib.pyplot as plt

'''
산점도(Scatter plot)
  : 연속되는 값을 갖는 서로 다른 두 변수 사이의 관계를 나타내는
  그래프로 x, y축에 변수를 두고 데이터가 위치한 좌표를 찾아 점(dot)
  으로 표시해준다.
'''
plt.style.use('default')

df = pd.read_csv('../resData/auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
'''
x축 : 자동차의 무게(weight)를 사용
y축 : 연비(mpg)를 사용
s : 점의 크기 설정
'''
df.plot(kind='scatter', x='weight', y='mpg', c='blue', s=10, figsize=(10,5))
# df.plot(kind='scatter', x='weight', y='mpg', c='blue', s=20, figsize=(10,5))
plt.title('Scatter plot - mpg VS weight')
plt.show()