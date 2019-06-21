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
#include <QtWidgets/QComboBox>
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
    QGridLayout *gridLayout_4;
    QGridLayout *gridLayout;
    QPushButton *pushButton_Save;
    QSpacerItem *horizontalSpacer_6;
    QSpacerItem *verticalSpacer_10;
    QSpacerItem *verticalSpacer_3;
    QFrame *frame;
    QGridLayout *gridLayout_19;
    QLineEdit *lineEdit_Browse;
    QGroupBox *groupBox_5;
    QGridLayout *gridLayout_14;
    QGridLayout *gridLayout_10;
    QLabel *label_Read_mode;
    QComboBox *comboBox_Read_mode;
    QGroupBox *groupBox_3;
    QGridLayout *gridLayout_16;
    QGridLayout *gridLayout_8;
    QLabel *label_EMCCDGain_disp;
    QDoubleSpinBox *doubleSpinBox_EMCCD_Gain;
    QPushButton *pushButton_Cam_Off;
    QSpacerItem *verticalSpacer;
    QGroupBox *groupBox_7;
    QGridLayout *gridLayout_17;
    QGridLayout *gridLayout_3;
    QDoubleSpinBox *doubleSpinBox_End_row;
    QDoubleSpinBox *doubleSpinBox_Start_col;
    QLabel *label_10;
    QLabel *label_End_col;
    QLabel *label_Start_row;
    QLabel *label_End_row;
    QDoubleSpinBox *doubleSpinBox_End_col;
    QLabel *label_9;
    QLabel *label_11;
    QLabel *label_4;
    QLabel *label_Start_col;
    QDoubleSpinBox *doubleSpinBox_Start_row;
    QFrame *line_2;
    QGroupBox *groupBox_6;
    QGridLayout *gridLayout_18;
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
    QSpacerItem *horizontalSpacer_2;
    QLabel *label_6;
    QPushButton *pushButton_Cam_On;
    QPushButton *pushButton_Browse;
    QSpacerItem *horizontalSpacer_3;
    QSpacerItem *horizontalSpacer;
    QLabel *label;
    QSpacerItem *verticalSpacer_8;
    QSpacerItem *verticalSpacer_6;
    QGroupBox *groupBox;
    QGridLayout *gridLayout_12;
    QGridLayout *gridLayout_5;
    QLabel *label_Cooler_OnOff;
    QLabel *label_Temp_disp;
    QDoubleSpinBox *doubleSpinBox_Temp_set;
    QPushButton *pushButton_Temp_set;
    QSpacerItem *verticalSpacer_5;
    QSpacerItem *horizontalSpacer_5;
    QSpacerItem *verticalSpacer_9;
    QLabel *label_Cam_OnOff;
    QSpacerItem *verticalSpacer_2;
    QSpacerItem *verticalSpacer_7;
    QGroupBox *groupBox_4;
    QGridLayout *gridLayout_13;
    QGridLayout *gridLayout_9;
    QLabel *label_Acq_mode;
    QComboBox *comboBox_Acq_mode;
    QSpacerItem *horizontalSpacer_4;
    QPushButton *pushButton_Snap;
    QSpacerItem *verticalSpacer_4;
    QGroupBox *groupBox_2;
    QGridLayout *gridLayout_15;
    QGridLayout *gridLayout_7;
    QDoubleSpinBox *doubleSpinBox_Exp_Time;
    QLabel *label_Exp_time_disp;
    QGroupBox *groupBox_8;
    QGridLayout *gridLayout_6;
    QGridLayout *gridLayout_11;
    QLabel *label_Trig_mode;
    QComboBox *comboBox_trig_mode;
    QPushButton *pushButton_trig_mode;
    QGroupBox *groupBox_9;
    QGridLayout *gridLayout_21;
    QGridLayout *gridLayout_20;
    QLabel *label_VSAmp;
    QPushButton *pushButton_VSAmp;
    QDoubleSpinBox *doubleSpinBox_VSAmp;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *cam_gui)
    {
        if (cam_gui->objectName().isEmpty())
            cam_gui->setObjectName(QStringLiteral("cam_gui"));
        cam_gui->resize(863, 762);
        centralWidget = new QWidget(cam_gui);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        gridLayout_4 = new QGridLayout(centralWidget);
        gridLayout_4->setSpacing(6);
        gridLayout_4->setContentsMargins(11, 11, 11, 11);
        gridLayout_4->setObjectName(QStringLiteral("gridLayout_4"));
        gridLayout = new QGridLayout();
        gridLayout->setSpacing(6);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        pushButton_Save = new QPushButton(centralWidget);
        pushButton_Save->setObjectName(QStringLiteral("pushButton_Save"));
        QFont font;
        font.setPointSize(11);
        pushButton_Save->setFont(font);

        gridLayout->addWidget(pushButton_Save, 11, 6, 1, 1);

        horizontalSpacer_6 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_6, 0, 3, 1, 1);

        verticalSpacer_10 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_10, 11, 0, 1, 1);

        verticalSpacer_3 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_3, 7, 0, 1, 1);

        frame = new QFrame(centralWidget);
        frame->setObjectName(QStringLiteral("frame"));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        gridLayout_19 = new QGridLayout(frame);
        gridLayout_19->setSpacing(6);
        gridLayout_19->setContentsMargins(11, 11, 11, 11);
        gridLayout_19->setObjectName(QStringLiteral("gridLayout_19"));
        lineEdit_Browse = new QLineEdit(frame);
        lineEdit_Browse->setObjectName(QStringLiteral("lineEdit_Browse"));

        gridLayout_19->addWidget(lineEdit_Browse, 0, 0, 1, 1);


        gridLayout->addWidget(frame, 11, 4, 1, 2);

        groupBox_5 = new QGroupBox(centralWidget);
        groupBox_5->setObjectName(QStringLiteral("groupBox_5"));
        QFont font1;
        font1.setPointSize(9);
        groupBox_5->setFont(font1);
        gridLayout_14 = new QGridLayout(groupBox_5);
        gridLayout_14->setSpacing(6);
        gridLayout_14->setContentsMargins(11, 11, 11, 11);
        gridLayout_14->setObjectName(QStringLiteral("gridLayout_14"));
        gridLayout_10 = new QGridLayout();
        gridLayout_10->setSpacing(6);
        gridLayout_10->setObjectName(QStringLiteral("gridLayout_10"));
        label_Read_mode = new QLabel(groupBox_5);
        label_Read_mode->setObjectName(QStringLiteral("label_Read_mode"));
        label_Read_mode->setFont(font);
        label_Read_mode->setAlignment(Qt::AlignCenter);

        gridLayout_10->addWidget(label_Read_mode, 0, 0, 1, 1);

        comboBox_Read_mode = new QComboBox(groupBox_5);
        comboBox_Read_mode->setObjectName(QStringLiteral("comboBox_Read_mode"));
        comboBox_Read_mode->setFont(font);
        comboBox_Read_mode->setEditable(false);

        gridLayout_10->addWidget(comboBox_Read_mode, 0, 1, 1, 1);


        gridLayout_14->addLayout(gridLayout_10, 0, 0, 1, 1);


        gridLayout->addWidget(groupBox_5, 4, 4, 1, 3);

        groupBox_3 = new QGroupBox(centralWidget);
        groupBox_3->setObjectName(QStringLiteral("groupBox_3"));
        groupBox_3->setFont(font1);
        gridLayout_16 = new QGridLayout(groupBox_3);
        gridLayout_16->setSpacing(6);
        gridLayout_16->setContentsMargins(11, 11, 11, 11);
        gridLayout_16->setObjectName(QStringLiteral("gridLayout_16"));
        gridLayout_8 = new QGridLayout();
        gridLayout_8->setSpacing(6);
        gridLayout_8->setObjectName(QStringLiteral("gridLayout_8"));
        label_EMCCDGain_disp = new QLabel(groupBox_3);
        label_EMCCDGain_disp->setObjectName(QStringLiteral("label_EMCCDGain_disp"));
        label_EMCCDGain_disp->setFont(font);
        label_EMCCDGain_disp->setAlignment(Qt::AlignCenter);

        gridLayout_8->addWidget(label_EMCCDGain_disp, 0, 0, 1, 1);

        doubleSpinBox_EMCCD_Gain = new QDoubleSpinBox(groupBox_3);
        doubleSpinBox_EMCCD_Gain->setObjectName(QStringLiteral("doubleSpinBox_EMCCD_Gain"));
        doubleSpinBox_EMCCD_Gain->setFont(font);
        doubleSpinBox_EMCCD_Gain->setDecimals(0);
        doubleSpinBox_EMCCD_Gain->setMaximum(300);

        gridLayout_8->addWidget(doubleSpinBox_EMCCD_Gain, 0, 1, 1, 1);


        gridLayout_16->addLayout(gridLayout_8, 0, 0, 1, 1);


        gridLayout->addWidget(groupBox_3, 5, 4, 1, 3);

        pushButton_Cam_Off = new QPushButton(centralWidget);
        pushButton_Cam_Off->setObjectName(QStringLiteral("pushButton_Cam_Off"));
        pushButton_Cam_Off->setFont(font);

        gridLayout->addWidget(pushButton_Cam_Off, 2, 6, 1, 1);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer, 2, 0, 1, 1);

        groupBox_7 = new QGroupBox(centralWidget);
        groupBox_7->setObjectName(QStringLiteral("groupBox_7"));
        groupBox_7->setFont(font1);
        gridLayout_17 = new QGridLayout(groupBox_7);
        gridLayout_17->setSpacing(6);
        gridLayout_17->setContentsMargins(11, 11, 11, 11);
        gridLayout_17->setObjectName(QStringLiteral("gridLayout_17"));
        gridLayout_3 = new QGridLayout();
        gridLayout_3->setSpacing(6);
        gridLayout_3->setObjectName(QStringLiteral("gridLayout_3"));
        doubleSpinBox_End_row = new QDoubleSpinBox(groupBox_7);
        doubleSpinBox_End_row->setObjectName(QStringLiteral("doubleSpinBox_End_row"));
        doubleSpinBox_End_row->setFont(font);
        doubleSpinBox_End_row->setDecimals(0);
        doubleSpinBox_End_row->setMaximum(512);

        gridLayout_3->addWidget(doubleSpinBox_End_row, 1, 6, 1, 1);

        doubleSpinBox_Start_col = new QDoubleSpinBox(groupBox_7);
        doubleSpinBox_Start_col->setObjectName(QStringLiteral("doubleSpinBox_Start_col"));
        doubleSpinBox_Start_col->setFont(font);
        doubleSpinBox_Start_col->setDecimals(0);
        doubleSpinBox_Start_col->setMaximum(512);
        doubleSpinBox_Start_col->setValue(1);

        gridLayout_3->addWidget(doubleSpinBox_Start_col, 0, 2, 1, 1);

        label_10 = new QLabel(groupBox_7);
        label_10->setObjectName(QStringLiteral("label_10"));
        label_10->setFont(font);

        gridLayout_3->addWidget(label_10, 0, 4, 1, 1);

        label_End_col = new QLabel(groupBox_7);
        label_End_col->setObjectName(QStringLiteral("label_End_col"));
        label_End_col->setFont(font);
        label_End_col->setAlignment(Qt::AlignCenter);

        gridLayout_3->addWidget(label_End_col, 1, 1, 1, 1);

        label_Start_row = new QLabel(groupBox_7);
        label_Start_row->setObjectName(QStringLiteral("label_Start_row"));
        label_Start_row->setFont(font);
        label_Start_row->setAlignment(Qt::AlignCenter);

        gridLayout_3->addWidget(label_Start_row, 0, 5, 1, 1);

        label_End_row = new QLabel(groupBox_7);
        label_End_row->setObjectName(QStringLiteral("label_End_row"));
        label_End_row->setFont(font);
        label_End_row->setAlignment(Qt::AlignCenter);

        gridLayout_3->addWidget(label_End_row, 1, 5, 1, 1);

        doubleSpinBox_End_col = new QDoubleSpinBox(groupBox_7);
        doubleSpinBox_End_col->setObjectName(QStringLiteral("doubleSpinBox_End_col"));
        doubleSpinBox_End_col->setFont(font);
        doubleSpinBox_End_col->setDecimals(0);
        doubleSpinBox_End_col->setMaximum(512);

        gridLayout_3->addWidget(doubleSpinBox_End_col, 1, 2, 1, 1);

        label_9 = new QLabel(groupBox_7);
        label_9->setObjectName(QStringLiteral("label_9"));
        label_9->setFont(font);

        gridLayout_3->addWidget(label_9, 1, 0, 1, 1);

        label_11 = new QLabel(groupBox_7);
        label_11->setObjectName(QStringLiteral("label_11"));
        label_11->setFont(font);

        gridLayout_3->addWidget(label_11, 1, 4, 1, 1);

        label_4 = new QLabel(groupBox_7);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setFont(font);

        gridLayout_3->addWidget(label_4, 0, 0, 1, 1);

        label_Start_col = new QLabel(groupBox_7);
        label_Start_col->setObjectName(QStringLiteral("label_Start_col"));
        label_Start_col->setFont(font);
        label_Start_col->setAlignment(Qt::AlignCenter);

        gridLayout_3->addWidget(label_Start_col, 0, 1, 1, 1);

        doubleSpinBox_Start_row = new QDoubleSpinBox(groupBox_7);
        doubleSpinBox_Start_row->setObjectName(QStringLiteral("doubleSpinBox_Start_row"));
        doubleSpinBox_Start_row->setFont(font);
        doubleSpinBox_Start_row->setDecimals(0);
        doubleSpinBox_Start_row->setMaximum(512);
        doubleSpinBox_Start_row->setValue(1);

        gridLayout_3->addWidget(doubleSpinBox_Start_row, 0, 6, 1, 1);

        line_2 = new QFrame(groupBox_7);
        line_2->setObjectName(QStringLiteral("line_2"));
        line_2->setFrameShape(QFrame::VLine);
        line_2->setFrameShadow(QFrame::Sunken);

        gridLayout_3->addWidget(line_2, 0, 3, 2, 1);


        gridLayout_17->addLayout(gridLayout_3, 0, 0, 1, 1);


        gridLayout->addWidget(groupBox_7, 8, 1, 2, 6);

        groupBox_6 = new QGroupBox(centralWidget);
        groupBox_6->setObjectName(QStringLiteral("groupBox_6"));
        groupBox_6->setFont(font1);
        gridLayout_18 = new QGridLayout(groupBox_6);
        gridLayout_18->setSpacing(6);
        gridLayout_18->setContentsMargins(11, 11, 11, 11);
        gridLayout_18->setObjectName(QStringLiteral("gridLayout_18"));
        gridLayout_2 = new QGridLayout();
        gridLayout_2->setSpacing(6);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        doubleSpinBox_Accum_time = new QDoubleSpinBox(groupBox_6);
        doubleSpinBox_Accum_time->setObjectName(QStringLiteral("doubleSpinBox_Accum_time"));
        doubleSpinBox_Accum_time->setFont(font);
        doubleSpinBox_Accum_time->setDecimals(3);
        doubleSpinBox_Accum_time->setSingleStep(0.001);

        gridLayout_2->addWidget(doubleSpinBox_Accum_time, 1, 3, 1, 1);

        label_8 = new QLabel(groupBox_6);
        label_8->setObjectName(QStringLiteral("label_8"));
        label_8->setFont(font);

        gridLayout_2->addWidget(label_8, 1, 5, 1, 1);

        label_7 = new QLabel(groupBox_6);
        label_7->setObjectName(QStringLiteral("label_7"));
        label_7->setFont(font);

        gridLayout_2->addWidget(label_7, 0, 5, 1, 1);

        doubleSpinBox_no_Kin = new QDoubleSpinBox(groupBox_6);
        doubleSpinBox_no_Kin->setObjectName(QStringLiteral("doubleSpinBox_no_Kin"));
        doubleSpinBox_no_Kin->setFont(font);
        doubleSpinBox_no_Kin->setDecimals(0);
        doubleSpinBox_no_Kin->setMaximum(1000);
        doubleSpinBox_no_Kin->setValue(1);

        gridLayout_2->addWidget(doubleSpinBox_no_Kin, 0, 7, 1, 1);

        label_no_Kin = new QLabel(groupBox_6);
        label_no_Kin->setObjectName(QStringLiteral("label_no_Kin"));
        label_no_Kin->setFont(font);
        label_no_Kin->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_no_Kin, 0, 6, 1, 1);

        label_Kin_time = new QLabel(groupBox_6);
        label_Kin_time->setObjectName(QStringLiteral("label_Kin_time"));
        label_Kin_time->setFont(font);
        label_Kin_time->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_Kin_time, 1, 6, 1, 1);

        doubleSpinBox_no_Accum = new QDoubleSpinBox(groupBox_6);
        doubleSpinBox_no_Accum->setObjectName(QStringLiteral("doubleSpinBox_no_Accum"));
        doubleSpinBox_no_Accum->setFont(font);
        doubleSpinBox_no_Accum->setDecimals(0);
        doubleSpinBox_no_Accum->setValue(1);

        gridLayout_2->addWidget(doubleSpinBox_no_Accum, 0, 3, 1, 1);

        label_2 = new QLabel(groupBox_6);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setFont(font);
        label_2->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);

        gridLayout_2->addWidget(label_2, 0, 1, 1, 1);

        label_Accum_time = new QLabel(groupBox_6);
        label_Accum_time->setObjectName(QStringLiteral("label_Accum_time"));
        label_Accum_time->setFont(font);
        label_Accum_time->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_Accum_time, 1, 2, 1, 1);

        label_3 = new QLabel(groupBox_6);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setFont(font);

        gridLayout_2->addWidget(label_3, 1, 1, 1, 1);

        label_no_Accum = new QLabel(groupBox_6);
        label_no_Accum->setObjectName(QStringLiteral("label_no_Accum"));
        label_no_Accum->setFont(font);
        label_no_Accum->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_no_Accum, 0, 2, 1, 1);

        doubleSpinBox_Kin_time = new QDoubleSpinBox(groupBox_6);
        doubleSpinBox_Kin_time->setObjectName(QStringLiteral("doubleSpinBox_Kin_time"));
        doubleSpinBox_Kin_time->setFont(font);
        doubleSpinBox_Kin_time->setDecimals(3);
        doubleSpinBox_Kin_time->setSingleStep(0.001);

        gridLayout_2->addWidget(doubleSpinBox_Kin_time, 1, 7, 1, 1);

        line = new QFrame(groupBox_6);
        line->setObjectName(QStringLiteral("line"));
        line->setFrameShape(QFrame::VLine);
        line->setFrameShadow(QFrame::Sunken);

        gridLayout_2->addWidget(line, 0, 4, 2, 1);


        gridLayout_18->addLayout(gridLayout_2, 0, 0, 1, 1);


        gridLayout->addWidget(groupBox_6, 6, 1, 2, 6);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_2, 0, 5, 1, 1);

        label_6 = new QLabel(centralWidget);
        label_6->setObjectName(QStringLiteral("label_6"));
        label_6->setFont(font);

        gridLayout->addWidget(label_6, 11, 1, 1, 1);

        pushButton_Cam_On = new QPushButton(centralWidget);
        pushButton_Cam_On->setObjectName(QStringLiteral("pushButton_Cam_On"));
        pushButton_Cam_On->setFont(font);

        gridLayout->addWidget(pushButton_Cam_On, 2, 5, 1, 1);

        pushButton_Browse = new QPushButton(centralWidget);
        pushButton_Browse->setObjectName(QStringLiteral("pushButton_Browse"));
        pushButton_Browse->setFont(font);

        gridLayout->addWidget(pushButton_Browse, 11, 3, 1, 1);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_3, 0, 4, 1, 1);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer, 0, 6, 1, 1);

        label = new QLabel(centralWidget);
        label->setObjectName(QStringLiteral("label"));
        label->setFont(font);

        gridLayout->addWidget(label, 2, 3, 1, 1);

        verticalSpacer_8 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_8, 8, 0, 1, 1);

        verticalSpacer_6 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_6, 6, 0, 1, 1);

        groupBox = new QGroupBox(centralWidget);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        groupBox->setFont(font1);
        gridLayout_12 = new QGridLayout(groupBox);
        gridLayout_12->setSpacing(6);
        gridLayout_12->setContentsMargins(11, 11, 11, 11);
        gridLayout_12->setObjectName(QStringLiteral("gridLayout_12"));
        gridLayout_5 = new QGridLayout();
        gridLayout_5->setSpacing(6);
        gridLayout_5->setObjectName(QStringLiteral("gridLayout_5"));
        label_Cooler_OnOff = new QLabel(groupBox);
        label_Cooler_OnOff->setObjectName(QStringLiteral("label_Cooler_OnOff"));
        label_Cooler_OnOff->setFont(font);
        label_Cooler_OnOff->setAlignment(Qt::AlignCenter);

        gridLayout_5->addWidget(label_Cooler_OnOff, 0, 1, 1, 1);

        label_Temp_disp = new QLabel(groupBox);
        label_Temp_disp->setObjectName(QStringLiteral("label_Temp_disp"));
        label_Temp_disp->setFont(font);
        label_Temp_disp->setAlignment(Qt::AlignCenter);

        gridLayout_5->addWidget(label_Temp_disp, 0, 0, 1, 1);

        doubleSpinBox_Temp_set = new QDoubleSpinBox(groupBox);
        doubleSpinBox_Temp_set->setObjectName(QStringLiteral("doubleSpinBox_Temp_set"));
        doubleSpinBox_Temp_set->setFont(font);
        doubleSpinBox_Temp_set->setDecimals(0);
        doubleSpinBox_Temp_set->setMinimum(-70);
        doubleSpinBox_Temp_set->setMaximum(30);
        doubleSpinBox_Temp_set->setValue(-30);

        gridLayout_5->addWidget(doubleSpinBox_Temp_set, 0, 2, 1, 1);

        pushButton_Temp_set = new QPushButton(groupBox);
        pushButton_Temp_set->setObjectName(QStringLiteral("pushButton_Temp_set"));
        pushButton_Temp_set->setFont(font);

        gridLayout_5->addWidget(pushButton_Temp_set, 0, 3, 1, 1);


        gridLayout_12->addLayout(gridLayout_5, 0, 0, 1, 1);


        gridLayout->addWidget(groupBox, 3, 1, 1, 6);

        verticalSpacer_5 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_5, 5, 0, 1, 1);

        horizontalSpacer_5 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_5, 0, 2, 1, 1);

        verticalSpacer_9 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_9, 9, 0, 1, 1);

        label_Cam_OnOff = new QLabel(centralWidget);
        label_Cam_OnOff->setObjectName(QStringLiteral("label_Cam_OnOff"));
        label_Cam_OnOff->setFont(font);
        label_Cam_OnOff->setAlignment(Qt::AlignCenter);

        gridLayout->addWidget(label_Cam_OnOff, 2, 4, 1, 1);

        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_2, 3, 0, 1, 1);

        verticalSpacer_7 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_7, 10, 0, 1, 1);

        groupBox_4 = new QGroupBox(centralWidget);
        groupBox_4->setObjectName(QStringLiteral("groupBox_4"));
        groupBox_4->setFont(font1);
        gridLayout_13 = new QGridLayout(groupBox_4);
        gridLayout_13->setSpacing(6);
        gridLayout_13->setContentsMargins(11, 11, 11, 11);
        gridLayout_13->setObjectName(QStringLiteral("gridLayout_13"));
        gridLayout_9 = new QGridLayout();
        gridLayout_9->setSpacing(6);
        gridLayout_9->setObjectName(QStringLiteral("gridLayout_9"));
        label_Acq_mode = new QLabel(groupBox_4);
        label_Acq_mode->setObjectName(QStringLiteral("label_Acq_mode"));
        label_Acq_mode->setFont(font);
        label_Acq_mode->setAlignment(Qt::AlignCenter);

        gridLayout_9->addWidget(label_Acq_mode, 0, 0, 1, 1);

        comboBox_Acq_mode = new QComboBox(groupBox_4);
        comboBox_Acq_mode->setObjectName(QStringLiteral("comboBox_Acq_mode"));
        comboBox_Acq_mode->setFont(font);

        gridLayout_9->addWidget(comboBox_Acq_mode, 0, 1, 1, 1);


        gridLayout_13->addLayout(gridLayout_9, 0, 0, 1, 1);


        gridLayout->addWidget(groupBox_4, 4, 1, 1, 3);

        horizontalSpacer_4 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_4, 0, 1, 1, 1);

        pushButton_Snap = new QPushButton(centralWidget);
        pushButton_Snap->setObjectName(QStringLiteral("pushButton_Snap"));
        pushButton_Snap->setFont(font);

        gridLayout->addWidget(pushButton_Snap, 11, 2, 1, 1);

        verticalSpacer_4 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_4, 4, 0, 1, 1);

        groupBox_2 = new QGroupBox(centralWidget);
        groupBox_2->setObjectName(QStringLiteral("groupBox_2"));
        groupBox_2->setFont(font1);
        gridLayout_15 = new QGridLayout(groupBox_2);
        gridLayout_15->setSpacing(6);
        gridLayout_15->setContentsMargins(11, 11, 11, 11);
        gridLayout_15->setObjectName(QStringLiteral("gridLayout_15"));
        gridLayout_7 = new QGridLayout();
        gridLayout_7->setSpacing(6);
        gridLayout_7->setObjectName(QStringLiteral("gridLayout_7"));
        doubleSpinBox_Exp_Time = new QDoubleSpinBox(groupBox_2);
        doubleSpinBox_Exp_Time->setObjectName(QStringLiteral("doubleSpinBox_Exp_Time"));
        doubleSpinBox_Exp_Time->setFont(font);
        doubleSpinBox_Exp_Time->setDecimals(3);
        doubleSpinBox_Exp_Time->setMinimum(0);
        doubleSpinBox_Exp_Time->setMaximum(5);
        doubleSpinBox_Exp_Time->setSingleStep(0.001);

        gridLayout_7->addWidget(doubleSpinBox_Exp_Time, 0, 1, 1, 1);

        label_Exp_time_disp = new QLabel(groupBox_2);
        label_Exp_time_disp->setObjectName(QStringLiteral("label_Exp_time_disp"));
        label_Exp_time_disp->setFont(font);
        label_Exp_time_disp->setAlignment(Qt::AlignCenter);

        gridLayout_7->addWidget(label_Exp_time_disp, 0, 0, 1, 1);


        gridLayout_15->addLayout(gridLayout_7, 0, 0, 1, 1);


        gridLayout->addWidget(groupBox_2, 5, 1, 1, 3);

        groupBox_8 = new QGroupBox(centralWidget);
        groupBox_8->setObjectName(QStringLiteral("groupBox_8"));
        groupBox_8->setFont(font1);
        gridLayout_6 = new QGridLayout(groupBox_8);
        gridLayout_6->setSpacing(6);
        gridLayout_6->setContentsMargins(11, 11, 11, 11);
        gridLayout_6->setObjectName(QStringLiteral("gridLayout_6"));
        gridLayout_11 = new QGridLayout();
        gridLayout_11->setSpacing(6);
        gridLayout_11->setObjectName(QStringLiteral("gridLayout_11"));
        label_Trig_mode = new QLabel(groupBox_8);
        label_Trig_mode->setObjectName(QStringLiteral("label_Trig_mode"));
        label_Trig_mode->setFont(font);
        label_Trig_mode->setAlignment(Qt::AlignCenter);

        gridLayout_11->addWidget(label_Trig_mode, 0, 0, 1, 1);

        comboBox_trig_mode = new QComboBox(groupBox_8);
        comboBox_trig_mode->setObjectName(QStringLiteral("comboBox_trig_mode"));
        comboBox_trig_mode->setFont(font);

        gridLayout_11->addWidget(comboBox_trig_mode, 0, 1, 1, 1);

        pushButton_trig_mode = new QPushButton(groupBox_8);
        pushButton_trig_mode->setObjectName(QStringLiteral("pushButton_trig_mode"));
        pushButton_trig_mode->setFont(font);

        gridLayout_11->addWidget(pushButton_trig_mode, 0, 2, 1, 1);


        gridLayout_6->addLayout(gridLayout_11, 0, 0, 1, 1);


        gridLayout->addWidget(groupBox_8, 10, 1, 1, 3);

        groupBox_9 = new QGroupBox(centralWidget);
        groupBox_9->setObjectName(QStringLiteral("groupBox_9"));
        gridLayout_21 = new QGridLayout(groupBox_9);
        gridLayout_21->setSpacing(6);
        gridLayout_21->setContentsMargins(11, 11, 11, 11);
        gridLayout_21->setObjectName(QStringLiteral("gridLayout_21"));
        gridLayout_20 = new QGridLayout();
        gridLayout_20->setSpacing(6);
        gridLayout_20->setObjectName(QStringLiteral("gridLayout_20"));
        label_VSAmp = new QLabel(groupBox_9);
        label_VSAmp->setObjectName(QStringLiteral("label_VSAmp"));
        label_VSAmp->setFont(font);
        label_VSAmp->setAlignment(Qt::AlignCenter);

        gridLayout_20->addWidget(label_VSAmp, 0, 0, 1, 1);

        pushButton_VSAmp = new QPushButton(groupBox_9);
        pushButton_VSAmp->setObjectName(QStringLiteral("pushButton_VSAmp"));
        pushButton_VSAmp->setFont(font);

        gridLayout_20->addWidget(pushButton_VSAmp, 0, 2, 1, 1);

        doubleSpinBox_VSAmp = new QDoubleSpinBox(groupBox_9);
        doubleSpinBox_VSAmp->setObjectName(QStringLiteral("doubleSpinBox_VSAmp"));
        doubleSpinBox_VSAmp->setFont(font);
        doubleSpinBox_VSAmp->setDecimals(0);
        doubleSpinBox_VSAmp->setMaximum(4);

        gridLayout_20->addWidget(doubleSpinBox_VSAmp, 0, 1, 1, 1);


        gridLayout_21->addLayout(gridLayout_20, 0, 0, 1, 1);


        gridLayout->addWidget(groupBox_9, 10, 4, 1, 3);


        gridLayout_4->addLayout(gridLayout, 0, 0, 1, 1);

        cam_gui->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(cam_gui);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 863, 21));
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
        pushButton_Save->setText(QApplication::translate("cam_gui", "Save", 0));
        groupBox_5->setTitle(QApplication::translate("cam_gui", "Read Mode", 0));
        label_Read_mode->setText(QApplication::translate("cam_gui", "N/A", 0));
        groupBox_3->setTitle(QApplication::translate("cam_gui", "EMCCD Gain", 0));
        label_EMCCDGain_disp->setText(QApplication::translate("cam_gui", "0", 0));
        pushButton_Cam_Off->setText(QApplication::translate("cam_gui", "Camera OFF", 0));
        groupBox_7->setTitle(QApplication::translate("cam_gui", "Image Area", 0));
        label_10->setText(QApplication::translate("cam_gui", "Start Row:", 0));
        label_End_col->setText(QApplication::translate("cam_gui", "512", 0));
        label_Start_row->setText(QApplication::translate("cam_gui", "1", 0));
        label_End_row->setText(QApplication::translate("cam_gui", "512", 0));
        label_9->setText(QApplication::translate("cam_gui", "End Column:", 0));
        label_11->setText(QApplication::translate("cam_gui", "End Row:", 0));
        label_4->setText(QApplication::translate("cam_gui", "Start Column:", 0));
        label_Start_col->setText(QApplication::translate("cam_gui", "1", 0));
        groupBox_6->setTitle(QApplication::translate("cam_gui", "Kinetic Settings", 0));
        label_8->setText(QApplication::translate("cam_gui", "Kinetic Cycle Time:", 0));
        label_7->setText(QApplication::translate("cam_gui", "Number in Kinetic Series:", 0));
        label_no_Kin->setText(QApplication::translate("cam_gui", "1", 0));
        label_Kin_time->setText(QApplication::translate("cam_gui", "0 s", 0));
        doubleSpinBox_no_Accum->setPrefix(QString());
        doubleSpinBox_no_Accum->setSuffix(QString());
        label_2->setText(QApplication::translate("cam_gui", "Number of Accumulations:", 0));
        label_Accum_time->setText(QApplication::translate("cam_gui", "0 s", 0));
        label_3->setText(QApplication::translate("cam_gui", "Accumulation Cycle Time:", 0));
        label_no_Accum->setText(QApplication::translate("cam_gui", "1", 0));
        label_6->setText(QApplication::translate("cam_gui", "Picture:", 0));
        pushButton_Cam_On->setText(QApplication::translate("cam_gui", "Camera ON", 0));
        pushButton_Browse->setText(QApplication::translate("cam_gui", "Browse", 0));
        label->setText(QApplication::translate("cam_gui", "Initialisation:", 0));
        groupBox->setTitle(QApplication::translate("cam_gui", "Temperature", 0));
        label_Cooler_OnOff->setText(QApplication::translate("cam_gui", "OFF", 0));
        label_Temp_disp->setText(QApplication::translate("cam_gui", "0 \302\260C", 0));
        pushButton_Temp_set->setText(QApplication::translate("cam_gui", "Set", 0));
        label_Cam_OnOff->setText(QApplication::translate("cam_gui", "OFF", 0));
        groupBox_4->setTitle(QApplication::translate("cam_gui", "Acquisition Mode", 0));
        label_Acq_mode->setText(QApplication::translate("cam_gui", "N/A", 0));
        pushButton_Snap->setText(QApplication::translate("cam_gui", "Snap", 0));
        groupBox_2->setTitle(QApplication::translate("cam_gui", "Exposure Time", 0));
        label_Exp_time_disp->setText(QApplication::translate("cam_gui", "0 s", 0));
        groupBox_8->setTitle(QApplication::translate("cam_gui", "Trigger Mode", 0));
        label_Trig_mode->setText(QApplication::translate("cam_gui", "N/A", 0));
        pushButton_trig_mode->setText(QApplication::translate("cam_gui", "Set Trigger Mode", 0));
        groupBox_9->setTitle(QApplication::translate("cam_gui", "Set Vertical Clock Voltage Amplitude", 0));
        label_VSAmp->setText(QApplication::translate("cam_gui", "0 V", 0));
        pushButton_VSAmp->setText(QApplication::translate("cam_gui", "Set Voltage", 0));
    } // retranslateUi

};

namespace Ui {
    class cam_gui: public Ui_cam_gui {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CAM_GUI_H
