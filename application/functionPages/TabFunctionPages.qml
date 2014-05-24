import QtQuick 2.0
import "../component"

TabWidget {
    id: tabs
    gcolor: "green"

    Rectangle {
        property string title: "Red"
        property string icon: "../images/icons/dark/appbar.tree.leaf.png"
        anchors.fill: parent
        color: "transparent"

        Rectangle {
            anchors.fill: parent; anchors.margins: 0
            color: "#ff7f7f"
            Text {
                width: parent.width - 20
                anchors.centerIn: parent; horizontalAlignment: Qt.AlignHCenter
                text: "Roses are red"
                font.pixelSize: 20
                wrapMode: Text.WordWrap
            }
        }
    }

    Rectangle {
        property string title: "Green"
        property string icon: "../images/icons/dark/appbar.tree.leaf.three.png"
        anchors.fill: parent
        color: "transparent"

        Rectangle {
            anchors.fill: parent; anchors.margins: 0
            color: "#7fff7f"
            Text {
                width: parent.width - 20
                anchors.centerIn: parent; horizontalAlignment: Qt.AlignHCenter
                text: "Flower stems are green"
                font.pixelSize: 20
                wrapMode: Text.WordWrap
            }
        }
    }

    Rectangle {
        property string title: "Blue"
        property string icon: "../images/icons/dark/appbar.tree.pine.png"
        anchors.fill: parent
        color: "transparent"

        Rectangle {
            anchors.fill: parent; anchors.margins: 0
            color: "#7f7fff"
            Text {
                width: parent.width - 20
                anchors.centerIn: parent; horizontalAlignment: Qt.AlignHCenter
                text: "Violets are blue"
                font.pixelSize: 20
                wrapMode: Text.WordWrap
            }
        }
    }
}
