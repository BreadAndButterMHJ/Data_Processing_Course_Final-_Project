import sys

import matplotlib.pyplot as plt

sys.path.append('../utils')
import data_processing as dp
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import xgboost as xgb
import time_sequence

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

"""
    预测基于月份，时间，是否是工作日，温度
"""


class PredictCnt():
    def __init__(self):
        self.scaler = MinMaxScaler()
        data_hour, data_day = dp.load_data()
        self.time_model = time_sequence.TimeSequence(data_hour)
        data = data_hour.original_data.values
        data = data[:, [2, 3, 6, 8]]
        self.scaler.fit(data[:, [0, 1, 3]])
        data[:, [0, 1, 3]] = self.scaler.transform(data[:, [0, 1, 3]])
        target = data_hour.original_data['cnt'].values
        self.model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1, max_depth=5)
        self.model.fit(data, target)

    def predict(self, month, time, is_workday, temp):
        temp = self.time_model.predict(time, temp)
        data_pre = np.zeros((24, 4))
        data_pre[:, 0] = month
        data_pre[:, 1] = np.array([time + i for i in range(24)]) % 24
        data_pre[:, 2] = is_workday
        data_pre[:, 3] = temp
        data_pre[:, [0, 1, 3]] = self.scaler.transform(data_pre[:, [0, 1, 3]])
        plt.figure(1, figsize=(7, 4.5))
        pre = self.model.predict(data_pre)
        time_label = np.array([i for i in range(24)])
        plt.plot(time_label, pre, 'r', label='predict')
        plt.xlabel('时间', fontsize=12)
        plt.ylabel('租凭人数', fontsize=12)
        plt.xticks(time_label[::2], labels=[f"{(time + i) % 24}:00" for i in range(0, 24, 2)])
        plt.legend()
        plt.title('预测租凭人数')
        plt.savefig('../img/predict_cnt.png')
        return pre


if __name__ == '__main__':
    pc = PredictCnt()
    print(pc.predict(1, 9, 1, 12))
