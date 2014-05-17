import QtQuick 2.0
import QtQuick.Window 2.1
import QtQuick.Controls 1.1
import QtQuick.Controls.Styles 1.1

ApplicationWindow {
    id: root
    width: 800
    height: 600
    color: 'green'
    flags: Qt.Window| Qt.FramelessWindowHint

    property bool isfullscreen: false
    property int dragpoistionX
    property int dragpoistionY

    function showWindow(){
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

    Rectangle{
        id: bg
        anchors.fill: parent
        gradient: Gradient {
            GradientStop { position: 0.0; color: "red" }
            GradientStop { position: 0.33; color: "yellow" }
            GradientStop { position: 1.0; color: "green" }
        }
        focus: true

        MouseArea{
            anchors.fill: parent
            onDoubleClicked: { showWindow() }
            onPressed:{
                // root.dragpoistionY = mouse.y
                root.dragpoistionX =  mapToItem(bg, mouse.x).x - root.x
                root.dragpoistionY = mapToItem(bg, mouse.y).y - root.y
                mouse.accepted = true
            }
            onReleased:{
                root.dragpoistionX = mouse.x
                root.dragpoistionY = mouse.y
            }
            onPositionChanged:{
                root.x = mapToItem(bg, mouse.x).x - root.dragpoistionX
                root.y = mapToItem(bg, mouse.y).y - root.dragpoistionY
                mouse.accepted = true

            }
        }

        Keys.onPressed: {
            if (event.key == Qt.Key_F1){
                showWindow()
            }
        }
        Keys.onEscapePressed:{
            root.close();
        }
    }
    TabView {
        id: frame
        anchors.fill: bg
        anchors.topMargin: 30
        Tab { 
            id: tab1
            title: "Tab 1" 
            Rectangle{
                anchors.fill: parent
                color: "transparent"
                Flickable {
                    anchors.fill: parent
                    contentWidth: image.width; contentHeight: image.height
                    Image { id: image; source: "images/butterfly_bak.png" }
                }
                focus: true
            }
        }
        Tab { 
            id: tab2
            title: "Tab 2" 
        }
        Tab { title: "Tab 3" }

        style: TabViewStyle {
            frameOverlap: 1
            tabsMovable: true
            padding.left: 1000
            tabsAlignment: Qt.AlignHCenter
            leftCorner: Rectangle {
                width: 10
                height: 10
                color: 'green'
            }
            tab: Rectangle {
                id: tab
                color: styleData.selected ? "steelblue" :"lightsteelblue"
                border.color:  "steelblue"
                border.width: 2
                implicitWidth: Math.max(text.width + 4, 80)
                implicitHeight: 60
                radius: 2
                Text {
                    id: text
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.bottom: parent.bottom
                    anchors.bottomMargin: 5
                    // anchors.fill: parent
                    text: styleData.title
                    color: styleData.selected ? "white" : "black"
                    Image {
                        id: image
                        // anchors.fill: parent
                        anchors.horizontalCenter: parent.horizontalCenter
                        anchors.bottom: text.top
                        // anchors.top: 0
                        width: 50
                        height: 50
                        Component.onCompleted: {
                            if(styleData.title == tab1.title){
                                image.source="images/butterfly_bak.png"
                            }
                            if(styleData.title == tab2.title){
                                image.source="images/butterfly_bak.png"
                            }
                        }
                    }
                }

            }
            frame: Rectangle { color: 'transparent' }
        }
    }

    // Row {
    //     Repeater {
    //         model: 300
    //         Rectangle {
    //             width: 5; height: 5
    //             border.width: 1
    //             color: "yellow"
    //         }
    //     }
    // }

    // Row {
    //     anchors.bottom: parent.bottom
    //     Repeater {
    //         model: 300
    //         Rectangle {
    //             width: 5; height: 5
    //             border.width: 1
    //             color: "yellow"
    //         }
    //     }
    // }

    // Column{
    //     Repeater {
    //         model: 300
    //         Rectangle {
    //             width: 5; height: 5
    //             border.width: 1
    //             color: "yellow"
    //         }
    //     }
    // }

    // Column{
    //     anchors.right: parent.right
    //     Repeater {
    //         model: 300
    //         Rectangle {
    //             width: 5; height: 5
    //             border.width: 1
    //             color: "yellow"
    //         }
    //     }
    // }
}
