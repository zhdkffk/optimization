import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('sharing_bike_train.csv')

#문자열로 돼 있는 날짜를 시간으로 바꿔 줌
df["year"] = pd.to_datetime(df["datetime"]).dt.year
df["month"] = pd.to_datetime(df["datetime"]).dt.month
df["day"] = pd.to_datetime(df["datetime"]).dt.day
df["hour"] = pd.to_datetime(df["datetime"]).dt.hour
df["weekday"] = pd.to_datetime(df["datetime"]).dt.weekday

#불필요한 속성 제거
del df["datetime"] #문자열로바꿧으니까지우나봄?
del df["casual"] #여기서부터는 날씨에영향을안주는것들
del df["registered"]
del df["count"]

#one hot encoding
df["year"] = df["year"].astype("category")
df["month"] = df["month"].astype("category")
df["day"] = df["day"].astype("category")
df["hour"] = df["hour"].astype("category")
df["weekday"] = df["weekday"].astype("category")
df["season"] = df["season"].astype("category")
#컴퓨터가 받아들이는 이것들의 타입을 "category"라고 정의한 것임 = 종류만 인식되게 바꿈(문자1문자2머이렇게..)

df = pd.get_dummies(df)

#print(df.shape)를 하면 10886*75가 나옴!

#테스트 데이터 분리
train = df.sample(frac=0.8, random_state=200) #train:학습. 샘플: 일부를 추출하는 거. "80%를 추출하고", 랜덤값을 만들 때 200만큼 랜덤??
test = df.drop(train.index) #검증. 그니까학습용데이터와 검증용데이터를 분리한걱ㅈ. 나머지20퍼를 갖고검증하는거..래

#열을선택하는거
train_y = train["weather"] #목표가날씨다 - x값을통해y값을구하는거
del train["weather"] #그러니까train에서목표값(날씨)를지우는거지
train_x = train #필요한속성만!

test_y = test["weather"]
del test["weather"]
test_x = test
#오버피팅: 학습데이터만딱맞아떨어지는거 = 따른데이터는못맞힘.. 그걸방지하기위해test데이터분리
#언더피팅: 너무못맞히는거

knn = KNeighborsClassifier(n_neighbors=2) #n_neighbors = 볼 주변데이터개수.. 바꾸면서테스트를해봐야댐
knn.fit(train_x, train_y)
score = knn.score(test_x, test_y)
print(score)