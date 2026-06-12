import pandas as pd

# 딕셔너리 선언
dict_data = {'a':1, 'b':2, 'c':3}
sr = pd.Series(dict_data)
print('타입', type(sr))
print('시리즈1\n', sr)

print("="*30)

list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
idx = sr.index
val = sr.values
print('시리즈2\n', sr)
print('인덱스', idx)
print('값', val)

print("="*30) 

# 튜플 선언
tuple_data = ('유겸', '2012-04-03', True)
sr = pd.Series(tuple_data, index=['이름', '생년월일', '성별', '학생여부'])

print('시리즈3\n', sr)
print('숫자형인덱스', sr[0]) # FuturWarning 발생
print('문자형인덱스', sr['이름'])

print('1,2출력\n', sr[[1, 2]]) # FuturWarning 발생
print('생년월일, 성별 출력\n', sr[['생년월일', '성별']])

print('슷자형 범위\n', sr[1 : 2])
print('문자형 범위\n', sr['생년월일' : '학생여부'])
