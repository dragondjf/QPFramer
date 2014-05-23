import QtQuick 2.0

Flipable {
    id: button

    property string text: '545454'

    signal clicked(int x, int y)

    width: 120
    height: 120

    front: Rectangle{
        anchors.fill: parent
        color: "green"
        Text{
            text: button.text
            anchors.centerIn: parent
        }
    }
    back: Rectangle{
        anchors.fill: parent
        color: "green"
        Text{
            text: button.text
            anchors.centerIn: parent
        }
    }

    transform: Rotation {
        id: rotation
        origin.x: button.width/2
        origin.y: button.height/2
        axis.x: 1; axis.y: 0; axis.z: 0     // set axis.y to 1 to rotate around y-axis
        angle: 0    // the default angle
    }

    states: [
        State {
            name: "font"
            PropertyChanges { target: rotation; angle: 180 }
        },
        State {
            name: "back"
            PropertyChanges { target: rotation; angle: 0 }
        }
    ]

    transitions: Transition {
        NumberAnimation { target: rotation; property: "angle"; duration: 800 }
    }

    MouseArea {
        anchors.fill: parent
        hoverEnabled: true
        onEntered: {
            button.state = 'font'
        }
        onExited: {
            button.state = 'back'
        }

        onPressed:{
            console.log('onPressed')
        }
        onReleased:{
            // button.front.color = "green"
            console.log('onReleased')
        }

        onClicked:{
            console.log('onClicked')
            button.clicked(mouse.mouseX, mouse.mouseY);
        } 
    }
}