# 自行车租赁量分析与预测系统

该项目主要是我的数据处理课程的期末项目，这里写一个readme文件主要是熟悉github的使用，之后也希望能通过这个readme写一下我的期末报告。

我采用的数据集是:[Bike Sharing Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)

数据集说明:[Readme.txt](data/Readme.txt)

系统提供以下主要功能模块：


1. **GUI 界面制作**：  
   直观易用的图形化界面，用户可在其中查看数据、选择参数进行预测，并查看聚类结果。

2. **数据信息展示**：  
   多种可视化图表（包括箱线图、热力图、折线图、散点图、相关性热力图等）帮助用户直观了解租赁量随时间、天气、季节变化的规律。

3. **预测模块**：  
   使用 XGBoost 模型对未来24小时的租赁量进行预测。用户可输入特定天气条件和时间信息，即可获取预测结果。

4. **聚类模块**：  
   对数据进行聚类分析，帮助发现相似的租赁模式（如特定天气和时间条件下的高峰类群）。

---

## 功能模块概述

### GUI 界面
- 实现一个简单易用的用户界面（如使用 PyQt5 或 Tkinter）。  
- 提供导航菜单，在“数据展示”、“预测”、“聚类结果”界面之间切换。  
- 用户可通过图形化控件选择时间、季节和天气数据，并查看相应的统计图和预测结果。

### 数据信息展示
- **箱线图（Box Plot）**：展示不同季节的租赁量分布，了解中位数、分布范围及异常值。  
- **季节-小时热力图（Heatmap）**：展示各季节各小时平均租赁量分布，一目了然把握周期性规律。  
- **折线图（Line Chart）**：展示租赁量随日期变化的趋势。  
- **直方图 / KDE图**：展示在不同气象条件（如温度）下的租赁量分布。  
- **散点图（Scatter Plot）**：展示温度、湿度等环境变量与租赁量之间的关系。  
- **相关性热力图（Correlation Heatmap）**：展示天气特征与租赁量的相关关系。

### 预测模块
- 使用 XGBoost 进行回归预测。  
- 输入：当日的天气参数（温度、湿度、风速、天气类型）及时间信息。  
- 输出：未来24小时的租赁量预测值。  
- 模型训练时包括数据清洗、特征工程（如标准化、类别编码）、参数调优和交叉验证。

### 聚类模块
- 使用 K-Means 或层次聚类对数据进行分群。  
- 按小时（或天）为粒度，使用天气、时间特征和租赁量进行聚类。  
- 可通过 GUI 展示各聚类类中心特征，以帮助用户理解相似模式的分组。
  
目前正在编写代码中，放个三鹰，提高一下我的编程热情。

![鹰鹰鹰](img/鹰鹰鹰.jpg)
