import pandas as pd

pd.set_option('display.max_columns', 100)


def load_data(file_path):
    return pd.read_csv(file_path)


def data_preprocessing(data):
    """
    这里我要去掉一些不需要的特征，去除dteday，instant ，yr，temp，casual，registered
    yr这个特征是年份，我们只有两年的数据，所以这个特征对我们的预测没有帮助
    instant是每一行的编号，对我们的预测没有帮助
    去除temp是因为temp和atemp是高度相关的，去除casual和registered是因为我们要预测的是cnt
    """
    data = data.drop(['dteday', 'instant', 'yr', 'temp', 'casual', 'registered'], axis=1)
    return data


def feature_engineering(data):
    """
    这里我们对特征进行处理，我们对weekday，mnth，weathersit进行one-hot编码
    对atemp，windspeed，hum进行新的标准化
    """
    data = pd.get_dummies(data, columns=['weekday', 'mnth', 'weathersit'])
    return data


data = load_data('../data/hour.csv')
data1 = load_data('../data/day.csv')
data_processed = data_preprocessing(data)
data_processed = feature_engineering(data_processed)
data1_processed = data_preprocessing(data1)
data1_processed = feature_engineering(data1_processed)
data_processed.to_csv('../data/hour_processed.csv', index=False)
data1_processed.to_csv('../data/day_processed.csv', index=False)
