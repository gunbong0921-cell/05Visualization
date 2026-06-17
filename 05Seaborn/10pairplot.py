import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')
sns.set_style('whitegrid')

'''
페어플롯 : 이변수 데이터의 분포를 표현하기 위해 데이터프레임의 
    열(변수)을 두개씩 짝지어 표현한다. '''
titanic_pair = titanic[['age', 'pclass', 'fare']]

g = sns.pairplot(titanic_pair)
plt.show()
