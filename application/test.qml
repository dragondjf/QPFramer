import QtQuick 2.0
import "loading/loading.js" as Loading 

Rectangle {
    id: page

    property var ls

    width: 1000; height: 480
    color: Qt.application.active ? "white" : "lightgray"
    opacity: Qt.application.active ? 1.0 : 0
    Rectangle {
        id: topLeftRect

        function rightshow(){
            if(topLeftRect.state == "primary_x"){
                topLeftRect.state = "right_x"
                console.log(Qt.platform.os)
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

    function loading(parent) {
        var ls = [];
        var component = Qt.createComponent("loading.qml");
        for (var i=0; i<10; i++) {
            var object = component.createObject(parent);
            object.pwidth = parent.width + i * 10;
            object.x = object.pwidth - i * 30;
            ls[i] = object
        }
        return ls
    }

    function loadingfinsih(ls){
        for(var i=0, len=ls.length; i < len; i++){
            if(ls[i] != undefined){
                ls[i].destroy();
            }
        }
        ls = []
        return ls
    }

    Component.onCompleted: {
        // page.ls = Loading.loading(page);
        // console.log(page.ls)
    }

    MouseArea {
        anchors.fill: parent
        cursorShape: Qt.PointingHandCursor
        hoverEnabled: false
        onEntered: {}
        onExited: {}
        onWheel: {}
        onClicked: {
            page.ls = Loading.loadingfinsih(page.ls)
        }
        onDoubleClicked:{
            page.ls = Loading.loading(page);
        }
    }
}