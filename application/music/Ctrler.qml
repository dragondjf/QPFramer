import QtQuick 2.0

Rectangle {
    color: "transparent"
    signal prev
    signal play
    signal next
    property real vol: 1

    SwitchBtn {
        id: lyrics
        anchors.right: lyr_note.left
        anchors.verticalCenter: parent.verticalCenter
        onPic: "res/img/Toggle_on.png"
        offPic: "res/img/Toggle_off.png"
    }
    Text {
        id: lyr_note
        text: qsTr("歌词")
        color: "#ffffff"
        anchors.right: prev.left
        anchors.rightMargin: 20
        anchors.verticalCenter: parent.verticalCenter
    }

    SysBtn {
        id: prev
        anchors.verticalCenter: parent.verticalCenter
        anchors.right: play.left
        anchors.rightMargin: 10
        picNormal: "res/img/Prev_normal.png"
        picHovered: "res/img/Prev_normal.png"
        picPressed: "res/img/Prev_click.png"
        onClicked: parent.prev()
    }

    SysBtn {
        id: play
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        picNormal: "res/img/Play_normal.png"
        picHovered: "res/img/Play_normal.png"
        picPressed: "res/img/Play_click.png"

        property real prevWidth: 0

        onClicked: parent.play()
//        onWidthChanged: {
//            prev.anchors.rightMargin = 10 + (prevWidth - width)/2;
//            prevWidth = width;
//        }
    }
    SysBtn {
        id: next
        anchors.verticalCenter: parent.verticalCenter
        anchors.left: play.right
        anchors.leftMargin: 10
        picNormal: "res/img/next_normal.png"
        picHovered: "res/img/next_normal.png"
        picPressed: "res/img/next_click.png"
        onClicked: parent.next()
    }
    SliderBar {
        id: volume
        x: 83
        y: -8
        width: 98
        height: 15
        anchors.verticalCenterOffset: 0
        anchors.horizontalCenterOffset: 132
        anchors.left: next.right
        anchors.leftMargin: 188
        anchors.verticalCenter: parent.verticalCenter
        anchors.right: parent.right
        anchors.rightMargin: -117
        grooveColor: "#D3D3D3"
        value: 1
        onValueChanged: {
            if(volume.pressed == true){
                vol = value;
            }
        }
    }

}
