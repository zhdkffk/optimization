import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

data = [[7,1], [2,1], [4,2], [9,4], [10,5], [10,6], [11,5], [11,6], [15,3], [15,2], [16,4], [16,1]]

df = pd.DataFrame(columns=['x', 'y'], data=data)
km = KMeans(n_clusters=3).fit(df[['x', 'y']])

df['cluster_id'] = km.labels_

sns.lmplot('x', 'y', data=df, hue='cluster_id', fit_reg=False) #기준: 거리
plt.show()

#클러스터의 개수는? 1~n개, 최적 개수: 차트로 짐작, 최적의 수치 계산