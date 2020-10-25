import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

data = [[7,1], [2,1], [4,2], [9,4], [10,5], [10,6], [11,5], [11,6], [15,3], [15,2], [16,4], [16,1]]

df = pd.DataFrame(columns=['x', 'y'], data=data)

distortions = []

#클러스터 개수별 최저 거리 구하기
for cluster in range(1,10):
    km = KMeans(n_clusters=cluster).fit(df[['x', 'y']]) #1부터 10개까지 클러스터 몇 개일 때로,, 테스트를 해 보겟다??..
    #중심점과 모든 좌표들간의 거리 (N:M)
    distance = cdist(df[['x', 'y']], km.cluster_centers_, 'euclidean') #km.cluster_centers_: 중심점 #data에 있는 점과 중심점 간의 거리를 뉴클리드 디스턴스??로 구함

    #중심점-좌표간 거리 중 최저인 값
    min_distance = np.min(distance, axis=1) #np.min = 최소거리 (=중심점과 제일 가까운 점 거리)
    sum_distance = sum(min_distance) #클러스터 개수에 따른? 최소거리의 합

    #평균 최소거리의 합
    distortions.append(sum_distance / df[['x', 'y']].shape[0])

plt.plot(range(1, 10), distortions)
plt.show() #그래프가 급격하게 바뀌는 점 = 최적의 클러스터 개수