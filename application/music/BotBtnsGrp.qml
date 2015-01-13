import QtQuick 2.0

Rectangle {
    height: add.height
    color: "transparent"

    signal addClick
    signal locClick
    signal plyClick
    signal schClick

    SysBtn{
        id: add
        anchors.left: parent.left
        anchors.leftMargin: 10
        picNormal: "res/img/Add_normal.png"
        picHovered: "res/img/Add_normal.png"
        picPressed:  "res/img/Add_normal.png"
        onClicked: addClick()
    }
    SysBtn{
        id: locate
        anchors.left: add.right
        anchors.leftMargin: 10
        picNormal: "res/img/locale_normal.png"
        picHovered: "res/img/locale_normal.png"
        picPressed:  "res/img/locale_normal.png"
        onClicked: locClick()
    }
    SysBtn{
        id: play_way
        anchors.left: locate.right
        anchors.leftMargin: 10
        picNormal: "res/img/Play_way.png"
        picHovered: "res/img/Play_way.png"
        picPressed:  "res/img/Play_way.png"
        onClicked: plyClick()
    }
    SysBtn{
        id: search_btn
        anchors.left: play_way.right
        anchors.leftMargin: 10
        picNormal: "res/img/Search_normal.png"
        picHovered: "res/img/Search_normal.png"
        picPressed:  "res/img/Search_normal.png"
        onClicked: schClick()
    }
}
