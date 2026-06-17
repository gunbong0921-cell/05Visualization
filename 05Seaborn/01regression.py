import matplotlib.pyplot as plt
import seaborn as sns

'''
회귀(regression)
  : 통계학에서 변ㅅ들간의 관계를 분석하고 예측하는데 사용되는
  통계적 방법을 의미한다.
regplot()
  : 회귀선이 있는 산점도를 표현해주는 함수. 서로 다른 2개의 연속변수
  사이의 산점도를 그리고 선형회귀 분석을 위한 회귀선을 표시한다.
  회귀의 목적은 데이터에서 패턴을 학습해서 새로운 데이터에 대한 예측을
  수행하는 것이다.  
'''
# 씨본에서 제공하는 타이타닉 데이터셋 로드
titanic = sns.load_dataset('titanic')
# 데이터셋의 처음 or 마지막의 데이터 확인. 디폴트값은 5개.
print(titanic.head())
print(titanic.tail(10))

sns.set_style('darkgrid')
# 캔버스의 크기 설정
fig = plt.figure(figsize=(15, 5))
# Axe 객체를 1행 2열로 지정한 후 가로형으로 2개의 그래프를 표현
axe1 = fig.add_subplot(1,2,1)
axe2 = fig.add_subplot(1,2,2)
# x축은 나이, y축은 운임요금 설정
sns.regplot(x='age', y='fare', data=titanic, ax=axe1)
# fit_reg : 회귀선을 표시하기 위한 옵션, True가 디폰트값.
sns.regplot(x='age', y='fare', data=titanic, ax=axe2, fit_reg=False)

plt.show()
