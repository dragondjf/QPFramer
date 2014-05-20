import QtQuick 2.0

Rectangle {
    id: page
    width: 640; height: 480
    color: "#343434"
    

    Rectangle {
        id: topLeftRect

        function rightshow(){
            if(topLeftRect.state == "primary_x"){
                topLeftRect.state = "right_x"
                console.log('12121212')
            }else{
                topLeftRect.state = "primary_x"
            }
        }

        anchors { left: parent.left; top: parent.top; leftMargin: 10; topMargin: 20 }
        width: 46; height: 54
        color: "Transparent"; border.color: "Gray"; radius: 6
        state: "primary_x"
        // Clicking in here sets the state to the default state, returning the image to
        // its initial position
        MouseArea { anchors.fill: parent; onClicked: topLeftRect.rightshow() }

        states: [
        State {
            name: "primary_x"
            PropertyChanges { target: topLeftRect; x: 200 }
        },
        State {
            name: "right_x"
            PropertyChanges { target: topLeftRect; x: 400}
        }
    ]

    transitions: [
        Transition {
            from: "primary_x"
            to: "right_x"
            NumberAnimation { target: topLeftRect; property: "x"; duration: 1000}
        },
        Transition {
            from: "right_x"
            to: "primary_x"
            NumberAnimation { target: topLeftRect; property: "x"; duration: 1000}
        }
    ]
    }

   

    
}