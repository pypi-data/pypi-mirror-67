from PyQt5 import QtWidgets, QtGui, QtCore
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

from nndesigndemos.nndesign_layout import NNDLayout
from nndesigndemos.get_package_path import PACKAGE_PATH


class HopfieldClassification(NNDLayout):
    def __init__(self, w_ratio, h_ratio):
        super(HopfieldClassification, self).__init__(w_ratio, h_ratio, main_menu=1)

        self.fill_chapter("Hopfield Classification", 3, "Click [Go] to send a fruit\ndown the belt to be\nclassified"
                          " by a Hopfield\nnetwork.\n\nThe calculations for the\nHopfield network will\nappear below.",
                          PACKAGE_PATH + "Logo/Logo_Ch_3.svg", None)

        self.make_plot(1, (15, 100, 500, 390))
        self.axis = Axes3D(self.figure)
        ys = np.linspace(-1, 1, 100)
        zs = np.linspace(-1, 1, 100)
        Y, Z = np.meshgrid(ys, zs)
        X = 0
        apple = np.array([-1, 1, -1])
        orange = np.array([1, 1, -1])
        self.axis.set_title("Input Space")
        self.axis.plot_surface(X, Y, Z, alpha=0.5)
        self.axis.set_xlabel("texture")
        self.axis.set_xticks([-1, 1])
        self.axis.set_ylabel("shape")
        self.axis.set_yticks([-1, 1])
        self.axis.set_zlabel("weight")
        self.axis.zaxis._axinfo['label']['space_factor'] = 0.1
        self.axis.set_zticks([-1, 1])
        self.axis.scatter(orange[0], orange[1], orange[2], color='orange')
        self.axis.scatter(apple[0], apple[1], apple[2], color='yellow')
        self.line1, self.line2, self.line3 = None, None, None
        self.axis.view_init(10, 110)
        self.canvas.draw()

        self.p, self.a1, self.a2, self.fruit, self.label = None, None, None, None, None

        self.make_label("label_w", "W = [.2 0 0; 0 1.2 0; 0 0 .2]", (532, 320 - 5, 170, 25))
        self.make_label("label_b", "b = [0.9; 0; -0.9]", (532, 350 - 5, 150, 25))
        self.make_label("label_p", "", (532, 380 - 5, 150, 25))
        self.make_label("label_a_11", "", (532, 410 - 5, 150, 25))
        self.make_label("label_a_12", "", (532, 440 - 5, 150, 25))
        self.make_label("label_fruit", "", (532, 470 - 5, 150, 25))

        self.figure_w, self.figure_h = 575, 190
        self.icon3 = QtWidgets.QLabel(self)
        if self.running_on_windows:
            self.icon3.setPixmap(QtGui.QIcon(PACKAGE_PATH + "Figures/nnd3d1_1.svg").pixmap(self.figure_w * self.h_ratio, self.figure_h * self.h_ratio, QtGui.QIcon.Normal, QtGui.QIcon.On))
            self.icon3.setGeometry(28 * self.h_ratio, 485 * self.h_ratio, self.figure_w * self.h_ratio, self.figure_h * self.h_ratio)
        else:
            self.icon3.setPixmap(QtGui.QIcon(PACKAGE_PATH + "Figures/nnd3d1_1.svg").pixmap(self.figure_w * self.w_ratio, self.figure_h * self.h_ratio, QtGui.QIcon.Normal, QtGui.QIcon.On))
            self.icon3.setGeometry(28 * self.w_ratio, 485 * self.h_ratio, self.figure_w * self.w_ratio, self.figure_h * self.h_ratio)
        self.text_shape, self.text_texture, self.text_weight = "?", "?", "?"

        self.make_button("run_button", "Go", (self.x_chapter_button, 500, self.w_chapter_button, self.h_chapter_button), self.on_run)

    def paintEvent(self, event):
        super(HopfieldClassification, self).paintEvent(event)
        painter = QtGui.QPainter(self.icon3.pixmap())
        if self.running_on_windows:
            w_ratio, h_ratio = self.h_ratio, self.h_ratio
        else:
            w_ratio, h_ratio = self.w_ratio, self.h_ratio
        painter.setFont(QtGui.QFont("times", 12 * (w_ratio + h_ratio) / 2))
        painter.drawText(QtCore.QPoint(100 * w_ratio, 28 * h_ratio), self.text_shape)
        painter.drawText(QtCore.QPoint(245 * w_ratio, 28 * h_ratio), self.text_texture)
        painter.drawText(QtCore.QPoint(410 * w_ratio, 28 * h_ratio), self.text_weight)

    def on_run(self):
        self.timer = QtCore.QTimer()
        self.idx = 0
        self.text_shape, self.text_texture, self.text_weight = "?", "?", "?"
        self.icon3.setPixmap(QtGui.QIcon(PACKAGE_PATH + "Figures/nnd3d1_1.svg").pixmap(self.figure_w * self.w_ratio, self.figure_h * self.h_ratio, QtGui.QIcon.Normal, QtGui.QIcon.On))
        self.timer.timeout.connect(self.update_label)
        self.timer.start(800)

    def update_label(self):
        if self.idx == 0:
            self.label_p.setText("")
            self.label_a_11.setText(""); self.label_a_12.setText("")
            self.label_fruit.setText("")
            self.p = np.round(np.random.uniform(-1, 1, (1, 3)), 2)
            w = np.array([[0.2, 0, 0], [0, 1.2, 0], [0, 0, 0.2]])
            b = np.array([[0.9], [0], [-0.9]])
            self.a1 = np.round(self.satlins(np.dot(w, self.p.T) + b), 2)
            self.a2 = np.round(self.satlins(np.dot(w, self.a1) + b), 2)
            self.fruit = "Orange" if self.a2[1, 0] > 0 else "Apple"
            self.label = 1 if self.fruit == "Apple" else 0
            if self.line1:
                self.line1.pop().remove()
                self.line2.pop().remove()
                self.line3.pop().remove()
                self.canvas.draw()
        if self.idx == 1:
            if self.label == 1:
                self.icon3.setPixmap(QtGui.QIcon(PACKAGE_PATH + "Figures/nnd3d1_2.svg").pixmap(self.figure_w * self.w_ratio, self.figure_h * self.h_ratio, QtGui.QIcon.Normal, QtGui.QIcon.On))
            else:
                self.icon3.setPixmap(QtGui.QIcon(PACKAGE_PATH + "Figures/nnd3d1_7.svg").pixmap(self.figure_w * self.w_ratio, self.figure_h * self.h_ratio, QtGui.QIcon.Normal, QtGui.QIcon.On))
        elif self.idx == 2:
            if self.label == 1:
                self.icon3.setPixmap(QtGui.QIcon(PACKAGE_PATH + "Figures/nnd3d1_3.svg").pixmap(self.figure_w * self.w_ratio, self.figure_h * self.h_ratio, QtGui.QIcon.Normal, QtGui.QIcon.On))
            else:
                self.icon3.setPixmap(QtGui.QIcon(PACKAGE_PATH + "Figures/nnd3d1_8.svg").pixmap(self.figure_w * self.w_ratio, self.figure_h * self.h_ratio, QtGui.QIcon.Normal, QtGui.QIcon.On))
        elif self.idx == 3:
            self.text_shape, self.text_texture, self.text_weight = str(self.p[0, 0]), str(self.p[0, 1]), str(self.p[0, 2])
            if self.label == 1:
                self.icon3.setPixmap(QtGui.QIcon(PACKAGE_PATH + "Figures/nnd3d1_3.svg").pixmap(self.figure_w * self.w_ratio, self.figure_h * self.h_ratio, QtGui.QIcon.Normal, QtGui.QIcon.On))
            else:
                self.icon3.setPixmap(QtGui.QIcon(PACKAGE_PATH + "Figures/nnd3d1_8.svg").pixmap(self.figure_w * self.w_ratio, self.figure_h * self.h_ratio, QtGui.QIcon.Normal, QtGui.QIcon.On))
        elif self.idx == 4:
            self.line1 = self.axis.plot3D([self.p[0, 0]] * 10, np.linspace(-1, 1, 10), [self.p[0, 2]] * 10, color="g")
            self.line2 = self.axis.plot3D([self.p[0, 0]] * 10, [self.p[0, 1]] * 10, np.linspace(-1, 1, 10), color="g")
            self.line3 = self.axis.plot3D(np.linspace(-1, 1, 10), [self.p[0, 1]] * 10, [self.p[0, 2]] * 10, color="g")
            self.canvas.draw()
        elif self.idx == 5:
            self.label_p.setText("p = [{} {} {}]".format(self.p[0, 0], self.p[0, 1], self.p[0, 2]))
        elif self.idx == 6:
            self.label_a_11.setText("a1 = satlins(W * p + b)")
            if self.label == 1:
                self.icon3.setPixmap(QtGui.QIcon(PACKAGE_PATH + "Figures/nnd3d1_4.svg").pixmap(self.figure_w * self.w_ratio, self.figure_h * self.h_ratio, QtGui.QIcon.Normal, QtGui.QIcon.On))
            else:
                self.icon3.setPixmap(QtGui.QIcon(PACKAGE_PATH + "Figures/nnd3d1_9.svg").pixmap(self.figure_w * self.w_ratio, self.figure_h * self.h_ratio, QtGui.QIcon.Normal, QtGui.QIcon.On))
        elif self.idx == 7:
            self.label_a_12.setText("a1 = [{} {} {}]".format(self.a1[0, 0], self.a1[1, 0], self.a1[2, 0]))
            if self.label == 1:
                self.icon3.setPixmap(QtGui.QIcon(PACKAGE_PATH + "Figures/nnd3d1_5.svg").pixmap(self.figure_w * self.w_ratio, self.figure_h * self.h_ratio, QtGui.QIcon.Normal, QtGui.QIcon.On))
            else:
                self.icon3.setPixmap(QtGui.QIcon(PACKAGE_PATH + "Figures/nnd3d1_10.svg").pixmap(self.figure_w * self.w_ratio, self.figure_h * self.h_ratio, QtGui.QIcon.Normal, QtGui.QIcon.On))
        elif self.idx == 8:
            self.label_fruit.setText("Fruit = {}".format(self.fruit))
            if self.label == 1:
                self.icon3.setPixmap(QtGui.QIcon(PACKAGE_PATH + "Figures/nnd3d1_6.svg").pixmap(self.figure_w * self.w_ratio, self.figure_h * self.h_ratio, QtGui.QIcon.Normal, QtGui.QIcon.On))
            else:
                self.icon3.setPixmap(QtGui.QIcon(PACKAGE_PATH + "Figures/nnd3d1_11.svg").pixmap(self.figure_w * self.w_ratio, self.figure_h * self.h_ratio, QtGui.QIcon.Normal, QtGui.QIcon.On))
            pass
        self.idx += 1

    @staticmethod
    @np.vectorize
    def satlins(x):
        return max([-1, min([x, 1])])
