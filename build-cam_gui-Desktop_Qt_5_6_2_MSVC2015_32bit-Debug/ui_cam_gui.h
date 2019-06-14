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
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
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
    QGroupBox *groupBox_3;
    QWidget *gridLayoutWidget_4;
    QGridLayout *gridLayout_8;
    QSpacerItem *horizontalSpacer_26;
    QSpacerItem *horizontalSpacer_25;
    QDoubleSpinBox *doubleSpinBox_EMCCD_Gain;
    QLabel *label_EMCCDGain_disp;
    QSpacerItem *horizontalSpacer_21;
    QSpacerItem *horizontalSpacer_22;
    QGroupBox *groupBox_2;
    QWidget *gridLayoutWidget_3;
    QGridLayout *gridLayout_7;
    QSpacerItem *horizontalSpacer_18;
    QSpacerItem *horizontalSpacer_17;
    QDoubleSpinBox *doubleSpinBox_Exp_Time;
    QLabel *label_Exp_time_disp;
    QSpacerItem *horizontalSpacer_11;
    QSpacerItem *horizontalSpacer_12;
    QSpacerItem *verticalSpacer_3;
    QSpacerItem *verticalSpacer_5;
    QSpacerItem *verticalSpacer_6;
    QSpacerItem *verticalSpacer;
    QSpacerItem *verticalSpacer_2;
    QSpacerItem *verticalSpacer_4;
    QSpacerItem *horizontalSpacer_3;
    QSpacerItem *horizontalSpacer_2;
    QSpacerItem *horizontalSpacer;
    QSpacerItem *horizontalSpacer_5;
    QSpacerItem *horizontalSpacer_6;
    QSpacerItem *horizontalSpacer_4;
    QLabel *label;
    QLabel *label_Cam_OnOff;
    QPushButton *pushButton_Cam_On;
    QPushButton *pushButton_Cam_Off;
    QGroupBox *groupBox_5;
    QWidget *gridLayoutWidget_6;
    QGridLayout *gridLayout_10;
    QSpacerItem *horizontalSpacer_36;
    QSpacerItem *horizontalSpacer_35;
    QLabel *label_Read_mode;
    QLineEdit *lineEdit_read_mode;
    QSpacerItem *horizontalSpacer_9;
    QSpacerItem *horizontalSpacer_10;
    QGroupBox *groupBox;
    QWidget *gridLayoutWidget_2;
    QGridLayout *gridLayout_5;
    QLabel *label_Cooler_OnOff;
    QLabel *label_Temp_disp;
    QDoubleSpinBox *doubleSpinBox_Temp_set;
    QPushButton *pushButton_Temp_set;
    QGroupBox *groupBox_4;
    QWidget *gridLayoutWidget_5;
    QGridLayout *gridLayout_9;
    QLabel *label_Acq_mode;
    QLineEdit *lineEdit_acq_mode;
    QSpacerItem *horizontalSpacer_32;
    QSpacerItem *horizontalSpacer_31;
    QSpacerItem *horizontalSpacer_7;
    QSpacerItem *horizontalSpacer_8;
    QSpacerItem *verticalSpacer_7;
    QPushButton *pushButton_Save;
    QGroupBox *groupBox_6;
    QWidget *gridLayoutWidget_7;
    QGridLayout *gridLayout_2;
    QDoubleSpinBox *doubleSpinBox_Accum_time;
    QLabel *label_8;
    QLabel *label_7;
    QDoubleSpinBox *doubleSpinBox_no_Kin;
    QLabel *label_no_Kin;
    QLabel *label_Kin_time;
    QDoubleSpinBox *doubleSpinBox_no_Accum;
    QLabel *label_2;
    QLabel *label_Accum_time;
    QLabel *label_3;
    QLabel *label_no_Accum;
    QDoubleSpinBox *doubleSpinBox_Kin_time;
    QFrame *line;
    QLabel *label_6;
    QPushButton *pushButton_Snap;
    QFrame *frame;
    QLineEdit *lineEdit_Browse;
    QPushButton *pushButton_Browse;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *cam_gui)
    {
        if (cam_gui->objectName().isEmpty())
            cam_gui->setObjectName(QStringLiteral("cam_gui"));
        cam_gui->resize(840, 688);
        centralWidget = new QWidget(cam_gui);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        gridLayoutWidget = new QWidget(centralWidget);
        gridLayoutWidget->setObjectName(QStringLiteral("gridLayoutWidget"));
        gridLayoutWidget->setGeometry(QRect(9, -1, 821, 631));
        gridLayout = new QGridLayout(gridLayoutWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        groupBox_3 = new QGroupBox(gridLayoutWidget);
        groupBox_3->setObjectName(QStringLiteral("groupBox_3"));
        QFont font;
        font.setPointSize(9);
        groupBox_3->setFont(font);
        gridLayoutWidget_4 = new QWidget(groupBox_3);
        gridLayoutWidget_4->setObjectName(QStringLiteral("gridLayoutWidget_4"));
        gridLayoutWidget_4->setGeometry(QRect(0, 10, 391, 78));
        gridLayout_8 = new QGridLayout(gridLayoutWidget_4);
        gridLayout_8->setSpacing(6);
        gridLayout_8->setContentsMargins(11, 11, 11, 11);
        gridLayout_8->setObjectName(QStringLiteral("gridLayout_8"));
        gridLayout_8->setContentsMargins(0, 0, 0, 0);
        horizontalSpacer_26 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_8->addItem(horizontalSpacer_26, 0, 0, 1, 1);

        horizontalSpacer_25 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_8->addItem(horizontalSpacer_25, 0, 1, 1, 1);

        doubleSpinBox_EMCCD_Gain = new QDoubleSpinBox(gridLayoutWidget_4);
        doubleSpinBox_EMCCD_Gain->setObjectName(QStringLiteral("doubleSpinBox_EMCCD_Gain"));
        QFont font1;
        font1.setPointSize(11);
        doubleSpinBox_EMCCD_Gain->setFont(font1);
        doubleSpinBox_EMCCD_Gain->setDecimals(0);
        doubleSpinBox_EMCCD_Gain->setMaximum(300);

        gridLayout_8->addWidget(doubleSpinBox_EMCCD_Gain, 1, 1, 1, 1);

        label_EMCCDGain_disp = new QLabel(gridLayoutWidget_4);
        label_EMCCDGain_disp->setObjectName(QStringLiteral("label_EMCCDGain_disp"));
        label_EMCCDGain_disp->setFont(font1);
        label_EMCCDGain_disp->setAlignment(Qt::AlignCenter);

        gridLayout_8->addWidget(label_EMCCDGain_disp, 1, 0, 1, 1);

        horizontalSpacer_21 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_8->addItem(horizontalSpacer_21, 2, 0, 1, 1);

        horizontalSpacer_22 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_8->addItem(horizontalSpacer_22, 2, 1, 1, 1);


        gridLayout->addWidget(groupBox_3, 7, 4, 1, 3);

        groupBox_2 = new QGroupBox(gridLayoutWidget);
        groupBox_2->setObjectName(QStringLiteral("groupBox_2"));
        groupBox_2->setFont(font);
        gridLayoutWidget_3 = new QWidget(groupBox_2);
        gridLayoutWidget_3->setObjectName(QStringLiteral("gridLayoutWidget_3"));
        gridLayoutWidget_3->setGeometry(QRect(0, 10, 391, 78));
        gridLayout_7 = new QGridLayout(gridLayoutWidget_3);
        gridLayout_7->setSpacing(6);
        gridLayout_7->setContentsMargins(11, 11, 11, 11);
        gridLayout_7->setObjectName(QStringLiteral("gridLayout_7"));
        gridLayout_7->setContentsMargins(0, 0, 0, 0);
        horizontalSpacer_18 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_7->addItem(horizontalSpacer_18, 0, 0, 1, 1);

        horizontalSpacer_17 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_7->addItem(horizontalSpacer_17, 0, 1, 1, 1);

        doubleSpinBox_Exp_Time = new QDoubleSpinBox(gridLayoutWidget_3);
        doubleSpinBox_Exp_Time->setObjectName(QStringLiteral("doubleSpinBox_Exp_Time"));
        doubleSpinBox_Exp_Time->setFont(font1);
        doubleSpinBox_Exp_Time->setDecimals(3);
        doubleSpinBox_Exp_Time->setMinimum(0);
        doubleSpinBox_Exp_Time->setMaximum(5);
        doubleSpinBox_Exp_Time->setSingleStep(0.1);

        gridLayout_7->addWidget(doubleSpinBox_Exp_Time, 1, 1, 1, 1);

        label_Exp_time_disp = new QLabel(gridLayoutWidget_3);
        label_Exp_time_disp->setObjectName(QStringLiteral("label_Exp_time_disp"));
        label_Exp_time_disp->setFont(font1);
        label_Exp_time_disp->setAlignment(Qt::AlignCenter);

        gridLayout_7->addWidget(label_Exp_time_disp, 1, 0, 1, 1);

        horizontalSpacer_11 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_7->addItem(horizontalSpacer_11, 2, 0, 1, 1);

        horizontalSpacer_12 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_7->addItem(horizontalSpacer_12, 2, 1, 1, 1);


        gridLayout->addWidget(groupBox_2, 7, 1, 1, 3);

        verticalSpacer_3 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_3, 9, 0, 1, 1);

        verticalSpacer_5 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_5, 7, 0, 1, 1);

        verticalSpacer_6 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_6, 8, 0, 1, 1);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer, 2, 0, 1, 1);

        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_2, 5, 0, 1, 1);

        verticalSpacer_4 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_4, 6, 0, 1, 1);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_3, 0, 4, 1, 1);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_2, 0, 5, 1, 1);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer, 0, 6, 1, 1);

        horizontalSpacer_5 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_5, 0, 2, 1, 1);

        horizontalSpacer_6 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_6, 0, 3, 1, 1);

        horizontalSpacer_4 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_4, 0, 1, 1, 1);

        label = new QLabel(gridLayoutWidget);
        label->setObjectName(QStringLiteral("label"));
        label->setFont(font1);

        gridLayout->addWidget(label, 2, 3, 1, 1);

        label_Cam_OnOff = new QLabel(gridLayoutWidget);
        label_Cam_OnOff->setObjectName(QStringLiteral("label_Cam_OnOff"));
        label_Cam_OnOff->setFont(font1);
        label_Cam_OnOff->setAlignment(Qt::AlignCenter);

        gridLayout->addWidget(label_Cam_OnOff, 2, 4, 1, 1);

        pushButton_Cam_On = new QPushButton(gridLayoutWidget);
        pushButton_Cam_On->setObjectName(QStringLiteral("pushButton_Cam_On"));
        pushButton_Cam_On->setFont(font1);

        gridLayout->addWidget(pushButton_Cam_On, 2, 5, 1, 1);

        pushButton_Cam_Off = new QPushButton(gridLayoutWidget);
        pushButton_Cam_Off->setObjectName(QStringLiteral("pushButton_Cam_Off"));
        pushButton_Cam_Off->setFont(font1);

        gridLayout->addWidget(pushButton_Cam_Off, 2, 6, 1, 1);

        groupBox_5 = new QGroupBox(gridLayoutWidget);
        groupBox_5->setObjectName(QStringLiteral("groupBox_5"));
        groupBox_5->setFont(font);
        gridLayoutWidget_6 = new QWidget(groupBox_5);
        gridLayoutWidget_6->setObjectName(QStringLiteral("gridLayoutWidget_6"));
        gridLayoutWidget_6->setGeometry(QRect(0, 10, 391, 74));
        gridLayout_10 = new QGridLayout(gridLayoutWidget_6);
        gridLayout_10->setSpacing(6);
        gridLayout_10->setContentsMargins(11, 11, 11, 11);
        gridLayout_10->setObjectName(QStringLiteral("gridLayout_10"));
        gridLayout_10->setContentsMargins(0, 0, 0, 0);
        horizontalSpacer_36 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_10->addItem(horizontalSpacer_36, 0, 1, 1, 1);

        horizontalSpacer_35 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_10->addItem(horizontalSpacer_35, 0, 0, 1, 1);

        label_Read_mode = new QLabel(gridLayoutWidget_6);
        label_Read_mode->setObjectName(QStringLiteral("label_Read_mode"));
        label_Read_mode->setFont(font1);
        label_Read_mode->setAlignment(Qt::AlignCenter);

        gridLayout_10->addWidget(label_Read_mode, 1, 0, 1, 1);

        lineEdit_read_mode = new QLineEdit(gridLayoutWidget_6);
        lineEdit_read_mode->setObjectName(QStringLiteral("lineEdit_read_mode"));

        gridLayout_10->addWidget(lineEdit_read_mode, 1, 1, 1, 1);

        horizontalSpacer_9 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_10->addItem(horizontalSpacer_9, 2, 0, 1, 1);

        horizontalSpacer_10 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_10->addItem(horizontalSpacer_10, 2, 1, 1, 1);


        gridLayout->addWidget(groupBox_5, 6, 4, 1, 3);

        groupBox = new QGroupBox(gridLayoutWidget);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        groupBox->setFont(font);
        gridLayoutWidget_2 = new QWidget(groupBox);
        gridLayoutWidget_2->setObjectName(QStringLiteral("gridLayoutWidget_2"));
        gridLayoutWidget_2->setGeometry(QRect(0, 10, 791, 71));
        gridLayout_5 = new QGridLayout(gridLayoutWidget_2);
        gridLayout_5->setSpacing(6);
        gridLayout_5->setContentsMargins(11, 11, 11, 11);
        gridLayout_5->setObjectName(QStringLiteral("gridLayout_5"));
        gridLayout_5->setContentsMargins(0, 0, 0, 0);
        label_Cooler_OnOff = new QLabel(gridLayoutWidget_2);
        label_Cooler_OnOff->setObjectName(QStringLiteral("label_Cooler_OnOff"));
        label_Cooler_OnOff->setFont(font1);
        label_Cooler_OnOff->setAlignment(Qt::AlignCenter);

        gridLayout_5->addWidget(label_Cooler_OnOff, 0, 1, 1, 1);

        label_Temp_disp = new QLabel(gridLayoutWidget_2);
        label_Temp_disp->setObjectName(QStringLiteral("label_Temp_disp"));
        label_Temp_disp->setFont(font1);
        label_Temp_disp->setAlignment(Qt::AlignCenter);

        gridLayout_5->addWidget(label_Temp_disp, 0, 0, 1, 1);

        doubleSpinBox_Temp_set = new QDoubleSpinBox(gridLayoutWidget_2);
        doubleSpinBox_Temp_set->setObjectName(QStringLiteral("doubleSpinBox_Temp_set"));
        doubleSpinBox_Temp_set->setFont(font1);
        doubleSpinBox_Temp_set->setDecimals(0);
        doubleSpinBox_Temp_set->setMinimum(-70);
        doubleSpinBox_Temp_set->setMaximum(30);
        doubleSpinBox_Temp_set->setValue(-30);

        gridLayout_5->addWidget(doubleSpinBox_Temp_set, 0, 2, 1, 1);

        pushButton_Temp_set = new QPushButton(gridLayoutWidget_2);
        pushButton_Temp_set->setObjectName(QStringLiteral("pushButton_Temp_set"));
        pushButton_Temp_set->setFont(font1);

        gridLayout_5->addWidget(pushButton_Temp_set, 0, 3, 1, 1);


        gridLayout->addWidget(groupBox, 5, 1, 1, 6);

        groupBox_4 = new QGroupBox(gridLayoutWidget);
        groupBox_4->setObjectName(QStringLiteral("groupBox_4"));
        groupBox_4->setFont(font);
        gridLayoutWidget_5 = new QWidget(groupBox_4);
        gridLayoutWidget_5->setObjectName(QStringLiteral("gridLayoutWidget_5"));
        gridLayoutWidget_5->setGeometry(QRect(0, 10, 391, 74));
        gridLayout_9 = new QGridLayout(gridLayoutWidget_5);
        gridLayout_9->setSpacing(6);
        gridLayout_9->setContentsMargins(11, 11, 11, 11);
        gridLayout_9->setObjectName(QStringLiteral("gridLayout_9"));
        gridLayout_9->setContentsMargins(0, 0, 0, 0);
        label_Acq_mode = new QLabel(gridLayoutWidget_5);
        label_Acq_mode->setObjectName(QStringLiteral("label_Acq_mode"));
        label_Acq_mode->setFont(font1);
        label_Acq_mode->setAlignment(Qt::AlignCenter);

        gridLayout_9->addWidget(label_Acq_mode, 1, 0, 1, 1);

        lineEdit_acq_mode = new QLineEdit(gridLayoutWidget_5);
        lineEdit_acq_mode->setObjectName(QStringLiteral("lineEdit_acq_mode"));

        gridLayout_9->addWidget(lineEdit_acq_mode, 1, 1, 1, 1);

        horizontalSpacer_32 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_9->addItem(horizontalSpacer_32, 0, 1, 1, 1);

        horizontalSpacer_31 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_9->addItem(horizontalSpacer_31, 0, 0, 1, 1);

        horizontalSpacer_7 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_9->addItem(horizontalSpacer_7, 2, 0, 1, 1);

        horizontalSpacer_8 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_9->addItem(horizontalSpacer_8, 2, 1, 1, 1);


        gridLayout->addWidget(groupBox_4, 6, 1, 1, 3);

        verticalSpacer_7 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_7, 10, 0, 1, 1);

        pushButton_Save = new QPushButton(gridLayoutWidget);
        pushButton_Save->setObjectName(QStringLiteral("pushButton_Save"));
        pushButton_Save->setFont(font1);

        gridLayout->addWidget(pushButton_Save, 10, 6, 1, 1);

        groupBox_6 = new QGroupBox(gridLayoutWidget);
        groupBox_6->setObjectName(QStringLiteral("groupBox_6"));
        groupBox_6->setFont(font);
        gridLayoutWidget_7 = new QWidget(groupBox_6);
        gridLayoutWidget_7->setObjectName(QStringLiteral("gridLayoutWidget_7"));
        gridLayoutWidget_7->setGeometry(QRect(10, 10, 781, 151));
        gridLayout_2 = new QGridLayout(gridLayoutWidget_7);
        gridLayout_2->setSpacing(6);
        gridLayout_2->setContentsMargins(11, 11, 11, 11);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        gridLayout_2->setContentsMargins(0, 0, 0, 0);
        doubleSpinBox_Accum_time = new QDoubleSpinBox(gridLayoutWidget_7);
        doubleSpinBox_Accum_time->setObjectName(QStringLiteral("doubleSpinBox_Accum_time"));
        doubleSpinBox_Accum_time->setFont(font1);
        doubleSpinBox_Accum_time->setDecimals(3);

        gridLayout_2->addWidget(doubleSpinBox_Accum_time, 1, 3, 1, 1);

        label_8 = new QLabel(gridLayoutWidget_7);
        label_8->setObjectName(QStringLiteral("label_8"));
        label_8->setFont(font1);

        gridLayout_2->addWidget(label_8, 1, 5, 1, 1);

        label_7 = new QLabel(gridLayoutWidget_7);
        label_7->setObjectName(QStringLiteral("label_7"));
        label_7->setFont(font1);

        gridLayout_2->addWidget(label_7, 0, 5, 1, 1);

        doubleSpinBox_no_Kin = new QDoubleSpinBox(gridLayoutWidget_7);
        doubleSpinBox_no_Kin->setObjectName(QStringLiteral("doubleSpinBox_no_Kin"));
        doubleSpinBox_no_Kin->setFont(font1);
        doubleSpinBox_no_Kin->setDecimals(0);

        gridLayout_2->addWidget(doubleSpinBox_no_Kin, 0, 7, 1, 1);

        label_no_Kin = new QLabel(gridLayoutWidget_7);
        label_no_Kin->setObjectName(QStringLiteral("label_no_Kin"));
        label_no_Kin->setFont(font1);
        label_no_Kin->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_no_Kin, 0, 6, 1, 1);

        label_Kin_time = new QLabel(gridLayoutWidget_7);
        label_Kin_time->setObjectName(QStringLiteral("label_Kin_time"));
        label_Kin_time->setFont(font1);
        label_Kin_time->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_Kin_time, 1, 6, 1, 1);

        doubleSpinBox_no_Accum = new QDoubleSpinBox(gridLayoutWidget_7);
        doubleSpinBox_no_Accum->setObjectName(QStringLiteral("doubleSpinBox_no_Accum"));
        doubleSpinBox_no_Accum->setFont(font1);
        doubleSpinBox_no_Accum->setDecimals(0);

        gridLayout_2->addWidget(doubleSpinBox_no_Accum, 0, 3, 1, 1);

        label_2 = new QLabel(gridLayoutWidget_7);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setFont(font1);
        label_2->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);

        gridLayout_2->addWidget(label_2, 0, 1, 1, 1);

        label_Accum_time = new QLabel(gridLayoutWidget_7);
        label_Accum_time->setObjectName(QStringLiteral("label_Accum_time"));
        label_Accum_time->setFont(font1);
        label_Accum_time->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_Accum_time, 1, 2, 1, 1);

        label_3 = new QLabel(gridLayoutWidget_7);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setFont(font1);

        gridLayout_2->addWidget(label_3, 1, 1, 1, 1);

        label_no_Accum = new QLabel(gridLayoutWidget_7);
        label_no_Accum->setObjectName(QStringLiteral("label_no_Accum"));
        label_no_Accum->setFont(font1);
        label_no_Accum->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_no_Accum, 0, 2, 1, 1);

        doubleSpinBox_Kin_time = new QDoubleSpinBox(gridLayoutWidget_7);
        doubleSpinBox_Kin_time->setObjectName(QStringLiteral("doubleSpinBox_Kin_time"));
        doubleSpinBox_Kin_time->setFont(font1);
        doubleSpinBox_Kin_time->setDecimals(3);

        gridLayout_2->addWidget(doubleSpinBox_Kin_time, 1, 7, 1, 1);

        line = new QFrame(gridLayoutWidget_7);
        line->setObjectName(QStringLiteral("line"));
        line->setFrameShape(QFrame::VLine);
        line->setFrameShadow(QFrame::Sunken);

        gridLayout_2->addWidget(line, 0, 4, 2, 1);


        gridLayout->addWidget(groupBox_6, 8, 1, 2, 6);

        label_6 = new QLabel(gridLayoutWidget);
        label_6->setObjectName(QStringLiteral("label_6"));
        label_6->setFont(font1);

        gridLayout->addWidget(label_6, 10, 1, 1, 1);

        pushButton_Snap = new QPushButton(gridLayoutWidget);
        pushButton_Snap->setObjectName(QStringLiteral("pushButton_Snap"));
        pushButton_Snap->setFont(font1);

        gridLayout->addWidget(pushButton_Snap, 10, 2, 1, 1);

        frame = new QFrame(gridLayoutWidget);
        frame->setObjectName(QStringLiteral("frame"));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        lineEdit_Browse = new QLineEdit(frame);
        lineEdit_Browse->setObjectName(QStringLiteral("lineEdit_Browse"));
        lineEdit_Browse->setGeometry(QRect(0, 30, 261, 20));

        gridLayout->addWidget(frame, 10, 4, 1, 2);

        pushButton_Browse = new QPushButton(gridLayoutWidget);
        pushButton_Browse->setObjectName(QStringLiteral("pushButton_Browse"));
        pushButton_Browse->setFont(font1);

        gridLayout->addWidget(pushButton_Browse, 10, 3, 1, 1);

        cam_gui->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(cam_gui);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 840, 21));
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
        groupBox_3->setTitle(QApplication::translate("cam_gui", "EMCCD Gain", 0));
        label_EMCCDGain_disp->setText(QApplication::translate("cam_gui", "0", 0));
        groupBox_2->setTitle(QApplication::translate("cam_gui", "Exposure Time", 0));
        label_Exp_time_disp->setText(QApplication::translate("cam_gui", "0 s", 0));
        label->setText(QApplication::translate("cam_gui", "Initialisation:", 0));
        label_Cam_OnOff->setText(QApplication::translate("cam_gui", "OFF", 0));
        pushButton_Cam_On->setText(QApplication::translate("cam_gui", "Camera ON", 0));
        pushButton_Cam_Off->setText(QApplication::translate("cam_gui", "Camera OFF", 0));
        groupBox_5->setTitle(QApplication::translate("cam_gui", "Read Mode", 0));
        label_Read_mode->setText(QApplication::translate("cam_gui", "N/A", 0));
        groupBox->setTitle(QApplication::translate("cam_gui", "Temperature", 0));
        label_Cooler_OnOff->setText(QApplication::translate("cam_gui", "OFF", 0));
        label_Temp_disp->setText(QApplication::translate("cam_gui", "0 \302\260C", 0));
        pushButton_Temp_set->setText(QApplication::translate("cam_gui", "Set", 0));
        groupBox_4->setTitle(QApplication::translate("cam_gui", "Acquisition Mode", 0));
        label_Acq_mode->setText(QApplication::translate("cam_gui", "N/A", 0));
        pushButton_Save->setText(QApplication::translate("cam_gui", "Save", 0));
        groupBox_6->setTitle(QApplication::translate("cam_gui", "Kinetic Settings", 0));
        label_8->setText(QApplication::translate("cam_gui", "Kinetic Cycle Time:", 0));
        label_7->setText(QApplication::translate("cam_gui", "Number in Kinetic Series:", 0));
        label_no_Kin->setText(QApplication::translate("cam_gui", "1", 0));
        label_Kin_time->setText(QApplication::translate("cam_gui", "0 s", 0));
        label_2->setText(QApplication::translate("cam_gui", "Number of Accumulations:", 0));
        label_Accum_time->setText(QApplication::translate("cam_gui", "0 s", 0));
        label_3->setText(QApplication::translate("cam_gui", "Accumulation Cycle Time:", 0));
        label_no_Accum->setText(QApplication::translate("cam_gui", "1", 0));
        label_6->setText(QApplication::translate("cam_gui", "Picture:", 0));
        pushButton_Snap->setText(QApplication::translate("cam_gui", "Snap", 0));
        pushButton_Browse->setText(QApplication::translate("cam_gui", "Browse", 0));
    } // retranslateUi

};

namespace Ui {
    class cam_gui: public Ui_cam_gui {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CAM_GUI_H
