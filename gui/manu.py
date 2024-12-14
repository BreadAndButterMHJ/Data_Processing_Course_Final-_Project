from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QStackedWidget
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFormLayout, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("自行车租赁量分析与预测系统")
        self.setGeometry(600, 300, 1000, 600)

        # 主窗口布局
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # 增加导航栏标题以及图片
        self.label = QLabel(self.central_widget)
        self.label.setGeometry(45, 50, 200, 50)
        self.label.setText("导航栏")
        self.label.setStyleSheet("font-size: 30px;")
        self.new_buttons = []
        self.add_buttons()

    def add_buttons(self):
        # 创建数据可视化按钮
        self.button1 = QPushButton("数据可视化", self.central_widget)
        self.button1.setGeometry(25, 150, 150, 75)
        self.button1.setStyleSheet("font-size: 20px;")
        self.button1.setIcon(QIcon(r"../img/数据可视化.png"))
        self.button1.setIconSize(QSize(25, 25))
        self.button1.clicked.connect(self.data_visualization_button_show)

        # 创建聚类功能按钮
        self.button2 = QPushButton("聚类", self.central_widget)
        self.button2.setGeometry(25, 300, 150, 75)
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

    def data_visualization_button_show(self):
        self.clear_new_buttons()

        new_button1 = QPushButton("季节租凭人数箱线图", self.central_widget)
        new_button1.setGeometry(225, 20, 130, 40)
        new_button1.setStyleSheet("font-size: 12px;")
        self.new_buttons.append(new_button1)

        new_button2 = QPushButton("新按钮2", self.central_widget)
        new_button2.setGeometry(380, 20, 130, 40)
        new_button2.setStyleSheet("font-size: 12px;")
        self.new_buttons.append(new_button2)

        new_button3 = QPushButton("新按钮3", self.central_widget)
        new_button3.setGeometry(535, 20, 130, 40)
        new_button3.setStyleSheet("font-size: 12px;")
        self.new_buttons.append(new_button3)

        new_button4 = QPushButton("新按钮4", self.central_widget)
        new_button4.setGeometry(690, 20, 130, 40)
        new_button4.setStyleSheet("font-size: 12px;")
        self.new_buttons.append(new_button4)

        new_button5 = QPushButton("新按钮5", self.central_widget)
        new_button5.setGeometry(845, 20, 130, 40)
        new_button5.setStyleSheet("font-size: 12px;")
        self.new_buttons.append(new_button5)

        for button in self.new_buttons:
            button.show()


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
        self.input_field_temp.setGeometry(270, 200, 300, 40)
        self.input_field_temp.setPlaceholderText("请输入温度")
        self.input_field_temp.setStyleSheet("font-size: 14px;")
        self.new_buttons.append(self.input_field_temp)

        self.input_field_hum = QLineEdit(self.central_widget)
        self.input_field_hum.setGeometry(270, 300, 300, 40)
        self.input_field_hum.setPlaceholderText("请输入湿度")
        self.input_field_hum.setStyleSheet("font-size: 14px;")
        self.new_buttons.append(self.input_field_hum)

        # Create a button to trigger the output
        self.output_button = QPushButton("输出", self.central_widget)
        self.output_button.setGeometry(270, 70, 300, 40)
        self.output_button.setStyleSheet("font-size: 14px;")
        self.output_button.clicked.connect(self.perform_output)
        self.new_buttons.append(self.output_button)

        for button in self.new_buttons:
            button.show()

    def perform_output(self):
        print("输出")
        print(self.input_field_temp.text())
        print(self.input_field_hum.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
