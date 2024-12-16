import pandas as pd

pd.set_option('display.max_columns', 100)


class MyData():
    def __init__(self, file_path):
        """
        这里我要去掉一些不需要的特征，去除dteday，instant ，yr，atemp，casual，registered
        yr这个特征是年份，我们只有两年的数据，所以这个特征对我们的预测没有帮助
        instant是每一行的编号，对我们的预测没有帮助
        去除temp是因为temp和atemp是高度相关的，去除casual和registered是因为我们要预测的是cnt
        """
        self.data = pd.read_csv(file_path)
        self.data = self.data.drop(['dteday', 'instant', 'atemp'], axis=1)
        self.original_data = self.data.copy()
        self.data = self.data.drop(['casual', 'registered', 'yr'], axis=1)
        self.data_temp_max = 39
        self.data_temp_min = -8
        self.data_windspeed_max = 67
        self.data_hum_max = 100
        self.original_data = self.data_denormalization(self.original_data)
        self.data = self.feature_engineering(self.data)

    def data_denormalization(self, data):
        data['temp'] = data['temp'] * (self.data_temp_max - self.data_temp_min) + self.data_temp_min
        data['windspeed'] = data['windspeed'] * self.data_windspeed_max
        data['hum'] = data['hum'] * self.data_hum_max
        return data

    def data_normalization(self, data):
        data['atemp'] = (data['atemp'] - self.data_temp_min) / (self.data_temp_max - self.data_temp_min)
        data['windspeed'] = data['windspeed'] / self.data_windspeed_max
        data['hum'] = data['hum'] / self.data_hum_max
        return data

    def feature_engineering(self, data):
        """
        这里我们对特征进行处理，我们对weekday，mnth，weathersit进行one-hot编码
        对atemp，windspeed，hum进行新的标准化
        """
        data = pd.get_dummies(data, columns=['weekday', 'mnth', 'weathersit', 'season'])
        data['holiday'] = data['holiday'].astype('bool')
        data['workingday'] = data['workingday'].astype('bool')
        return data

    def __str__(self):
        print('original_data shape:', self.original_data.shape, sep='\n')
        print('original_data:', self.original_data.head(), sep='\n')
        print('data shape:', self.data.shape, sep='\n')
        print('data:', self.data.head(), sep='\n')
        return ''


def load_data():
    """
    加载数据
    :return:data_hour, data_day
    """
    data_hour = MyData('../data/hour.csv')
    data_day = MyData('../data/day.csv')
    return data_hour, data_day


if __name__ == '__main__':
    data_hour, data_day = load_data()
    print(data_day)
