import os
import sys

import numpy as np
from PIL.features import features
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

os.environ['OMP_NUM_THREADS'] = '3'

sys.path.append('../utils')
import data_processing
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


class KMeansClustering:
    def __init__(self, data, n_clusters=3):
        self.n_clusters = n_clusters
        self.data = data.astype(np.float64)
        self.labels = None

    def fit(self):
        kmeans = KMeans(n_clusters=self.n_clusters)
        kmeans.fit(self.data)
        self.labels = kmeans.labels_
        return self.labels

    def calculate_silhouette_score(self):
        score = silhouette_score(self.data, self.labels)
        return score


def show_result(data, labels, n_clusters):
    cluster_features = np.zeros((n_clusters, 9))
    for i in range(n_clusters):
        cluster_features[i, 0] = np.bincount(data[labels == i, 0].astype(int)).argmax()
        cluster_features[i, 1] = np.bincount(data[labels == i, 2].astype(int)).argmax()
        cluster_features[i, 2] = np.bincount(data[labels == i, 3].astype(int)).argmax()
        cluster_features[i, 3] = np.bincount(data[labels == i, 4].astype(int)).argmax()
        cluster_features[i, 4] = np.bincount(data[labels == i, 5].astype(int)).argmax()
        cluster_features[i, 5] = np.bincount(data[labels == i, 6].astype(int)).argmax()
        cluster_features[i, 6] = data[labels == i, 7].mean()
        cluster_features[i, 7] = data[labels == i, 8].mean()
        cluster_features[i, 8] = data[labels == i, 12].mean()
    return cluster_features


if __name__ == '__main__':
    data_hour, data_day = data_processing.load_data()
    kmeans_clustering = KMeansClustering(data=data_day.data.values, n_clusters=3)
    scores = []
    for i in range(2, 11):
        kmeans_clustering.n_clusters = i
        kmeans_clustering.fit()
        silhouette_score1 = kmeans_clustering.calculate_silhouette_score()
        scores.append(silhouette_score1)
    kmeans_clustering.n_clusters = 3
    kmeans_clustering.fit()
    result = show_result(data_day.original_data.values, kmeans_clustering.labels, 3)
    print(result)
    mapping_0 = {1: '冬季', 2: '春季', 3: '夏季', 4: '秋季'}
    mapping_3 = {0: '非节假日', 1: '节假日'}
    mapping_4 = {0: '星期日', 1: '星期一', 2: '星期二', 3: '星期三', 4: '星期四', 5: '星期五', 6: '星期六'}
    mapping_5 = {1: '休息日', 0: '工作日'}
    mapping_6 = {1: '晴天', 2: '多云', 3: '小雨', 4: '大雨'}
    cluster_feature = []
    for i in range(3):
        features = []
        print(f'第{i + 1}类')
        print(f'季节：{mapping_0[result[i, 0].astype(int)]}')
        features.append('季节：' + mapping_0[result[i, 0].astype(int)])
        print(f'月份：{result[i, 1]}')
        features.append('月份：' + str(result[i, 1]))
        print(f'节假日：{mapping_3[result[i, 2].astype(int)]}')
        print(f'星期：{mapping_4[result[i, 3].astype(int)]}')
        features.append('星期：' + mapping_4[result[i, 3].astype(int)])
        print(f'工作日：{mapping_5[result[i, 4].astype(int)]}')
        print(f'天气：{mapping_6[result[i, 5].astype(int)]}')
        print(f'温度：{result[i, 6]}')
        features.append('温度：' + str(np.round(result[i, 6])))
        print(f'湿度：{result[i, 7]}')
        features.append('湿度：' + str(np.round(result[i, 7])))
        print(f'租车数量：{result[i, 8]}')
        features.append('租车数量：' + str(np.round(result[i, 8])))
        cluster_feature.append(features)
        print('----------------')
    print(cluster_feature)
    cluster_feature[0] = ','.join(cluster_feature[0])
    cluster_feature[1] = ','.join(cluster_feature[1])
    cluster_feature[2] = ','.join(cluster_feature[2])
    print(cluster_feature)
    plt.figure(figsize=(7, 4.5))
    plt.plot(range(2, 11), scores, 'o-')
    plt.xlabel('k', fontsize=12)
    plt.ylabel('轮廓系数', fontsize=12)
    plt.savefig('silhouette_score.png')
    data = data_day.original_data[['season', 'temp', 'cnt', 'holiday', 'weekday', 'workingday', 'weathersit']]
    data = data.values
    standard_data = StandardScaler().fit_transform(data)
    pca = PCA(n_components=2)
    data_day_pca = pca.fit_transform(standard_data)
    plt.figure(2, figsize=(7, 4.5))
    plt.scatter(data_day_pca[kmeans_clustering.labels == 0, 0], data_day_pca[kmeans_clustering.labels == 0, 1], c='r',
                label='类别1')
    plt.scatter(data_day_pca[kmeans_clustering.labels == 1, 0], data_day_pca[kmeans_clustering.labels == 1, 1], c='g',
                label='类别2')
    plt.scatter(data_day_pca[kmeans_clustering.labels == 2, 0], data_day_pca[kmeans_clustering.labels == 2, 1], c='b',
                label='类别3')
    plt.title(f'类别1特征：{cluster_feature[0]}\n类别2特征：{cluster_feature[1]}\n类别3特征：{cluster_feature[2]}'
              , fontsize=10)
    plt.xlabel('PCA1', fontsize=12)
    plt.ylabel('PCA2', fontsize=12)
    plt.savefig('PCA.png')
    plt.legend()
    plt.show()
