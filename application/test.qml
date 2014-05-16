import QtQuick 2.0
import QtQuick.Window 2.1
import QtQuick.Controls 1.1

ApplicationWindow {
    id: root
    width: 800
    height: 600
    color: 'green'
    // flags: Qt.Window| Qt.FramelessWindowHint

    property bool isfullscreen: false

    Rectangle{
        anchors.fill: parent
        gradient: Gradient {
            GradientStop { position: 0.0; color: "red" }
            GradientStop { position: 0.33; color: "yellow" }
            GradientStop { position: 1.0; color: "green" }
        }

        MouseArea {
            anchors.fill: parent
            onClicked: label.moveTo(mouse.x, mouse.y)
        }

        Text {
            id: label

            function moveTo(newX, newY) {
                label.x = newX;
                label.y = newY;
            }

            text: "Move me!"
        }

        // Flickable {
        //     anchors.fill: parent
        //     contentWidth: image.width; contentHeight: image.height
        //     Image { id: image; source: "images/butterfly_bak.png" }
        // }
        focus: true
        Keys.onPressed: {
            if (event.key == Qt.Key_F1){
                console.log(root.windowState)
                if(root.isfullscreen == true)
                {
                    root.showNormal();
                    root.isfullscreen = false;
                }
                else{
                    root.showFullScreen();
                    root.isfullscreen = true;         
                }
            }
        }
        Keys.onEscapePressed:{
            root.close();
        }
    }

    Row {
        Repeater {
            model: 300
            Rectangle {
                width: 5; height: 5
                border.width: 1
                color: "yellow"
            }
        }
    }

    Row {
        anchors.bottom: parent.bottom
        Repeater {
            model: 300
            Rectangle {
                width: 5; height: 5
                border.width: 1
                color: "yellow"
            }
        }
    }

    Column{
        Repeater {
            model: 300
            Rectangle {
                width: 5; height: 5
                border.width: 1
                color: "yellow"
            }
        }
    }

    Column{
        anchors.right: parent.right
        Repeater {
            model: 300
            Rectangle {
                width: 5; height: 5
                border.width: 1
                color: "yellow"
            }
        }
    }


    function moveTo(obj, newX, newY) {
        obj.x = newX;
        obj.y = newY;
    }
}
