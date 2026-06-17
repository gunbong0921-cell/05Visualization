import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic') 
sns.set_style('whitegrid')

# 2행 2열로 틀을 생성한 후 4개의 Axe객체 배치 
fig = plt.figure(figsize=(15, 10))   
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

'''
boxplot : 범주형 데이터 분포와 주요 통계 지표를 함께 제공하는 그래프.
    단, 데이터가 퍼져있는 분산의 정도는 정확히 알기 어려운 단점이 있다.
violinplot : 데이터가 퍼져 있는 분산의 정도를 알기위해 사용하는 그래프.
'''
# 박스플롯(디폴트값)
sns.boxplot(x='alive', y='age', data=titanic, ax=ax1) 
# hue 옵션을 추가하여 남녀 데이터를 구분할 수 있다. 
sns.boxplot(x='alive', y='age', hue='sex', data=titanic, ax=ax2) 
# 바이올린 그래프(디폴트값)
sns.violinplot(x='alive', y='age', data=titanic, ax=ax3) 
# hue 옵션에 성별 추가 
sns.violinplot(x='alive', y='age', hue='sex', data=titanic, ax=ax4) 

plt.show()



