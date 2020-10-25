# 식별: 과거의 정보를 근거로 현 상황을 봄
#  - 다음에 해야 하는 동작을 생각
#
# 식별을 사용하는 방법
# 1. Clustering
# 먼저 뭉침(평균적으로 나랑 가까운 걸 찾아냄)
# 2. Classification
# 라벨을 먼저 함
###########지금은 clustering!!###########

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
import seaborn as sns

df = pd.read_csv('cluster_sample_1.csv')
#plt.scatter(df[['x']], df[['y']])  #이게 데이터 보는 방법인듯???
#plt.show()

distortions = []

for cluster in range(1,20):
    km = KMeans(n_clusters=cluster).fit(df[['x', 'y']]) #1부터 10개까지 클러스터 몇 개일 때로,, 테스트를 해 보겟다??..
    #중심점과 모든 좌표들간의 거리 (N:M)
    distance = cdist(df[['x', 'y']], km.cluster_centers_, 'euclidean') #km.cluster_centers_: 중심점 #data에 있는 점과 중심점 간의 거리를 뉴클리드 디스턴스??로 구함

    #중심점-좌표간 거리 중 최저인 값
    min_distance = np.min(distance, axis=1) #np.min = 최소거리 (=중심점과 제일 가까운 점 거리)
    sum_distance = sum(min_distance) #클러스터 개수에 따른? 최소거리의 합

    #평균 최소거리의 합
    distortions.append(sum_distance / df[['x', 'y']].shape[0])


# plt.plot(range(1, 20), distortions)
# plt.show() #15개일때최적



# km = KMeans(n_clusters=15).fit(df[['x', 'y']]) #데이터 clustering
# df['cluster_id'] = km.labels_
# sns.lmplot('x', 'y', data=df, hue='cluster_id', fit_reg=False) #기준: 거리
# plt.show()

#데이터가 n개일 때 클러스터는 1~n개
#차트로 확인하는데(클러스터의 개수에 대한 오차 그래프) 그게 꺾이는 게 최적ㅇ.,.몰라!!



