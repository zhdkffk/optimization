import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import seaborn as sns

df = pd.read_csv('telecom_churn.csv')
df.dropna(inplace=True)  # 값이 없는 데이터 삭제

#라벨인코딩
le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])
df['Partner'] = le.fit_transform(df['Partner'])
df['Dependents'] = le.fit_transform(df['Dependents'])
df['PhoneService'] = le.fit_transform(df['PhoneService'])
df['MultipleLines'] = le.fit_transform(df['MultipleLines'])
df['InternetService'] = le.fit_transform(df['InternetService'])
df['OnlineSecurity'] = le.fit_transform(df['OnlineSecurity'])
df['OnlineBackup'] = le.fit_transform(df['OnlineBackup'])
df['DeviceProtection'] = le.fit_transform(df['DeviceProtection'])
df['TechSupport'] = le.fit_transform(df['TechSupport'])
df['StreamingTV'] = le.fit_transform(df['StreamingTV'])
df['StreamingMovies'] = le.fit_transform(df['StreamingMovies'])
df['Contract'] = le.fit_transform(df['Contract'])
df['PaperlessBilling'] = le.fit_transform(df['PaperlessBilling'])
df['PaymentMethod'] = le.fit_transform(df['PaymentMethod'])
df['Churn'] = le.fit_transform(df['Churn'])

# 검증데이터(다른파일에서 train test 그거빼고이거한거임)
dd = pd.read_csv('telecom_churn_test.csv')
dd.dropna(inplace=True)

dd['gender'] = le.fit_transform(dd['gender'])
dd['Partner'] = le.fit_transform(dd['Partner'])
dd['Dependents'] = le.fit_transform(dd['Dependents'])
dd['PhoneService'] = le.fit_transform(dd['PhoneService'])
dd['MultipleLines'] = le.fit_transform(dd['MultipleLines'])
dd['InternetService'] = le.fit_transform(dd['InternetService'])
dd['OnlineSecurity'] = le.fit_transform(dd['OnlineSecurity'])
dd['OnlineBackup'] = le.fit_transform(dd['OnlineBackup'])
dd['DeviceProtection'] = le.fit_transform(dd['DeviceProtection'])
dd['TechSupport'] = le.fit_transform(dd['TechSupport'])
dd['StreamingTV'] = le.fit_transform(dd['StreamingTV'])
dd['StreamingMovies'] = le.fit_transform(dd['StreamingMovies'])
dd['Contract'] = le.fit_transform(dd['Contract'])
dd['PaperlessBilling'] = le.fit_transform(dd['PaperlessBilling'])
dd['PaymentMethod'] = le.fit_transform(dd['PaymentMethod'])
dd['Churn'] = le.fit_transform(dd['Churn'])

sns.lmplot('tenure', 'TotalCharges', data=df, hue='Churn', fit_reg=False)
# plt.show()

train = df.sample(frac=0.9, random_state=200)
test = df.drop(train.index)

logistic = LogisticRegression(solver='newton-cg')
logistic.fit(df[["gender", "SeniorCitizen", "Partner", "Dependents", "tenure", "PhoneService",
                              "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection",
                              "TechSupport", "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod",
                              "MonthlyCharges", "TotalCharges"]], df['Churn'])
# score = logistic.score(test[['tenure', 'TotalCharges']], test['Churn'])

dscore = logistic.score(dd[["gender", "SeniorCitizen", "Partner", "Dependents", "tenure", "PhoneService",
                              "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection",
                              "TechSupport", "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod",
                              "MonthlyCharges", "TotalCharges"]], dd['Churn'])
print(dscore)

# 회귀 분석이 가능하려면 숫자 데이터로 치환되어야 함
# 카테고리 수치화: 임의로 값 부여, 같은 카테고리에는 같은 값을!
# 카테고리 수치화 방법: One hot encoding, Label Encoding
# 라벨인코딩: 첫번째건1,두번째건2..머이렇게 - 대충,,머편한거
# 원핫인코딩: 카테고리개수만큼 숫자를늘린다 - 좀ㄷ더정교함

# 데이ㅓ를 처리하다 보면 일부 값ㅇ ㅣ없는 겨우가 잇구, 이걸 제거하거나 기본값으로 설정해
