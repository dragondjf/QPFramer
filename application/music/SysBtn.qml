import QtQuick 2.0


Rectangle {
    id: sysbtn

    property string currentPic: ""
    property string picHovered: ""
    property string picNormal: ""
    property string picPressed: ""

    signal clicked
    signal hovered
    signal exited

    width: ima.width
    height: ima.height
    state: "normal"
    color: "transparent"

    Image {
        id: ima
        source: currentPic
    }
    MouseArea {
        hoverEnabled: true
        anchors.fill: parent

        onEntered: {
            hovered();
            sysbtn.state=="pressed"?sysbtn.state="pressed":sysbtn.state="hovered";
        }
        onExited: {
            sysbtn.exited();
            sysbtn.state=="pressed"?sysbtn.state="pressed":sysbtn.state="normal";
        }

        onPressed: sysbtn.state = "pressed"
        onReleased: {
            sysbtn.state = "normal"
            sysbtn.clicked()
        }
    }
    states: [
        State {
            name: "normal"
            PropertyChanges {
                target: sysbtn
                currentPic:picNormal
            }
        },
        State {
            name: "hovered"
            PropertyChanges {
                target: sysbtn
                currentPic:picHovered
            }
        },
        State {
            name: "pressed"
            PropertyChanges {
                target: sysbtn
                currentPic:picPressed
            }
        }
    ]
}
