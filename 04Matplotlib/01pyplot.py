import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('../resData/시도별_전출입_인구수.xlsx', engine='openpyxl', header=0)
# print(df.head())

# pandas에서 3.x
# df = df.fillna(method='ffill') 
# 누락값(NaN)을 앞 부분의 데이터로 채워준다.
df = df.ffill()
'''
데이터는 일반적으로 근접한것끼리 관련이 높을 수 있으므로 누락값은 보통
이런 방식으로 대체하게된다. 즉 NaN이 '전국'으로 대체된다.
'''
print(df.head())

'''
전출지별 에서는 서울특별시민 추출하고,
전입지별에서는 서울특별시가 아닌 데이터만 추출하기 위해 mask 변수를
생성한다.
즉 서울에서 다른지역으로 전출한 데이터만 남기기 위함이다.
'''
mask = (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')
df_seoul = df[mask]
'''
전출지별 컬럼(열)을 삭제한다. 즉 옵션이 1로 지정되지 않았다면 행이
삭제된다. 또한 Inplace 옵션이 없으므로 원본은 보존되고, 변경된
새로운 객체가 반환된다.
'''
df_seoul = df_seoul.drop(['전출지별'], axis=1)
# 컬럼명을 변경한 후 원본 데이터프레임에 적용
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
# 이름을 변경한 전입지를 인덱스로 지정
df_seoul.set_index('전입지', inplace=True)
print(df_seoul)

'''
서울에서 경기도로 전출한 행만 추출한다. 앞에서 문자형 인덱스로
지정했으므로 loc 함수를 사용한다. 만약 숫자형 인덱스를 사용한다면
iloc 함수를 사용해야한다.
'''
sr_one = df_seoul.loc['경기도']
print(sr_one)
# 여기까지 실행하면 전출입 인구수 데이터 전처리는 완료된다.

# 그래프에 x축, y축에 인덱스와 값을 적용
plt.plot(sr_one.index, sr_one.values)
# 제목과 x,y축의 라벨 추가
plt.title('서울 -> 경기 인구 이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')
# 여기서 그래프가 출력된다.
plt.show()
