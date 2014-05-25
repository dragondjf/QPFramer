import QtQuick 2.0
import "../component"

TabWidget {
    gcolor: "green"

    Rectangle {
        id: page1
        objectName: "page1"
        property string title: "Red"
        property string icon: "../images/icons/dark/appbar.tree.leaf.png"
        
        signal clicked()

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

                MouseArea {
                    anchors.fill: parent
                    cursorShape: Qt.PointingHandCursor
                    hoverEnabled: false
                    onEntered: {}
                    onExited: {}
                    onWheel: {}
                    onClicked: {
                        page1.clicked();
                        parent.text = "clicked";
                    }
                }
            }
        }
    }

    Rectangle {
        id: page2
        objectName: "page2"
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
        id: page3
        objectName: "page3"
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
