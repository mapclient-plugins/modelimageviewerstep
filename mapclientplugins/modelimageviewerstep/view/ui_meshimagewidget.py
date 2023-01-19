# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'meshimagewidget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)

from opencmiss.zincwidgets.sceneviewerwidget import SceneviewerWidget

class Ui_MeshImageWidget(object):
    def setupUi(self, MeshImageWidget):
        if not MeshImageWidget.objectName():
            MeshImageWidget.setObjectName(u"MeshImageWidget")
        MeshImageWidget.resize(884, 640)
        self.horizontalLayout = QHBoxLayout(MeshImageWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_3 = QGroupBox(MeshImageWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_5 = QGroupBox(self.groupBox_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButtonContinue = QPushButton(self.groupBox_5)
        self.pushButtonContinue.setObjectName(u"pushButtonContinue")

        self.horizontalLayout_3.addWidget(self.pushButtonContinue)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addWidget(self.groupBox_5)

        self.listWidget = QListWidget(self.groupBox_3)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_2.addWidget(self.listWidget)

        self.groupBox_4 = QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout = QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonViewAll = QPushButton(self.groupBox_4)
        self.pushButtonViewAll.setObjectName(u"pushButtonViewAll")

        self.horizontalLayout_2.addWidget(self.pushButtonViewAll)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_2 = QGroupBox(self.groupBox_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.labelAngle = QLabel(self.groupBox_2)
        self.labelAngle.setObjectName(u"labelAngle")

        self.verticalLayout_6.addWidget(self.labelAngle)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lineEditAngle = QLineEdit(self.groupBox_2)
        self.lineEditAngle.setObjectName(u"lineEditAngle")
        self.lineEditAngle.setMaximumSize(QSize(40, 16777215))
        self.lineEditAngle.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)

        self.horizontalLayout_7.addWidget(self.lineEditAngle)

        self.horizontalSliderAngle = QSlider(self.groupBox_2)
        self.horizontalSliderAngle.setObjectName(u"horizontalSliderAngle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalSliderAngle.sizePolicy().hasHeightForWidth())
        self.horizontalSliderAngle.setSizePolicy(sizePolicy1)
        self.horizontalSliderAngle.setMaximum(100)
        self.horizontalSliderAngle.setValue(50)
        self.horizontalSliderAngle.setSliderPosition(50)
        self.horizontalSliderAngle.setTracking(False)
        self.horizontalSliderAngle.setOrientation(Qt.Horizontal)

        self.horizontalLayout_7.addWidget(self.horizontalSliderAngle)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)


        self.verticalLayout_2.addWidget(self.groupBox_2)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.widgetZinc = SceneviewerWidget(MeshImageWidget)
        self.widgetZinc.setObjectName(u"widgetZinc")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(3)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.widgetZinc.sizePolicy().hasHeightForWidth())
        self.widgetZinc.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.widgetZinc)


        self.retranslateUi(MeshImageWidget)

        QMetaObject.connectSlotsByName(MeshImageWidget)
    # setupUi

    def retranslateUi(self, MeshImageWidget):
        MeshImageWidget.setWindowTitle(QCoreApplication.translate("MeshImageWidget", u"Mesh/Image", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MeshImageWidget", u"Mesh/Image Controls", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MeshImageWidget", u"File", None))
        self.pushButtonContinue.setText(QCoreApplication.translate("MeshImageWidget", u"Continue", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MeshImageWidget", u"View", None))
        self.pushButtonViewAll.setText(QCoreApplication.translate("MeshImageWidget", u"View All", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MeshImageWidget", u"Plane", None))
        self.labelAngle.setText(QCoreApplication.translate("MeshImageWidget", u"Angle:", None))
    # retranslateUi

