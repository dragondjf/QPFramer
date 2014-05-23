import QtQuick 2.0

Flipable {
    id: button

    property string text: '545454'
    property string color: 'green'

    signal clicked(int x, int y)

    width: 60
    height: 40

    front: Rectangle{
        anchors.fill: parent
        color: mousearea.pressed? 'lightgreen': 'green'

        MouseArea{
            propagateComposedEvents: true
            onClicked: {
                console.log('front clicked')
                mouse.accepted = false
            }
        }

        Text{
            text: button.text
            anchors.centerIn: parent
            font: { font.pointSize=10; font.weight=Font.Bold}
            color: 'white'
        }
    }
    back: Rectangle{
        anchors.fill: parent
        color: mousearea.pressed? 'lightgreen': 'green'

        MouseArea{
            propagateComposedEvents: true
            onClicked: {
                mouse.accepted = false
            }
        }

        Text{
            text: button.text
            anchors.centerIn: parent
            color: "white"
            font: { font.pointSize=10; font.weight=Font.Bold}
        }
    }

    MouseArea {
        id: mousearea
        anchors.fill: parent
        hoverEnabled: true
        propagateComposedEvents: true
        onEntered: {
            parent.state = 'font'
        }
        onExited: {
            parent.state = 'back'
        }
        onClicked:{
            button.clicked(mouse.mouseX, mouse.mouseY);
            mouse.accepted = true
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

}
