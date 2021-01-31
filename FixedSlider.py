# QSlider with a label to show its value.
# PyQt6 version.
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QSlider, QLabel
class FixedSlider(QSlider):
    def __init__(self):
        super(FixedSlider,self).__init__()
        self.setTickInterval(1)
        self.value_label=QLabel(self)    
        self.value_label.setFixedSize(40,20) 
        self.value_label.setAutoFillBackground(True)
        self.value_label.setStyleSheet("QLabel{background:transparent;font:8px}")
        self.value_label.setAlignment(Qt.Alignment.AlignCenter)
        self.value_label.setVisible(False)
        self.value_label.move(0,-5)
    def mousePressEvent(self,event:QMouseEvent):
        super(FixedSlider,self).mousePressEvent(event)
        if self.value_label.isVisible()==False:
            self.value_label.setVisible(True)
            self.value_label.setText(str(self.value()/10))
    def mouseMoveEvent(self,event:QMouseEvent):
        super(FixedSlider,self).mouseMoveEvent(event)
        self.value_label.setText(str(self.value()/10))
        self.value_label.move(int((self.width()-self.value_label.width())*self.value()/(self.maximum()-self.minimum())),-5)
    def mouseReleaseEvent(self,event:QMouseEvent):
        super(FixedSlider,self).mouseReleaseEvent(event)
        if self.value_label.isVisible()==True:
            self.value_label.setVisible(False)
