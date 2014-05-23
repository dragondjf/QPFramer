import QtQuick 2.0

Item {
    width: 200; height: 200

    DropArea {
        x: 75; y: 75
        width: 50; height: 50

        Rectangle {
            anchors.fill: parent
            color: "green"

            visible: parent.containsDrag
        }
    }

    Rectangle {
        x: 10; y: 10
        width: 20; height: 20
        color: "red"

        Drag.active: dragArea.drag.active
        Drag.hotSpot.x: 10
        Drag.hotSpot.y: 10

        MouseArea {
            id: dragArea
            anchors.fill: parent

            drag.target: parent
        }
    }
}