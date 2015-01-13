import QtQuick 2.0

Row {
    id: sysbtngrp
    spacing: 0

    signal min
    signal close

    SysBtn {
        id: min
        color: "transparent"
        picNormal: "res/img/min_normal.png"
        picHovered: "res/img/min_hover.png"
        picPressed: "res/img/min_pressed.png"
        onClicked: sysbtngrp.min()
    }
    SysBtn {
        id: close
        color: "transparent"
        picNormal: "res/img/close_normal.png"
        picHovered: "res/img/close_hover.png"
        picPressed: "res/img/close_pressed.png"
        onClicked: sysbtngrp.close()
    }
}
