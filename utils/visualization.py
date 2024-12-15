import matplotlib.pyplot as plt
import numpy as np

import data_processing

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def season_boxplot():
    """
    绘制箱线图
    :param data:data_day
    :return:
    """
    data_hour, data_day = data_processing.load_data()
    data = data_day
    season = ['冬季', '春季', '夏季', '秋季']
    season_data = []
    plt.figure(figsize=(7, 4.5))
    for i in range(1, 5):
        season_data.append(data.original_data[data.original_data['season'] == i]['cnt'].values)
    season_colors = ['#ADD8E6', '#90EE90', '#006400', '#FFD700']
    box = plt.boxplot(season_data, labels=season, patch_artist=True, whis=1.3, widths=0.7,
                      medianprops=dict(color='black', linewidth=1),
                      flierprops=dict(marker='o', markersize=8,markerfacecolor='red'))
    for patch, color in zip(box['boxes'], season_colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.5)
    plt.ylabel('日租凭人数', fontsize=12)
    plt.xlabel('季节', fontsize=12)
    plt.title('不同季节的日租凭人数箱线图', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.savefig('season_boxplot.png')

def month_cnt():
    """
    绘制月的租车人数
    :return:
    """
    _, data_day = data_processing.load_data()
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


month_cnt()
