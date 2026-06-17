import pandas as pd
import matplotlib.pyplot as plt

'''
버블차트(Bubble chart)
  : 실린더 갯수를 나타내는 정수를 해당 열의 최대값으로 상태적 크기를
  나타내는 비율로 계산해서 점의 크기를 다르게 표현한다.
  점의 모양이 비눗방울 같다고 해서 붙여진 이름이다.
'''
plt.style.use('default')

df = pd.read_csv('../resData/auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 실린더 갯수의 상대적 비율을 계산해서 점의 크기 s에 적용한다.
cylinders_size = df.cylinders / df.cylinders.max() * 300
# 하나의 컬럼을 대상으로 했으므로 시리증로 생성된다.
print(cylinders_size)
'''
kind : 버블차트는 산점도를 기반으로 한다.
c : 점의 색깔
s : 점의 크기
cmap : 색깔을 정하는 컬러맵
'''
df.plot(kind='scatter', x='weight', y='mpg', c='coral', figsize=(10,5), s=cylinders_size, alpha=0.3,
        marker='o', cmap='viridis')
plt.title('Scatter plot : mpg-weight-cylinders')

# 출력된 그래프를 png 이미지 파일로 저장.
plt.savefig("../saveFiles/scatter.png")
# transparent 옵션으로 배경이 투명한 이미지로 저장된다.
plt.savefig("../saveFiles/scatter_transparent.png", transparent=True)
plt.show()