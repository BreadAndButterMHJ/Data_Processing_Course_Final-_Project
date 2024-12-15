import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QComboBox
from PyQt5.QtWidgets import QLineEdit

sys.path.append("../utils")
import visualization
import data_processing


class MainWindow(QMainWindow):
    def __init__(self, data_hour, data_day):
        super().__init__()
        self.setWindowTitle("自行车租赁量分析与预测系统")
        self.setGeometry(600, 300, 1000, 600)
        self.data_hour = data_hour
        self.data_day = data_day

        # 主窗口布局
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.background_image_label = QLabel(self.central_widget)
        self.background_image_label.setGeometry(0, 0, 1000, 600)  # 设置额外图片显示位置和大小
        self.background_image_label.setPixmap(QPixmap(r"../img/backgroud.png"))  # 加载并显示额外图片
        self.background_image_label.show()

        self.new_buttons = []
        self.img_label = []
        self.add_buttons()

    def add_buttons(self):
        # 创建数据可视化按钮
        self.button1 = QPushButton("数据可视化", self.central_widget)
        self.button1.setGeometry(25, 250, 150, 75)
        self.button1.setStyleSheet("font-size: 20px;")
        self.button1.setIcon(QIcon(r"../img/数据可视化.png"))
        self.button1.setIconSize(QSize(25, 25))
        self.button1.clicked.connect(self.data_visualization_button_show)

        # 创建聚类功能按钮
        self.button2 = QPushButton("聚类", self.central_widget)
        self.button2.setGeometry(25, 350, 150, 75)
        self.button2.setStyleSheet("font-size: 20px;")
        self.button2.setIcon(QIcon(r"../img/聚类.png"))
        self.button2.setIconSize(QSize(25, 25))
        self.button2.clicked.connect(self.clustering_button_show)

        # 创建预测按钮
        self.button3 = QPushButton("预测租凭量", self.central_widget)
        self.button3.setGeometry(25, 450, 150, 75)
        self.button3.setStyleSheet("font-size: 20px;")
        self.button3.setIcon(QIcon("../img/销量预测.png"))
        self.button3.setIconSize(QSize(25, 25))
        self.button3.clicked.connect(self.prediction_button_show)

    def clear_new_buttons(self):
        for button in self.new_buttons:
            button.deleteLater()
        self.new_buttons.clear()

    def clear_img_label(self):
        for label in self.img_label:
            label.deleteLater()
        self.img_label.clear()

    def data_visualization_button_show(self):
        self.clear_new_buttons()

        new_button1 = QPushButton("季节租凭人数箱线图", self.central_widget)
        new_button1.setGeometry(225, 20, 130, 40)
        new_button1.setStyleSheet("font-size: 12px;")
        new_button1.clicked.connect(self.show_data_visualization_button1)
        self.new_buttons.append(new_button1)

        new_button2 = QPushButton("月份租凭人数折线图", self.central_widget)
        new_button2.setGeometry(380, 20, 130, 40)
        new_button2.setStyleSheet("font-size: 12px;")
        new_button2.clicked.connect(self.show_data_visualization_button2)
        self.new_buttons.append(new_button2)

        new_button3 = QPushButton("月份时间人数热力图", self.central_widget)
        new_button3.setGeometry(535, 20, 130, 40)
        new_button3.setStyleSheet("font-size: 12px;")
        new_button3.clicked.connect(self.show_data_visualization_button3)
        self.new_buttons.append(new_button3)

        new_button4 = QPushButton("天气情况节假日人数", self.central_widget)
        new_button4.setGeometry(690, 20, 130, 40)
        new_button4.setStyleSheet("font-size: 12px;")
        new_button4.clicked.connect(self.show_data_visualization_button4)
        self.new_buttons.append(new_button4)

        new_button5 = QPushButton("天气参数租凭人数R值", self.central_widget)
        new_button5.setGeometry(845, 20, 130, 40)
        new_button5.clicked.connect(self.show_data_visualization_button5)
        new_button5.setStyleSheet("font-size: 12px;")
        self.new_buttons.append(new_button5)

        for button in self.new_buttons:
            button.show()

    def show_data_visualization_button1(self):
        self.clear_img_label()
        image_label = QLabel(self.central_widget)
        image_label.setGeometry(250, 125, 700, 450)
        image_label.setPixmap(QPixmap(r"season_boxplot.png"))
        self.img_label.append(image_label)
        image_label.show()

    def show_data_visualization_button2(self):
        self.clear_img_label()
        image_label = QLabel(self.central_widget)
        image_label.setGeometry(250, 125, 700, 450)
        image_label.setPixmap(QPixmap(r"month_cnt_with_rate.png"))
        self.img_label.append(image_label)
        image_label.show()

    def show_data_visualization_button3(self):
        self.clear_img_label()
        image_label = QLabel(self.central_widget)
        image_label.setGeometry(250, 125, 700, 450)
        visualization.hour_month_heatmap(self.data_hour)
        image_label.setPixmap(QPixmap(r"hour_month_heatmap.png"))
        self.img_label.append(image_label)
        image_label.show()

    def show_data_visualization_button4(self):
        self.clear_img_label()
        image_label = QLabel(self.central_widget)
        image_label.setGeometry(250, 125, 700, 450)
        visualization.holiday_workingday_weathersit(self.data_day)
        image_label.setPixmap(QPixmap(r"holiday_workingday_weathersit.png"))
        self.img_label.append(image_label)
        image_label.show()

    def show_data_visualization_button5(self):
        self.clear_img_label()
        image_label = QLabel(self.central_widget)
        image_label.setGeometry(250, 125, 700, 450)
        visualization.windspeed_temp_hum_cnt_relation(self.data_day)
        image_label.setPixmap(QPixmap(r"windspeed_temp_hum_cnt_relation.png"))
        self.img_label.append(image_label)
        image_label.show()

    def clustering_button_show(self):
        self.clear_new_buttons()
        new_button1 = QPushButton("Kmeans聚类结果图", self.central_widget)
        new_button1.setGeometry(270, 20, 300, 40)
        new_button1.setStyleSheet("font-size: 14px;")
        self.new_buttons.append(new_button1)

        new_button2 = QPushButton("DBSCAN聚类结果图", self.central_widget)
        new_button2.setGeometry(640, 20, 300, 40)
        new_button2.setStyleSheet("font-size: 14px;")
        self.new_buttons.append(new_button2)

        for button in self.new_buttons:
            button.show()

    def prediction_button_show(self):
        self.clear_new_buttons()

        self.input_field_temp = QLineEdit(self.central_widget)
        self.input_field_temp.setGeometry(220, 20, 105, 40)
        self.input_field_temp.setStyleSheet("font-size: 14px;")
        self.new_buttons.append(self.input_field_temp)
        label = QLabel("温度（例：0.5）", self.central_widget)
        label.setGeometry(220, 60, 105, 40)
        label.setStyleSheet("font-size: 14px;")
        self.new_buttons.append(label)

        self.input_field_hum = QLineEdit(self.central_widget)
        self.input_field_hum.setGeometry(345, 20, 105, 40)
        self.input_field_hum.setStyleSheet("font-size: 14px;")
        self.new_buttons.append(self.input_field_hum)
        label1 = QLabel("湿度（例：0.85）", self.central_widget)
        label1.setGeometry(345, 60, 105, 40)
        label1.setStyleSheet("font-size: 14px;")
        self.new_buttons.append(label1)

        self.input_field_windspeed = QLineEdit(self.central_widget)
        self.input_field_windspeed.setGeometry(470, 20, 105, 40)
        self.input_field_windspeed.setStyleSheet("font-size: 14px;")
        self.new_buttons.append(self.input_field_windspeed)
        label2 = QLabel("风速（例：0.5）", self.central_widget)
        label2.setGeometry(470, 60, 105, 40)
        label2.setStyleSheet("font-size: 14px;")
        self.new_buttons.append(label2)

        self.input_field_workingday = QComboBox(self.central_widget)
        self.input_field_workingday.setGeometry(595, 20, 105, 40)
        self.input_field_workingday.addItems(["是", "否"])
        self.input_field_workingday.setStyleSheet("font-size: 14px;")
        self.new_buttons.append(self.input_field_workingday)
        label3 = QLabel("是否工作日", self.central_widget)
        label3.setGeometry(595, 60, 105, 40)
        label3.setStyleSheet("font-size: 14px;")
        self.new_buttons.append(label3)

        self.input_field_time = QComboBox(self.central_widget)
        self.input_field_time.setGeometry(720, 20, 105, 40)
        self.input_field_time.addItems([str(time) + ':00' for time in range(24)])
        self.input_field_time.setStyleSheet("font-size: 14px;")
        self.new_buttons.append(self.input_field_time)
        label4 = QLabel("时间", self.central_widget)
        label4.setGeometry(720, 60, 105, 40)
        label4.setStyleSheet("font-size: 14px;")
        self.new_buttons.append(label4)

        self.input_field_month = QComboBox(self.central_widget)
        self.input_field_month.setGeometry(845, 20, 105, 40)
        self.input_field_month.setPlaceholderText("月份")
        self.input_field_month.setStyleSheet("font-size: 14px;")
        self.input_field_month.addItems([str(month) + '月' for month in range(1, 13)])
        self.new_buttons.append(self.input_field_month)
        label5 = QLabel("月份", self.central_widget)
        label5.setGeometry(845, 60, 105, 40)
        label5.setStyleSheet("font-size: 14px;")
        self.new_buttons.append(label5)

        self.output_button = QPushButton("输出24小时租凭量变化", self.central_widget)
        self.output_button.setGeometry(30, 20, 150, 40)
        self.output_button.setStyleSheet("font-size: 14px;")
        self.output_button.clicked.connect(self.perform_output)
        self.new_buttons.append(self.output_button)

        for button in self.new_buttons:
            button.show()

    def perform_output(self):
        print("输出")
        print(self.input_field_temp.text())
        print(self.input_field_hum.text())
        print(self.input_field_windspeed.text())
        print(self.input_field_workingday.currentText())
        print(self.input_field_time.currentText())
        print(self.input_field_month.currentText())


if __name__ == "__main__":
    data_hour, data_day = data_processing.load_data()
    app = QApplication(sys.argv)
    window = MainWindow(data_hour, data_day)
    window.show()
    sys.exit(app.exec_())
