import logging
import sys
from PyQt6.QtCore import pyqtSignal, pyqtBoundSignal
from PyQt6.QtWidgets import QApplication, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget
class UI(QWidget):
    update_log_text_signal=pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.logger=logging.getLogger()
        handler=QLogger(parent=self,update_log_text_signal=self.update_log_text_signal)
        self.update_log_text_signal.connect(handler.widget.appendPlainText)
        handler.widget.textChanged.connect(handler.scroll_widget_to_bottom)
        self.logger.setLevel(logging.INFO)
        # Here set the log level you want
        handler.setFormatter(logging.Formatter(fmt="%(asctime)s-%(levelname)s-%(message)s",datefmt="%Y-%m-%d %H:%M:%S"))
        self.logger.addHandler(handler)
        button=QPushButton("&Test")
        button.clicked.connect(self.button_handler)
        button.setDefault(True)
        layout_=QVBoxLayout()
        layout_.addWidget(handler.widget)
        layout_.addWidget(button)
        self.setLayout(layout_)
    def button_handler(self):
        self.logger.debug("This is a debug message")
        self.logger.info("This is an info message")
        self.logger.warning("This is a warning message")
        self.logger.error("This is an error message")
        self.logger.critical("This is a critical message")
        

class QLogger(logging.Handler):
    def __init__(self,parent:QWidget,update_log_text_signal:pyqtBoundSignal):
        super().__init__()
        self.widget=QPlainTextEdit(parent=parent)
        self.widget.setReadOnly(True)
        self.update_log_text_signal=update_log_text_signal
    def emit(self,record:logging.LogRecord):
        msg=self.format(record=record)
        self.update_log_text_signal.emit(msg)
    def scroll_widget_to_bottom(self):
        self.widget.verticalScrollBar().setSliderPosition(self.widget.verticalScrollBar().maximum())
if __name__=="__main__":
    app=QApplication(sys.argv)
    ui=UI()
    ui.show()
    sys.exit(app.exec())