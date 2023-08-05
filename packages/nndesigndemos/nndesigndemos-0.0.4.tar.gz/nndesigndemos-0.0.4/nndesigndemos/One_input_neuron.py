from PyQt5 import QtWidgets, QtCore
import numpy as np
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)

from nndesigndemos.nndesign_layout import NNDLayout
from nndesigndemos.get_package_path import PACKAGE_PATH


class OneInputNeuron(NNDLayout):
    def __init__(self, w_ratio, h_ratio):
        super(OneInputNeuron, self).__init__(w_ratio, h_ratio, main_menu=1)

        self.fill_chapter("One-Input Neuron", 2, "\nAlter the weight, bias and\ninput by moving the\nsliders.\n\n"
                                                 "Pick the transfer function\nwith the f menu."
                                                 "\n\nWatch the change to the\nneuron function and its\noutput.",
                          PACKAGE_PATH + "Chapters/2/Logo_Ch_2.svg", PACKAGE_PATH + "Chapters/2/SingleInputNeuron.svg",
                          icon_move_left=-5)

        self.make_plot(1)

        self.make_slider("slider_w", QtCore.Qt.Horizontal, (-30, 30), QtWidgets.QSlider.TicksBelow, 1, 10,
                         (self.x_chapter_usual, 340, self.w_chapter_slider, 50), self.graph, "label_w", "w: 1.0")
        self.make_slider("slider_b", QtCore.Qt.Horizontal, (-30, 30), QtWidgets.QSlider.TicksBelow, 1, 0,
                         (self.x_chapter_usual, 410, self.w_chapter_slider, 50), self.graph, "label_b", "b: 0.0")

        self.comboBox1_functions_str = ["purelin", "poslin", 'hardlim', 'hardlims', 'satlin', 'satlins', 'logsig', 'tansig']
        self.make_combobox(1, self.comboBox1_functions_str, (self.x_chapter_usual, 470, self.w_chapter_slider, 50),
                           self.change_transfer_function, "label_f", "f", label_italics=True)
        self.comboBox1_functions = [self.purelin, self.poslin, self.hardlim, self.hardlims, self.satlin, self.satlins, self.logsig, self.tansig]
        self.func1 = self.purelin
        self.func_idx = 0

        self.graph()

    def graph(self):

        a = self.figure.add_subplot(1, 1, 1)
        a.clear()
        a.set_xlim(-2, 2)
        a.set_ylim(-2, 2)
        a.set_xticks([-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5])
        a.set_yticks([-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5])
        a.plot([0] * 10, np.linspace(-2, 2, 10), color="black", linestyle="--", linewidth=0.2)
        a.plot(np.linspace(-2, 2, 10), [0] * 10, color="black", linestyle="--", linewidth=0.2)
        a.set_xlabel("$p$")
        a.xaxis.set_label_coords(1, -0.025)
        a.set_ylabel("$a$")
        a.yaxis.set_label_coords(-0.025, 1)

        weight = self.slider_w.value() / 10
        bias = self.slider_b.value() / 10
        self.label_w.setText("w: " + str(weight))
        self.label_b.setText("b: " + str(bias))
        p = np.arange(-4, 4, 0.1)
        func = np.vectorize(self.func1)
        out = func(np.dot(weight, p) + bias)

        a.plot(p, out, markersize=3, color="red")
        a.set_title("$a = {}(w \cdot p + b)$".format(self.comboBox1_functions_str[self.func_idx]))

        self.canvas.draw()

    def change_transfer_function(self, idx):
        self.func1 = self.comboBox1_functions[idx]
        self.func_idx = idx
        self.graph()
