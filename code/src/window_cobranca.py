# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_cobranca.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTreeView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(847, 510)
        MainWindow.setMinimumSize(QSize(847, 510))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_header = QGridLayout()
        self.gridLayout_header.setObjectName(u"gridLayout_header")
        self.label_header_title = QLabel(self.centralwidget)
        self.label_header_title.setObjectName(u"label_header_title")
        font = QFont()
        font.setFamilies([u"Tw Cen MT"])
        font.setPointSize(26)
        font.setBold(True)
        self.label_header_title.setFont(font)
        self.label_header_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_header.addWidget(self.label_header_title, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(100, -1, 100, -1)
        self.label_header_logo = QLabel(self.frame_2)
        self.label_header_logo.setObjectName(u"label_header_logo")
        self.label_header_logo.setPixmap(QPixmap(u"../imgs/mail-hori.png"))
        self.label_header_logo.setScaledContents(True)

        self.gridLayout_5.addWidget(self.label_header_logo, 0, 0, 1, 1)


        self.gridLayout_header.addWidget(self.frame_2, 0, 0, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 5))
        self.line.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.line.setLineWidth(0)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_header.addWidget(self.line, 2, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_header, 0, 0, 1, 1)

        self.stackedWidget_body = QStackedWidget(self.centralwidget)
        self.stackedWidget_body.setObjectName(u"stackedWidget_body")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.gridLayout_3 = QGridLayout(self.page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_body_relatorio_anexar = QPushButton(self.page)
        self.pushButton_body_relatorio_anexar.setObjectName(u"pushButton_body_relatorio_anexar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_body_relatorio_anexar.sizePolicy().hasHeightForWidth())
        self.pushButton_body_relatorio_anexar.setSizePolicy(sizePolicy)
        self.pushButton_body_relatorio_anexar.setMinimumSize(QSize(400, 50))
        font1 = QFont()
        font1.setFamilies([u"Rockwell"])
        font1.setPointSize(12)
        self.pushButton_body_relatorio_anexar.setFont(font1)
        self.pushButton_body_relatorio_anexar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_body_relatorio_anexar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon = QIcon()
        icon.addFile(u"../imgs/upload-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_body_relatorio_anexar.setIcon(icon)
        self.pushButton_body_relatorio_anexar.setIconSize(QSize(48, 48))

        self.gridLayout_3.addWidget(self.pushButton_body_relatorio_anexar, 9, 1, 1, 1)

        self.comboBox_body_funcionario = QComboBox(self.page)
        self.comboBox_body_funcionario.addItem("")
        self.comboBox_body_funcionario.addItem("")
        self.comboBox_body_funcionario.setObjectName(u"comboBox_body_funcionario")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_body_funcionario.sizePolicy().hasHeightForWidth())
        self.comboBox_body_funcionario.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(14)
        self.comboBox_body_funcionario.setFont(font2)
        self.comboBox_body_funcionario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_body_funcionario.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_3.addWidget(self.comboBox_body_funcionario, 1, 1, 2, 1)

        self.label_bodyrelatorio_title = QLabel(self.page)
        self.label_bodyrelatorio_title.setObjectName(u"label_bodyrelatorio_title")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_bodyrelatorio_title.sizePolicy().hasHeightForWidth())
        self.label_bodyrelatorio_title.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u"Tw Cen MT"])
        font3.setPointSize(16)
        self.label_bodyrelatorio_title.setFont(font3)
        self.label_bodyrelatorio_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_bodyrelatorio_title, 8, 1, 1, 1)

        self.pushButton_empresas_marcar = QPushButton(self.page)
        self.pushButton_empresas_marcar.setObjectName(u"pushButton_empresas_marcar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_empresas_marcar.sizePolicy().hasHeightForWidth())
        self.pushButton_empresas_marcar.setSizePolicy(sizePolicy3)
        self.pushButton_empresas_marcar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_3.addWidget(self.pushButton_empresas_marcar, 10, 0, 1, 1)

        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 384, 132))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.stackedWidget_empresas = QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget_empresas.setObjectName(u"stackedWidget_empresas")
        self.stackedWidget_empresas.setEnabled(True)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_7 = QGridLayout(self.page_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_empresas = QGridLayout()
        self.gridLayout_empresas.setObjectName(u"gridLayout_empresas")
        self.label_empresas_aviso = QLabel(self.page_3)
        self.label_empresas_aviso.setObjectName(u"label_empresas_aviso")
        self.label_empresas_aviso.setEnabled(False)
        font4 = QFont()
        font4.setFamilies([u"NSimSun"])
        font4.setPointSize(14)
        font4.setItalic(True)
        self.label_empresas_aviso.setFont(font4)
        self.label_empresas_aviso.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_empresas.addWidget(self.label_empresas_aviso, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_empresas, 1, 0, 1, 1)

        self.stackedWidget_empresas.addWidget(self.page_3)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_11 = QGridLayout(self.page_6)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_loading_empresas = QLabel(self.page_6)
        self.label_loading_empresas.setObjectName(u"label_loading_empresas")
        self.label_loading_empresas.setMaximumSize(QSize(96, 96))
        self.label_loading_empresas.setPixmap(QPixmap(u"../imgs/load.gif"))
        self.label_loading_empresas.setScaledContents(True)

        self.gridLayout_11.addWidget(self.label_loading_empresas, 0, 0, 1, 1)

        self.stackedWidget_empresas.addWidget(self.page_6)

        self.gridLayout_6.addWidget(self.stackedWidget_empresas, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 1, 0, 9, 1)

        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_body_executar = QPushButton(self.frame)
        self.pushButton_body_executar.setObjectName(u"pushButton_body_executar")
        self.pushButton_body_executar.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.pushButton_body_executar.sizePolicy().hasHeightForWidth())
        self.pushButton_body_executar.setSizePolicy(sizePolicy3)
        self.pushButton_body_executar.setMinimumSize(QSize(200, 40))
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(False)
        font5.setItalic(True)
        font5.setUnderline(False)
        self.pushButton_body_executar.setFont(font5)
        self.pushButton_body_executar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_body_executar.setStyleSheet(u"border: 2.5px solid rgb(85, 170, 255); border-radius: 10px; background-color: #E1E1E1;")

        self.gridLayout_4.addWidget(self.pushButton_body_executar, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 10, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.label_body_empresas_title = QLabel(self.page)
        self.label_body_empresas_title.setObjectName(u"label_body_empresas_title")
        self.label_body_empresas_title.setFont(font3)
        self.label_body_empresas_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_body_empresas_title, 0, 0, 1, 1)

        self.label_body_funcionario_title = QLabel(self.page)
        self.label_body_funcionario_title.setObjectName(u"label_body_funcionario_title")
        sizePolicy2.setHeightForWidth(self.label_body_funcionario_title.sizePolicy().hasHeightForWidth())
        self.label_body_funcionario_title.setSizePolicy(sizePolicy2)
        self.label_body_funcionario_title.setFont(font3)
        self.label_body_funcionario_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_body_funcionario_title, 0, 1, 1, 1)

        self.stackedWidget_body.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_8 = QGridLayout(self.page_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer = QSpacerItem(246, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.page_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(100, -1, 100, -1)
        self.progressBar = QProgressBar(self.frame_3)
        self.progressBar.setObjectName(u"progressBar")

        self.gridLayout_9.addWidget(self.progressBar, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_3, 3, 0, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(246, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.label_load_gif = QLabel(self.page_2)
        self.label_load_gif.setObjectName(u"label_load_gif")
        self.label_load_gif.setMaximumSize(QSize(192, 192))
        self.label_load_gif.setPixmap(QPixmap(u"../imgs/load.gif"))
        self.label_load_gif.setScaledContents(True)
        self.label_load_gif.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.label_load_gif, 0, 1, 1, 1)

        self.label_load_title = QLabel(self.page_2)
        self.label_load_title.setObjectName(u"label_load_title")
        font6 = QFont()
        font6.setFamilies([u"Tw Cen MT"])
        font6.setPointSize(24)
        font6.setBold(False)
        font6.setItalic(True)
        self.label_load_title.setFont(font6)
        self.label_load_title.setTextFormat(Qt.TextFormat.PlainText)
        self.label_load_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.label_load_title, 2, 1, 1, 1)

        self.stackedWidget_body.addWidget(self.page_2)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout = QGridLayout(self.page_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_endereco = QPushButton(self.page_5)
        self.pushButton_endereco.setObjectName(u"pushButton_endereco")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_endereco.sizePolicy().hasHeightForWidth())
        self.pushButton_endereco.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.pushButton_endereco, 4, 2, 1, 1)

        self.label_endereco_empresa = QLabel(self.page_5)
        self.label_endereco_empresa.setObjectName(u"label_endereco_empresa")
        font7 = QFont()
        font7.setFamilies([u"Trebuchet MS"])
        font7.setPointSize(14)
        font7.setBold(True)
        self.label_endereco_empresa.setFont(font7)
        self.label_endereco_empresa.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_endereco_empresa, 1, 1, 1, 2)

        self.label_endereco_input_title = QLabel(self.page_5)
        self.label_endereco_input_title.setObjectName(u"label_endereco_input_title")
        font8 = QFont()
        font8.setFamilies([u"Tw Cen MT"])
        font8.setPointSize(14)
        font8.setBold(False)
        self.label_endereco_input_title.setFont(font8)

        self.gridLayout.addWidget(self.label_endereco_input_title, 3, 1, 1, 1)

        self.frame_4 = QFrame(self.page_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, -1, 50, -1)
        self.lineEdit_endereco = QLineEdit(self.frame_4)
        self.lineEdit_endereco.setObjectName(u"lineEdit_endereco")

        self.gridLayout_10.addWidget(self.lineEdit_endereco, 0, 0, 1, 1)

        self.label_endereco_input_subtitle = QLabel(self.frame_4)
        self.label_endereco_input_subtitle.setObjectName(u"label_endereco_input_subtitle")
        font9 = QFont()
        font9.setFamilies([u"Tw Cen MT"])
        font9.setPointSize(12)
        font9.setBold(True)
        font9.setItalic(True)
        self.label_endereco_input_subtitle.setFont(font9)
        self.label_endereco_input_subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_10.addWidget(self.label_endereco_input_subtitle, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_4, 4, 1, 1, 1)

        self.label_endereco_title = QLabel(self.page_5)
        self.label_endereco_title.setObjectName(u"label_endereco_title")
        font10 = QFont()
        font10.setFamilies([u"Tw Cen MT"])
        font10.setPointSize(22)
        font10.setUnderline(True)
        self.label_endereco_title.setFont(font10)
        self.label_endereco_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_endereco_title, 0, 1, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.stackedWidget_body.addWidget(self.page_5)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_12 = QGridLayout(self.page_4)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.treeView = QTreeView(self.page_4)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setAnimated(False)

        self.gridLayout_12.addWidget(self.treeView, 0, 0, 1, 1)

        self.stackedWidget_body.addWidget(self.page_4)

        self.gridLayout_2.addWidget(self.stackedWidget_body, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 847, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget_body.setCurrentIndex(0)
        self.stackedWidget_empresas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cobran\u00e7a Autom\u00e1tica", None))
        self.label_header_title.setText(QCoreApplication.translate("MainWindow", u"Cobran\u00e7a Autom\u00e1tica", None))
        self.label_header_logo.setText("")
        self.pushButton_body_relatorio_anexar.setText("")
        self.comboBox_body_funcionario.setItemText(0, QCoreApplication.translate("MainWindow", u"Bruno", None))
        self.comboBox_body_funcionario.setItemText(1, QCoreApplication.translate("MainWindow", u"Wellington", None))

        self.label_bodyrelatorio_title.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rio de vencidos", None))
        self.pushButton_empresas_marcar.setText(QCoreApplication.translate("MainWindow", u"Desmacar todos", None))
        self.label_empresas_aviso.setText(QCoreApplication.translate("MainWindow", u"Insira o relat\u00f3rio de vencidos", None))
        self.label_loading_empresas.setText("")
        self.pushButton_body_executar.setText(QCoreApplication.translate("MainWindow", u"Executar", None))
        self.label_body_empresas_title.setText(QCoreApplication.translate("MainWindow", u"Empresas que deseja cobrar", None))
        self.label_body_funcionario_title.setText(QCoreApplication.translate("MainWindow", u"Funcion\u00e1rio respons\u00e1vel", None))
        self.label_load_gif.setText("")
        self.label_load_title.setText(QCoreApplication.translate("MainWindow", u"Carregando...", None))
        self.pushButton_endereco.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.label_endereco_empresa.setText(QCoreApplication.translate("MainWindow", u"nome da empresa", None))
        self.label_endereco_input_title.setText(QCoreApplication.translate("MainWindow", u"Favor, insira o(s) endere\u00e7o(s) de email da empresa", None))
        self.label_endereco_input_subtitle.setText(QCoreApplication.translate("MainWindow", u"No caso de mais de um endere\u00e7o, os divida com ponto-e-v\u00edrgula \";\"", None))
        self.label_endereco_title.setText(QCoreApplication.translate("MainWindow", u"Empresa abaixo n\u00e3o cadastrada!", None))
    # retranslateUi

