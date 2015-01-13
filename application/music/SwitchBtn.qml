import QtQuick 2.0


Rectangle {
    id: switchbtn
    width: ima.width
    height: ima.height
    color: "transparent"
    state: "off"

    property string curPic: ""
    property string onPic: ""
    property string offPic: ""

    signal turnOn
    signal turnOff

    Image {
        id: ima
        source: curPic
    }
    MouseArea {
        anchors.fill: parent
        onClicked: {
            if(switchbtn.state == "off"){
                switchbtn.state = "on"
                switchbtn.turnOn()
            }else{
                switchbtn.state = "off"
                switchbtn.turnOff()
            }
        }
    }

    states: [
        State {
            name: "on"
            PropertyChanges {
                target: switchbtn
                curPic: onPic
            }
        },
        State {
            name: "off"
            PropertyChanges {
                target: switchbtn
                curPic: offPic
            }
        }
    ]
}
