import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import metrics

df = pd.read_csv('sharing_bike_train.csv')

#문자열로 돼 있는 날짜를 시간으로 바꿔 줌
df["year"] = pd.to_datetime(df["datetime"]).dt.year
df["month"] = pd.to_datetime(df["datetime"]).dt.month
df["day"] = pd.to_datetime(df["datetime"]).dt.day
df["hour"] = pd.to_datetime(df["datetime"]).dt.hour
df["weekday"] = pd.to_datetime(df["datetime"]).dt.weekday

del df["datetime"]
del df["casual"]
del df["registered"]
#카운트가 목표값이라 뺀거임

#one hot encoding
df["year"] = df["year"].astype("category")
df["month"] = df["month"].astype("category")
df["day"] = df["day"].astype("category")
df["hour"] = df["hour"].astype("category")
df["weekday"] = df["weekday"].astype("category")
df["season"] = df["season"].astype("category")
df["weather"] = df["weather"].astype("category")
#컴퓨터가 받아들이는 이것들의 타입을 "category"라고 정의한 것임 = 종류만 인식되게 바꿈(문자1문자2머이렇게..)

df = pd.get_dummies(df)

#테스트 데이터 분리
train = df.sample(frac=0.8, random_state=200) #train:학습. 샘플: 일부를 추출하는 거. "80%를 추출하고", 랜덤값을 만들 때 200만큼 랜덤??
test = df.drop(train.index) #검증. 그니까학습용데이터와 검증용데이터를 분리한걱ㅈ. 나머지20퍼를 갖고검증하는거..래

#열을선택하는거
train_y = train["count"] #목표가날씨다 - x값을통해y값을구하는거
del train["count"] #그러니까train에서목표값(날씨)를지우는거지
train_x = train #필요한속성만!

test_y = test["count"]
del test["count"]
test_x = test

mlr = LinearRegression()

mlr.fit(train_x, train_y)

prediction = mlr.predict(train_x)
score = metrics.r2_score(train_y, prediction)
print(score)

prediction = mlr.predict(test_x)
score = metrics.r2_score(test_y, prediction)
print(score)