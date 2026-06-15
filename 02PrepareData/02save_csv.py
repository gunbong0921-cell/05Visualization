import pandas as pd

# 딕셔너리를 통해 데이터프레임 생성
data = {
        'name' : [ 'Jerry', 'Riah', 'Paul'],
        'algol' : [ "A", "A+", "B"],
        'basic' : [ "C", "B", "B+"],
        'c++' : [ "B+", "C", "C+"],
}
df = pd.DataFrame(data)
# name 컬럼을 인덱스로 지정 
df.set_index('name', inplace=True)   
print(df)
# 데이터프레임을 csv파일로 저장 
df.to_csv("../saveFiles/hakjum.csv")
