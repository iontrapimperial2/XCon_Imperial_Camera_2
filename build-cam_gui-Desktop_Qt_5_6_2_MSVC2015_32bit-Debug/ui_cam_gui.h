/********************************************************************************
** Form generated from reading UI file 'cam_gui.ui'
**
** Created by: Qt User Interface Compiler version 5.6.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CAM_GUI_H
#define UI_CAM_GUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDoubleSpinBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_cam_gui
{
public:
    QWidget *centralWidget;
    QWidget *gridLayoutWidget;
    QGridLayout *gridLayout;
    QPushButton *pushButton_Temp_set;
    QDoubleSpinBox *doubleSpinBox_Temp_set;
    QLabel *label_6;
    QSpacerItem *verticalSpacer_5;
    QDoubleSpinBox *doubleSpinBox_Exp_Time;
    QLabel *label;
    QDoubleSpinBox *doubleSpinBox_EMCCD_Gain;
    QSpacerItem *verticalSpacer_6;
    QPushButton *pushButton_Save;
    QPushButton *pushButton_Snap;
    QLabel *label_2;
    QLabel *label_4;
    QLabel *label_3;
    QPushButton *pushButton_Cam_OnOff;
    QLabel *label_5;
    QLabel *label_Cam_OnOff;
    QSpacerItem *verticalSpacer;
    QSpacerItem *verticalSpacer_2;
    QSpacerItem *verticalSpacer_3;
    QSpacerItem *verticalSpacer_4;
    QSpacerItem *horizontalSpacer_3;
    QLabel *label_Cooler_OnOff;
    QPushButton *pushButton_Exp_Time;
    QSpacerItem *horizontalSpacer_2;
    QLabel *label_Temp_disp;
    QSpacerItem *horizontalSpacer;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *cam_gui)
    {
        if (cam_gui->objectName().isEmpty())
            cam_gui->setObjectName(QStringLiteral("cam_gui"));
        cam_gui->resize(508, 557);
        centralWidget = new QWidget(cam_gui);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        gridLayoutWidget = new QWidget(centralWidget);
        gridLayoutWidget->setObjectName(QStringLiteral("gridLayoutWidget"));
        gridLayoutWidget->setGeometry(QRect(9, -1, 481, 501));
        gridLayout = new QGridLayout(gridLayoutWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        pushButton_Temp_set = new QPushButton(gridLayoutWidget);
        pushButton_Temp_set->setObjectName(QStringLiteral("pushButton_Temp_set"));
        QFont font;
        font.setPointSize(11);
        pushButton_Temp_set->setFont(font);

        gridLayout->addWidget(pushButton_Temp_set, 2, 4, 1, 1);

        doubleSpinBox_Temp_set = new QDoubleSpinBox(gridLayoutWidget);
        doubleSpinBox_Temp_set->setObjectName(QStringLiteral("doubleSpinBox_Temp_set"));
        doubleSpinBox_Temp_set->setFont(font);
        doubleSpinBox_Temp_set->setMinimum(-60);
        doubleSpinBox_Temp_set->setMaximum(30);
        doubleSpinBox_Temp_set->setValue(-30);

        gridLayout->addWidget(doubleSpinBox_Temp_set, 2, 3, 1, 1);

        label_6 = new QLabel(gridLayoutWidget);
        label_6->setObjectName(QStringLiteral("label_6"));
        label_6->setFont(font);

        gridLayout->addWidget(label_6, 6, 2, 1, 1);

        verticalSpacer_5 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_5, 5, 0, 1, 1);

        doubleSpinBox_Exp_Time = new QDoubleSpinBox(gridLayoutWidget);
        doubleSpinBox_Exp_Time->setObjectName(QStringLiteral("doubleSpinBox_Exp_Time"));
        doubleSpinBox_Exp_Time->setFont(font);
        doubleSpinBox_Exp_Time->setMinimum(0);
        doubleSpinBox_Exp_Time->setMaximum(5);
        doubleSpinBox_Exp_Time->setSingleStep(0.1);

        gridLayout->addWidget(doubleSpinBox_Exp_Time, 4, 3, 1, 1);

        label = new QLabel(gridLayoutWidget);
        label->setObjectName(QStringLiteral("label"));
        label->setFont(font);

        gridLayout->addWidget(label, 1, 2, 1, 1);

        doubleSpinBox_EMCCD_Gain = new QDoubleSpinBox(gridLayoutWidget);
        doubleSpinBox_EMCCD_Gain->setObjectName(QStringLiteral("doubleSpinBox_EMCCD_Gain"));
        doubleSpinBox_EMCCD_Gain->setFont(font);
        doubleSpinBox_EMCCD_Gain->setDecimals(0);
        doubleSpinBox_EMCCD_Gain->setMaximum(300);

        gridLayout->addWidget(doubleSpinBox_EMCCD_Gain, 5, 3, 1, 1);

        verticalSpacer_6 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_6, 6, 0, 1, 1);

        pushButton_Save = new QPushButton(gridLayoutWidget);
        pushButton_Save->setObjectName(QStringLiteral("pushButton_Save"));
        pushButton_Save->setFont(font);

        gridLayout->addWidget(pushButton_Save, 6, 4, 1, 1);

        pushButton_Snap = new QPushButton(gridLayoutWidget);
        pushButton_Snap->setObjectName(QStringLiteral("pushButton_Snap"));
        pushButton_Snap->setFont(font);

        gridLayout->addWidget(pushButton_Snap, 6, 3, 1, 1);

        label_2 = new QLabel(gridLayoutWidget);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setFont(font);

        gridLayout->addWidget(label_2, 2, 2, 1, 1);

        label_4 = new QLabel(gridLayoutWidget);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setFont(font);

        gridLayout->addWidget(label_4, 4, 2, 1, 1);

        label_3 = new QLabel(gridLayoutWidget);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setFont(font);

        gridLayout->addWidget(label_3, 3, 2, 1, 1);

        pushButton_Cam_OnOff = new QPushButton(gridLayoutWidget);
        pushButton_Cam_OnOff->setObjectName(QStringLiteral("pushButton_Cam_OnOff"));
        pushButton_Cam_OnOff->setFont(font);

        gridLayout->addWidget(pushButton_Cam_OnOff, 1, 4, 1, 1);

        label_5 = new QLabel(gridLayoutWidget);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setFont(font);

        gridLayout->addWidget(label_5, 5, 2, 1, 1);

        label_Cam_OnOff = new QLabel(gridLayoutWidget);
        label_Cam_OnOff->setObjectName(QStringLiteral("label_Cam_OnOff"));
        label_Cam_OnOff->setFont(font);
        label_Cam_OnOff->setAlignment(Qt::AlignCenter);

        gridLayout->addWidget(label_Cam_OnOff, 1, 3, 1, 1);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer, 1, 0, 1, 1);

        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_2, 2, 0, 1, 1);

        verticalSpacer_3 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_3, 3, 0, 1, 1);

        verticalSpacer_4 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_4, 4, 0, 1, 1);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_3, 0, 2, 1, 1);

        label_Cooler_OnOff = new QLabel(gridLayoutWidget);
        label_Cooler_OnOff->setObjectName(QStringLiteral("label_Cooler_OnOff"));
        label_Cooler_OnOff->setFont(font);
        label_Cooler_OnOff->setAlignment(Qt::AlignCenter);

        gridLayout->addWidget(label_Cooler_OnOff, 3, 4, 1, 1);

        pushButton_Exp_Time = new QPushButton(gridLayoutWidget);
        pushButton_Exp_Time->setObjectName(QStringLiteral("pushButton_Exp_Time"));
        pushButton_Exp_Time->setFont(font);

        gridLayout->addWidget(pushButton_Exp_Time, 4, 4, 1, 1);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_2, 0, 3, 1, 1);

        label_Temp_disp = new QLabel(gridLayoutWidget);
        label_Temp_disp->setObjectName(QStringLiteral("label_Temp_disp"));
        label_Temp_disp->setFont(font);
        label_Temp_disp->setAlignment(Qt::AlignCenter);

        gridLayout->addWidget(label_Temp_disp, 3, 3, 1, 1);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer, 0, 4, 1, 1);

        cam_gui->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(cam_gui);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 508, 21));
        cam_gui->setMenuBar(menuBar);
        mainToolBar = new QToolBar(cam_gui);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        cam_gui->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(cam_gui);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        cam_gui->setStatusBar(statusBar);

        retranslateUi(cam_gui);

        QMetaObject::connectSlotsByName(cam_gui);
    } // setupUi

    void retranslateUi(QMainWindow *cam_gui)
    {
        cam_gui->setWindowTitle(QApplication::translate("cam_gui", "cam_gui", 0));
        pushButton_Temp_set->setText(QApplication::translate("cam_gui", "Set", 0));
        label_6->setText(QApplication::translate("cam_gui", "Picture:", 0));
        label->setText(QApplication::translate("cam_gui", "Initialisation:", 0));
        pushButton_Save->setText(QApplication::translate("cam_gui", "Save", 0));
        pushButton_Snap->setText(QApplication::translate("cam_gui", "Snap", 0));
        label_2->setText(QApplication::translate("cam_gui", "Temperature set:", 0));
        label_4->setText(QApplication::translate("cam_gui", "Exposure Time:", 0));
        label_3->setText(QApplication::translate("cam_gui", "Temperature:", 0));
        pushButton_Cam_OnOff->setText(QApplication::translate("cam_gui", "Camera", 0));
        label_5->setText(QApplication::translate("cam_gui", "EMCCD Gain:", 0));
        label_Cam_OnOff->setText(QApplication::translate("cam_gui", "OFF", 0));
        label_Cooler_OnOff->setText(QApplication::translate("cam_gui", "OFF", 0));
        pushButton_Exp_Time->setText(QApplication::translate("cam_gui", "Set", 0));
        label_Temp_disp->setText(QApplication::translate("cam_gui", "0 \302\260C", 0));
    } // retranslateUi

};

namespace Ui {
    class cam_gui: public Ui_cam_gui {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CAM_GUI_H
