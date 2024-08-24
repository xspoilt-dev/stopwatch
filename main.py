import sys
import time
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_ui import Ui_MainWindow


class StopWatch(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        
        self.elapsed_time = 0
        self.running = False
        
        self.ui.pushButton.clicked.connect(self.start_stopwatch)
        self.ui.pushButton_2.clicked.connect(self.stop_stopwatch)
        
    def start_stopwatch(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.timer.start(1000)  # Update every second
            self.running = True
            
    def stop_stopwatch(self):
        if self.running:
            self.timer.stop()
            self.elapsed_time = time.time() - self.start_time
            self.running = False
            
    def update_time(self):
        elapsed = time.time() - self.start_time
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed))
        self.ui.label.setText(formatted_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    sys.exit(app.exec_())

