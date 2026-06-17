import matplotlib.pyplot as plt
import seaborn as sns

'''
stripplot : 이산형 변수의 데이터 분산을 고려하지 않고 그래프를 출력한다. 
    즉, 데이터가 겹쳐지는 경우가 발생한다. x축은 좌석등급, y축은 나이를
    사용한다. 
swarmplot : 데이터 분산을 고려하여 데이터가 겹쳐지지 않게 표현한다. 
    데이터가 퍼저있는 정도를 입체적으로 볼수있다. 
'''
titanic = sns.load_dataset('titanic')
sns.set_style('whitegrid')

fig = plt.figure(figsize=(15, 5))
axe1 = fig.add_subplot(1,2,1)
axe2 = fig.add_subplot(1,2,2)

sns.stripplot(x="class", y="age", data=titanic, ax=axe1)
sns.swarmplot(x="class", y="age", data=titanic, ax=axe2)

axe1.set_title('Strip Plot')
axe2.set_title('Swarm Plot')

plt.show()

