import matplotlib.pyplot as plt
from scipy.stats import alpha
from stack_data import markers_from_ranges

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
    plt.figure(figsize=(8, 5))
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


season_boxplot()
