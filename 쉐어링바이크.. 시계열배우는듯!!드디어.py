#시계열로 되어 있는 데이터는 날짜 및 시간을 포함하고 잇삼
#하지ㅏㅁㄴ 문자열로 데이터를 읽어오기때문에계싼이 불가
#데이터에 대한 판단!!!이 우선 필요 - "꼭필요한데이터인가?"
#날자와 시간은 실제로는 숫자로 치환 가능

#season - 1:봄, 2:여름, 3:가을, 4:겨울
#weather - 1:맑음, 약간 구름낌/ 2:박무, 구름낌/ 3:약간의 눈, 비, 천둥/ 4:안개, 강한 비, 우박

#날짜 데이터의 변환 방법
#1. 큰의미가없으면 - 삭제, 레이블인코딩
#2. 의미가쫌잇으면 - 필요한수준까지시간을분리(초까지가능) or 단일수치(timestamp)로 변경(레이블인코딩과큰차이x음)

#**분석하기전에!!!생각해생각해
#1. 데이터를보고 어떤 속성을 사용할 것인지
#2. 어떤 분석 방법을 사용할 것인지
import pandas as pd
df = pd.read_csv('sharing_bike_train.csv')
#데이터변환
df["year"] = pd.to_datetime(df["datetime"]).dt.year
df["month"] = pd.to_datetime(df["datetime"]).dt.month
df["day"] = pd.to_datetime(df["datetime"]).dt.day
df["hour"] = pd.to_datetime(df["datetime"]).dt.hour

#불필요한 데이터 지우기
del df["datetime"]
del df["casual"] #count = casual + registered이므로 둘을 지우고 count만 사용
del df ["registered"]

#one hot encoding하기
df = pd.get_dummies(df) #x_a, x_b같은걸자동으로해줌
#모든 속성의 이름을 나열하는 게 쉽지 않음.. - 필요한 데이터만 놔두고 지움 (데이터 분리를 통 데이터 사용 - 이게뭔말인지..)
