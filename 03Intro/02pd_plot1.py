import pandas as pd
import matplotlib.pyplot as plt

# 데이터프레임으로 변환시 header옵션이 없으므로 첫행은 컬럼명으로
# 인식
df = pd.read_excel('../resData/남북한_발전_전력량.xlsx',
                   engine='openpyxl')

# [0,5] => 엑셀의 2행과 7행을 의미한다. 
# 3: => D열부터 마지막을 의미
df_ns = df.iloc[[0, 5], 3:]

#남북한 데이터에 인덱스 부여
df_ns.index = ['South','North'] 

#열 이름의 자료형을 정수형으로 변경
df_ns.columns = df_ns.columns.map(int)

# 처음 5개 데이터 확인하기
print("원본 데이터", "="*30)
print(df_ns.head())
print("전치한 데이터", "="*30)
print(df_ns.T.head())

#선 그래프1(원본 데이터프레임)
df_ns.plot()
plt.show()

#선 그래프2(전치한 데이터프레임)
df_ns.T.plot()
plt.show()

#막대 그래프1(원본 데이터프레임)
df_ns.plot(kind='bar')
plt.show()

#막대 그래프1(전치한 데이터프레임)
df_ns.T.plot(kind='bar')
plt.show()

#히스토그램(전치한 데이터프레임)
df_ns = df_ns.apply(pd.to_numeric, errors='coerce')
df_ns.T.plot(kind='hist')
plt.show()
