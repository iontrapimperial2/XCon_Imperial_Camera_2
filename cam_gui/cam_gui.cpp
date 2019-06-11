#include "cam_gui.h"
#include "ui_cam_gui.h"

cam_gui::cam_gui(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::cam_gui)
{
    ui->setupUi(this);
}

cam_gui::~cam_gui()
{
    delete ui;
}
