import QtQuick 2.0

Rectangle{
    id: root

    property int zindex

    width: root.width / 2
    height: root.height
    color: "white"
    state: 'Font'

    signal clicked()

    Rectangle{
    	width: 1
	    height: root.height
    	anchors.left: parent.left
    	color: "black"
    }
    border.width:2
    border.color: "red"

    MouseArea{
    	id: mouseA
        anchors.fill: parent
        onClicked:{
            
            root.clicked()
        }
    }

    onClicked:{
    	if (root.state == 'Font'){
            root.state = 'Back';
        }
        else{
            root.state = 'Font';
        }
    }

    states: [
        State {
            name: "Font"
            PropertyChanges {
                target: rotate
                angle: 2
            }
            PropertyChanges {
                target: root
                z: 0
            }
        },
        State {
            name: "Back"
            PropertyChanges {
                target: rotate
                angle: -90
            }
            PropertyChanges {
                target: root
                z: zindex
            }
        }
    ]

    transform: [
        Rotation {
            id: rotate; angle: 0; origin.y: root.height / 2 ; origin.x: 0 ;  axis { x: 0; y: 1; z: 0 }
            Behavior on angle {
                NumberAnimation { easing.type: Easing.OutBack; duration: 1000 }
            }
        }
    ]
}