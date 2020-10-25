import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns

df = pd.read_csv('fruit_data_with_colors.csv')
label_count = len(df['fruit_name'].unique())
# sns.lmplot('mass', 'width', 'height', 'color_score', data= df, hue= 'fruit_name', fit_reg=False)
# plt.show()

train = df.sample(frac=0.8, random_state=200)
test = df.drop(train.index)

knn = KNeighborsClassifier(n_neighbors=label_count)
knn.fit(train[['mass', 'width', 'height', 'color_score']], train['fruit_label'])
score = knn.score(test[['mass', 'width', 'height', 'color_score']], test['fruit_label'])
#print(score)

guess = pd.DataFrame(columns=['mass', 'width', 'height', 'color_score'])
guess.loc[0] = [192,8.4,7.3,0.55]  #평균치를찾는것이므로 예측이틀릴수있다
print(knn.predict(guess))

# 아웃라이어 데이터들이 있는 경우
# 평균에 크게 영향ㅇ을 줘 올바른 식별이 안 됨

# 확률적인 모델로 바꾸기 필요하다!!
#  --- 이게 로지스틱 회귀




