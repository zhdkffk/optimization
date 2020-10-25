# simple: 작은 데이터, full: 큰 데이터
# simple로 학습된 모델을 full 데이터로 검증하는 방법 / simple로 원하는 결과에 도달하는지 보고 full로 "재실행" 하는 방법
# balance: 예금액, housing: 주택 담보 대출 유무, default: 채무 불이행 여부, campaign: 광고 몇 번 했는지, pdays: 광고 간의 시간 간격
# One hot encoding

import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('bank_marketing_simple.csv', sep=';')

df = pd.get_dummies(df,columns=["job", "marital", "education", "default", "balance", "housing", "loan", "contact", "day",
                        "month", "poutcome"]) #onehotencoding을 할 칼럼을 골라서 하는 거


train = df.sample(frac=0.8, random_state=200)
test = df.drop(train.index)

train_y = train['y']
del train['y']
train_x = train

test_y = test['y']
del test['y']
test_x = test

logistic = LogisticRegression(solver='newton-cg')
#solver를 쓴다 = 알고리즘을 바꾼다. 기본값을 쓰면 데이터 처리의 양에 한계가 있음. 더 많은 데이터를 처리하기 위해 newton그거쓴다
logistic.fit(train_x, train_y)

score = logistic.score(test_x, test_y)

# 검증데이터(다른파일에서 train test 그거빼고이거한거임)
dd = pd.read_csv('bank_marketing_full.csv')
dd = pd.get_dummies(dd,columns=["job", "marital", "education", "default", "balance", "housing", "loan", "contact", "day", "month", "poutcome"])

dtrain = dd.sample(frac=0.8, random_state=200)
dtest = dd.drop(train.index)

dtrain_y = dtrain['y']
del dtrain['y']
dtrain_x = dtrain

dtest_y = dtest['y']
del dtest['y']
dtest_x = dtest

dscore = logistic.score(dtest_x, dtest_y)

print(dscore)

