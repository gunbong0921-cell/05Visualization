# 판다스, 씨본 모듈 임포트 
import pandas as pd
import seaborn as sns

# Seaborn에서 제공하는 타이타닉 탑승자 데이터셋 로드 
titanic = sns.load_dataset('titanic')
# 데이터셋에서 나이와 운임요금만 추출 
df = titanic.loc[:, ['age','fare']]
# 데이터셋의 처음과 마지막 행을 5개씩 출력 
print(df.head())
print(df.tail())  

# 데이터프레임 전체에 10을 합산 
addition = df + 10
print(addition.head()) 

'''
컬럼명이 동일한 항목을 찾아 덧셈 연산을 한다. 문자형인 경우에는
단어가 연결된다. '영어'는 한쪽이 없는 상태이므로 NaN으로 표시된다.'''
exam_data1 = {'이름' : [ '서준', '우현', '인아'],
                              '국어' : [ 90, 80, 70],
                              '영어' : [ 98, 89, 95],}
subject1 = pd.DataFrame(exam_data1)

exam_data2 = {'이름' : [ '유비', '관우', '장비'],
                              '국어' : [ 1, 2, 3]}
subject2 = pd.DataFrame(exam_data2)
print(subject1+subject2)
