# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Owner\Documents\Final Round (Semester 8)\Produccion de Videojuegos\FinalProject_NeuralStyleTransfer\PyQT_Design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import DFT_InverseDFT_HPF
import os
import neural_style_transfer_1
import qimage2ndarray


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Photo made Art")
        MainWindow.resize(1132, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.SelectContent = QtWidgets.QPushButton(self.centralwidget)
        self.SelectContent.setGeometry(QtCore.QRect(50, 260, 240, 21))
        self.SelectContent.setObjectName("SelectContent")
        self.SelectContent.setText("Select Content Image")

        self.Select_Style = QtWidgets.QPushButton(self.centralwidget)
        self.Select_Style.setGeometry(QtCore.QRect(50, 540, 240, 22))
        self.Select_Style.setObjectName("Select_Style")
        self.Select_Style.setText("Select Style Image")

        self.displayContent = QtWidgets.QLabel(self.centralwidget)
        self.displayContent.setGeometry(QtCore.QRect(50, 10, 240, 240))
        self.displayContent.setFrameShape(QtWidgets.QFrame.Box)
        self.displayContent.setObjectName("displayContent")

        self.displayStyle = QtWidgets.QLabel(self.centralwidget)
        self.displayStyle.setGeometry(QtCore.QRect(50, 290, 240, 240))
        self.displayStyle.setFrameShape(QtWidgets.QFrame.Box)
        self.displayStyle.setObjectName("displayStyle")

        self.NeuralStyleTransfer_image = QtWidgets.QGraphicsView(self.centralwidget)
        self.NeuralStyleTransfer_image.setGeometry(QtCore.QRect(590, 10, 512, 512))
        self.NeuralStyleTransfer_image.setObjectName("NeuralStyleTransfer_image")

        self.apply_neural_style_transfer = QtWidgets.QPushButton(self.centralwidget)
        self.apply_neural_style_transfer.setGeometry(QtCore.QRect(790, 530, 150, 30))
        self.apply_neural_style_transfer.setObjectName("apply_neural_style_transfer")

        self.hpf_img = QtWidgets.QLabel(self.centralwidget)
        self.hpf_img.setGeometry(QtCore.QRect(320, 140, 240, 240))
        self.hpf_img.setFrameShape(QtWidgets.QFrame.Box)
        self.hpf_img.setObjectName("hpf_img")

        self.hpf_slider = QtWidgets.QSlider(self.centralwidget)
        self.hpf_slider.setGeometry(QtCore.QRect(320, 400, 240, 22))
        self.hpf_slider.setOrientation(QtCore.Qt.Horizontal)
        self.hpf_slider.setObjectName("hpf_slider")
        self.hpf_slider.setMinimum(2)
        self.hpf_slider.setMaximum(50)
       # self.hpf_slider.setTickInterval(5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1132, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.apply_neural_style_transfer.clicked.connect(self.make_art)
        self.SelectContent.clicked.connect(self.setContentImage)
        self.Select_Style.clicked.connect(self.setStyleImage)
        self.hpf_slider.valueChanged.connect(self.hpf_change_value)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.apply_neural_style_transfer.setText(_translate("MainWindow", "Apply Neural Style Transfer"))

    def setContentImage(self):
        content_img, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "content/", "Image Files(*.png *.jpg *.jpeg)")
        DFT_InverseDFT_HPF.read_img(content_img)
        neural_style_transfer_1.get_content_img(content_img)
        imageSelected = os.path.abspath(str(content_img))
        self.setContent_hpf(content_img)
        if content_img:
            pixmap = QtGui.QPixmap(content_img)
            pixmap = pixmap.scaled(self.displayContent.width(), self.displayContent.height(), QtCore.Qt.KeepAspectRatio)
            self.displayContent.setPixmap(pixmap)
            self.displayContent.setAlignment(QtCore.Qt.AlignCenter)
        return imageSelected

    def setStyleImage(self):
        style_img, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "" , "Image Files(*.png *.jpg *.jpeg *.bmp)")
        neural_style_transfer_1.get_style_img(style_img)
        if style_img:
            pixmap2 = QtGui.QPixmap(style_img)
            pixmap2 = pixmap2.scaled(self.displayStyle.width(), self.displayStyle.height(), QtCore.Qt.KeepAspectRatio)
            self.displayStyle.setPixmap(pixmap2)
            self.displayStyle.setAlignment(QtCore.Qt.AlignCenter)

    def hpf_change_value(self):
        freq_value = self.hpf_slider.value()
        dft_image = DFT_InverseDFT_HPF.hpf_method(freq_value)
        dft_Qimage = qimage2ndarray.array2qimage(dft_image)
        dft_Qpixmap_img = QtGui.QPixmap.fromImage(dft_Qimage)
        hpf_image_ready = QtGui.QPixmap(dft_Qpixmap_img)
        hpf_image_ready = hpf_image_ready.scaled(self.hpf_img.width(), self.hpf_img.height(), QtCore.Qt.KeepAspectRatio)
        self.setContent_hpf(hpf_image_ready)

    def setContent_hpf(self, content_img):
        if content_img:
            pixmap = QtGui.QPixmap(content_img)
            pixmap = pixmap.scaled(self.hpf_img.width(), self.hpf_img.height(), QtCore.Qt.KeepAspectRatio)
            self.hpf_img.setPixmap(pixmap)
            self.hpf_img.setAlignment(QtCore.Qt.AlignCenter)

    def make_art(self):
        best_img = neural_style_transfer_1.neural_style_transfer()
        if best_img:
            result = QtGui.QPixmap(best_img)
            result = result.scaled(self.displayStyle.width(), self.displayStyle.height(), QtCore.Qt.KeepAspectRatio)
            self.NeuralStyleTransfer_image.setPixmap(result)
            self.NeuralStyleTransfer_image.setAlignment(QtCore.Qt.AlignCenter)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()

