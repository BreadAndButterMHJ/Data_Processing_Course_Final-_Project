import sys
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.preprocessing import MinMaxScaler
sys.path.append('../utils')
import data_processing as dp

class TimeSequence():
    def __init__(self,data_hour):
        self.data = data_hour.original_data.values[:17378, [3, 8]]
        self.target = data_hour.original_data.values[1:, 8]
        self.scaler = MinMaxScaler()
        self.data = self.scaler.fit_transform(self.data)
        self.model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1, max_depth=5)
        self.model.fit(self.data, self.target)

    def predict(self, time, temp):
        temp_pre = []
        for i in range(24):
            data_pre = np.array([[time, temp]]).reshape(1, -1)
            data_pre = self.scaler.transform(data_pre)
            new_temp = self.model.predict(data_pre)[0]
            temp_pre.append(new_temp)
            time += 1
            if time == 24:
                time = 0
            temp = new_temp
        return temp_pre

if __name__ == '__main__':
    data_hour, data_day = dp.load_data()
    ts = TimeSequence(data_hour)
    print(ts.predict(9, 12))

