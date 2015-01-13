import QtQuick 2.0
import QtQuick.Controls 1.0
import QtQuick.Controls.Styles 1.0

Slider {
    id:aass
    anchors.centerIn: parent
    property string grooveColor: "black"
    property string handleColor: "white"
    property int ctlx: 0
    value: 0
    style: SliderStyle {
        id: ss
        groove: Rectangle {
            implicitWidth: 200
            implicitHeight: 5
            color: grooveColor
            radius: 0
            Rectangle {
                anchors.left: parent.left
                radius: 0
                height: 5

                width: control.value/aass.maximumValue*aass.width
                color: handleColor
            }
        }
        handle: Rectangle {
            anchors.centerIn: parent
            color: handleColor

            width: 10
            height: 10
            radius: 10

        }
    }
}
