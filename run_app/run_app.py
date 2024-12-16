import sys

sys.path.append(r'../data')
sys.path.append(r'../gui')
sys.path.append(r'../utils')
sys.path.append(r'../img')
sys.path.append(r'../models')

import manu
import data_processing
from PyQt5.QtWidgets import QApplication

data_hour, data_day = data_processing.load_data()
app = QApplication(sys.argv)
window = manu.MainWindow(data_hour, data_day)
window.show()
sys.exit(app.exec_())
