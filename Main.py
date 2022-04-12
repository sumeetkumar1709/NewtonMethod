from sympy import*

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 757)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 981, 771))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.790614, y2:0.511, stop:0 rgba(71, 118, 230, 255), stop:1 rgba(142, 84, 233, 255));}\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.heading = QtWidgets.QLabel(self.widget)
        self.heading.setGeometry(QtCore.QRect(0, 10, 871, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.heading.setFont(font)
        self.heading.setStyleSheet("color:white\n"
"")
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white\n"
"")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 110, 521, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#000\n"
"")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 521, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#000\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 521, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:#000\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(30, 170, 521, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:#000\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(40, 210, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:white\n"
"")
        self.label_6.setObjectName("label_6")
        self.inputText = QtWidgets.QLineEdit(self.widget)
        self.inputText.setGeometry(QtCore.QRect(40, 230, 781, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inputText.setFont(font)
        self.inputText.setObjectName("inputText")
        self.outputText = QtWidgets.QTextBrowser(self.widget)
        self.outputText.setGeometry(QtCore.QRect(40, 410, 811, 341))
        self.outputText.setObjectName("outputText")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(40, 380, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:white\n"
"")
        self.label_7.setObjectName("label_7")
        self.solve_button = QtWidgets.QPushButton(self.widget, clicked=lambda: self.press_it())
        self.solve_button.setGeometry(QtCore.QRect(340, 330, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(12)
        self.solve_button.setFont(font)
        self.solve_button.setStyleSheet("QPushButton{\n"
"color:#ffbfcf;\n"
"border-radius:20px;\n"
"border:2px solid #fff;\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: #fff;\n"
"  color: #514A9D;\n"
"   cursor: pointer;\n"
"}\n"
"\n"
"")
        self.solve_button.setObjectName("solve_button")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(40, 280, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:white\n"
"")
        self.label_8.setObjectName("label_8")
        self.startingX = QtWidgets.QLineEdit(self.widget)
        self.startingX.setGeometry(QtCore.QRect(170, 280, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.startingX.setFont(font)
        self.startingX.setObjectName("startingX")
        self.maxIterations = QtWidgets.QLineEdit(self.widget)
        self.maxIterations.setGeometry(QtCore.QRect(650, 280, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.maxIterations.setFont(font)
        self.maxIterations.setObjectName("maxIterations")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(450, 280, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:white\n"
"")
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def press_it(self):
        s = ''
        self.outputText.setText(s)
        x = Symbol('x')
        maxiter = int(self.maxIterations.text())
        curr_value = guess = float(self.startingX.text())
        eps = 10E-6
        expression = sympify(self.inputText.text())

        def f(z):
            return expression.subs(x, z)

        def g(z):
            d = diff(expression, x)
            return d.subs(x, z)

        for i in range(maxiter):
            cur_itr = curr_value - (f(curr_value) / g(curr_value))

            s += f"Value of x after iteration {i + 1} = {cur_itr} \n"
            self.outputText.setText(s)

            if abs(cur_itr - curr_value) < eps:
                s += '-'*200
                s += '\nRoot found : ' + str(cur_itr) +'\n'
                self.outputText.setText(s)
                return

            if i == maxiter - 1:
                s += '-' * 200
                s += '\n\nMax iterations reached!' + '\nApproximaiton to the Root after max iterations is : ' + str(cur_itr)
                self.outputText.setText(s)
                return

            curr_value = cur_itr
            i += 1


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NEWTON METHOD"))
        self.heading.setText(_translate("MainWindow", "NEWTON METHOD"))
        self.label_2.setText(_translate("MainWindow", "INSTRUCTIONS:"))
        self.label.setText(_translate("MainWindow", "1. For using powers \'^\' this cannot be used for 3^4 it should be written 3**4"))
        self.label_3.setText(_translate("MainWindow", "2. For using exponential equations e^x should be written as exp(x)"))
        self.label_4.setText(_translate("MainWindow", "3. 8x should be written as 8*x"))
        self.label_5.setText(_translate("MainWindow", "4. Every equation will by default be equated to 0 "))
        self.label_6.setText(_translate("MainWindow", "Enter the equation below in terms of x only :"))
        self.label_7.setText(_translate("MainWindow", "Output :"))
        self.solve_button.setText(_translate("MainWindow", "Solve"))
        self.label_8.setText(_translate("MainWindow", "Enter starting x:"))
        self.label_10.setText(_translate("MainWindow", "Max. Number of Iterations:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
