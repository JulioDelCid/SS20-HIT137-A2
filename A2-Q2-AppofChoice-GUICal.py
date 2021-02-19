# Assigment:        Question 2b - Create a program of your choice
# Contributors:     Julio Del Cid studentid 332808
# GITHUB Repo:      https://github.com/JulioDelCid/SS20-HIT137-A2/ 
#
#
#############       Commence assignmet code ##############################
#
#
# Insert pyside2 library to enable a GUI interface needed for the calendar features
# The Q represents the Qt framework tools, https://www.qt.io/ 
from PySide2.QtWidgets import QApplication, QCalendarWidget, QWidget, QVBoxLayout
import sys
from PySide2.QtGui import QIcon
 
#defines the class 
class Window(QWidget):
    def __init__(self): #Initiates the class and can instatiate itself 
        super().__init__()
        self.setWindowTitle("Pyside2 Calendar by Julio Del Cid studentid 332808")

#The format below is the position represented by the XY, then the width (600pixels) and height (500pixels)
        self.setGeometry(400,300,800,500)
        self.setIcon()

#Defines the calendar function 
        self.createCalendar()
        self.show()
 
 
#Defines the calendar icons within the icon  
    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)
 
#Defines the calendar function 
    def createCalendar(self):
        vbox = QVBoxLayout()    #vbox stands for vertical box, where the QVBox layout sets the attributes for the object
        self.calendar = QCalendarWidget()

#        self.calendar.setGridVisible(True)
 
        vbox.addWidget(self.calendar)
        self.setLayout(vbox)
 
 
julioapp = QApplication(sys.argv)
window = Window()
 
#Allows the user to end the program 
julioapp.exec_()
sys.exit()