#ifndef CAM_GUI_H
#define CAM_GUI_H

#include <QMainWindow>

namespace Ui {
class cam_gui;
}

class cam_gui : public QMainWindow
{
    Q_OBJECT

public:
    explicit cam_gui(QWidget *parent = nullptr);
    ~cam_gui();

private:
    Ui::cam_gui *ui;
};

#endif // CAM_GUI_H
