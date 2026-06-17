import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic') 
sns.set_style('whitegrid')

'''
패싯그리드 : 조건을 적용하여 화면을 그리드로 분할. 
    행, 열 방향으로 서로 다른 조건을 적용하여 여러개의 서브플롯(그래프)을
    만든다. 열 방향으로 who(탑승객구분) 행 방향으로 survived(생존여부)
    로 구분한다. 
'''
g = sns.FacetGrid(data=titanic, col='who', row='survived') 
g = g.map(plt.hist, 'age')
plt.show()
