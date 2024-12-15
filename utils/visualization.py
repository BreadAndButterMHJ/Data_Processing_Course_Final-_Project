import matplotlib.pyplot as plt
import numpy as np

import data_processing

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def season_boxplot(data):
    """
    绘制箱线图
    :param data:data_day
    :return:
    """
    season = ['冬季', '春季', '夏季', '秋季']
    season_data = []
    plt.figure(figsize=(7, 4.5))
    for i in range(1, 5):
        season_data.append(data.original_data[data.original_data['season'] == i]['cnt'].values)
    season_colors = ['#ADD8E6', '#90EE90', '#006400', '#FFD700']
    box = plt.boxplot(season_data, labels=season, patch_artist=True, whis=1.3, widths=0.7,
                      medianprops=dict(color='black', linewidth=1),
                      flierprops=dict(marker='o', markersize=8, markerfacecolor='red'))
    for patch, color in zip(box['boxes'], season_colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.5)
    plt.ylabel('日租凭人数', fontsize=12)
    plt.xlabel('季节', fontsize=12)
    plt.title('不同季节的日租凭人数箱线图', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.savefig('season_boxplot.png')


def month_cnt(data_day):
    """
    绘制月的租车人数
    :return:
    """
    month = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
    month_cnt = []
    for i in range(1, 13):
        month_cnt.append(np.sum(data_day.original_data[data_day.original_data['mnth'] == i]['cnt'].values))
    month_casual = []
    month_registered = []
    rate = []
    for i in range(1, 13):
        month_casual.append(np.sum(data_day.original_data[data_day.original_data['mnth'] == i]['casual'].values))
        month_registered.append(month_cnt[i - 1] - month_casual[i - 1])
        rate.append(month_casual[i - 1] / month_cnt[i - 1])
    fig, ax1 = plt.subplots(figsize=(7, 4.5))
    ax1.plot(month, month_cnt, marker='o', label='总租车人数')
    ax1.plot(month, month_casual, marker='o', label='临时租车人数')
    ax1.plot(month, month_registered, marker='o', label='注册租车人数')
    ax1.set_ylabel('租车人数', fontsize=12)
    ax1.set_xlabel('月份', fontsize=12)
    ax1.set_title('不同月份的租车人数和临时租车人数占比', fontsize=14)
    ax1.tick_params(axis='both', labelsize=12)
    ax1.legend(loc='upper left')

    ax2 = ax1.twinx()
    ax2.plot(month, rate, marker='o', color='r', label='临时租车人数占比')
    ax2.set_ylabel('临时租车人数占比', fontsize=12)
    ax2.tick_params(axis='y', labelsize=12)
    ax2.legend(loc='upper right')

    fig.tight_layout()
    plt.savefig('month_cnt_with_rate.png')


def hour_month_heatmap(data):
    """
    绘制小时-月份热力图
    :return:
    """
    hour_month = np.zeros((12, 12))
    for i in range(1, 13):
        for j in range(12):
            hour_month[i - 1, j] = (np.sum(
                data.original_data[(data.original_data['hr'] == 2 * j) & (data.original_data['mnth'] == i)][
                    'cnt'].values) + data.original_data[
                                        (data.original_data['hr'] == 2 * j + 1) & (data.original_data['mnth'] == i)][
                                        'cnt'].values[0])
    hour_month = hour_month[::-1]
    plt.figure(figsize=(7, 4.5))
    plt.imshow(hour_month, cmap='hot', interpolation='nearest')
    colorbar = plt.colorbar()
    colorbar.set_label('该时间节点总租凭人数', rotation=90)
    plt.xlabel('月份', fontsize=12)
    plt.ylabel('小时', fontsize=12)
    plt.title('不同小时-月份的租车人数热力图', fontsize=14)
    plt.xticks(range(12), [str(i) + '月' for i in range(1, 13)], fontsize=12)
    plt.yticks(range(12), [str(i * 2) + '时' for i in range(12)][::-1], fontsize=12)
    plt.savefig('hour_month_heatmap.png')


def day_plot(data):
    """
    绘制全年日租凭人数变化
    weathersit :
		- 1: Clear, Few clouds, Partly cloudy, Partly cloudy
		- 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
		- 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
		- 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
    :param data:
    :return:
    """
    cnt_1 = data.original_data[data.original_data['yr'] == 0]['cnt'].values
    cnt_2 = data.original_data[data.original_data['yr'] == 1]['cnt'].values
    # 去除2012年2月29日的数据
    cnt_2 = np.concatenate((cnt_2[:59], cnt_2[60:]))
    cnt = (cnt_1 + cnt_2) / 2
    plt.figure(figsize=(7, 4.5))
    plt.plot(cnt)
    plt.xlabel('月份', fontsize=12)
    plt.ylabel('日租凭人数', fontsize=12)
    plt.title('全年日租凭人数变化', fontsize=14)
    month = [15, 44, 72, 103, 133, 164, 194, 225, 256, 286, 317, 347]
    plt.xticks(month, [str(i) + '月' for i in range(1, 13)], fontsize=12)
    plt.yticks(fontsize=12)
    plt.savefig('day_plot.png')


def holiday_workingday_weathersit(data_day):
    """
    绘制出节假日，工作日，休息日，天气情况的平均租凭人数
    weathersit :
		- 1: Clear, Few clouds, Partly cloudy, Partly cloudy
		- 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
		- 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
    :param data_day:
    :return:
    """
    y = []
    x = ['晴天', '多云', '小雨']
    for i in range(1, 4):
        y.append(np.mean(data_day.original_data[data_day.original_data['weathersit'] == i]['cnt'].values))
    y.append(np.mean(data_day.original_data[data_day.original_data['holiday'] == 1]['cnt'].values))
    y.append(np.mean(data_day.original_data[data_day.original_data['workingday'] == 1]['cnt'].values))
    y.append(np.mean(data_day.original_data[data_day.original_data['workingday'] == 0]['cnt'].values))
    x.append('节假日')
    x.append('工作日')
    x.append('休息日')
    plt.figure(figsize=(7, 4.5))
    plt.bar(x, y, color=['#ADD8E6', '#90EE90', '#006400', '#FFD700', '#FF6347', '#FFA500', '#FF4500'])
    plt.xlabel('天气情况/工作状态', fontsize=12)
    plt.ylabel('平均租凭人数', fontsize=12)
    plt.title('不同天气情况/工作状态的平均租凭人数', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.savefig('holiday_workingday_weathersit.png')

def windspeed_temp_hum_cnt_relation(data_day):
    """
    绘制风速、温度、湿度与租车人数的r值的热力图
    :param data_day:
    :return:
    """
    windspeed = data_day.original_data['windspeed'].values
    temp = data_day.original_data['temp'].values
    hum = data_day.original_data['hum'].values
    cnt = data_day.original_data['cnt'].values
    sample = np.vstack((windspeed, temp, hum, cnt))
    r = np.corrcoef(sample)
    plt.figure(figsize=(7, 4.5))
    plt.imshow(r, cmap='viridis', interpolation='nearest')
    colorbar = plt.colorbar()
    colorbar.set_label('r值', rotation=90)
    plt.xlabel('风速、温度、湿度、租凭人数', fontsize=12)
    plt.ylabel('风速、温度、湿度、租凭人数', fontsize=12)
    plt.title('风速、温度、湿度与租车人数的r值热力图', fontsize=14)
    plt.xticks(range(4), ['风速', '温度', '湿度', '租凭人数'], fontsize=12)
    plt.yticks(range(4), ['风速', '温度', '湿度', '租凭人数'], fontsize=12)
    # 标注具体数值
    for i in range(4):
        for j in range(4):
            plt.text(i, j, round(r[i, j], 2), ha='center', va='center', color='red', fontsize=12)
    plt.savefig('windspeed_temp_hum_cnt_relation.png')




if __name__ == '__main__':
    data_hour, data_day = data_processing.load_data()
    windspeed_temp_hum_cnt_relation(data_day)
