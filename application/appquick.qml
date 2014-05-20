import QtQuick 2.0
import QtQuick.Window 2.1
import QtQuick.Controls 1.1
import QtQuick.Layouts 1.0
import "component"

Rectangle{
    id: mainwindow

    property bool isfullscreen: false

    signal minClicked()
    signal fullscreen()
    signal maxClicked()
    signal closeClicked()

    width: Screen.desktopAvailableWidth * 0.8
    height:Screen.desktopAvailableHeight * 0.8
    gradient: Gradient {
        GradientStop {id: start; position: 0.0; color: skinbar.startcolor }
        GradientStop {id: middle; position: 0.5; color: skinbar.middlecolor }
        GradientStop {id: stop; position: 1.0; color: skinbar.stopcolor }
    }

    TitleBar{
        id: titlebar
        title: mainconfig.title
        height: 25
        anchors.margins: 0
        isfullscreen: mainwindow.isfullscreen
        skinIsVisible: false

        skinIcon: "../images/icons/dark/appbar.clothes.shirt.png"
        skinHoverIcon: "../images/icons/light/appbar.clothes.shirt.png"
        dropdownmenuIcon: "../images/icons/dark/appbar.control.down.png"
        dropdownmenuHoverIcon: "../images/icons/light/appbar.control.down.png"
        minIcon: "../images/icons/dark/appbar.minus.png"
        minHoverIcon: "../images/icons/light/appbar.minus.png"
        maxIcon: "../images/icons/dark/appbar.fullscreen.box.png"
        maxHoverIcon: "../images/icons/light/appbar.fullscreen.box.png"
        normalIcon: "../images/icons/dark/appbar.app.png"
        normalHoverIcon: "../images/icons/light/appbar.app.png"
        closeIcon: "../images/icons/dark/appbar.close.png"
        closeHoverIcon: "../images/icons/light/appbar.close.png"

        onMinClicked:{
            mainwindow.minClicked()
        }

        onMaxClicked:{
            mainwindow.isfullscreen = !mainwindow.isfullscreen;
            mainwindow.maxClicked();
            skinbar.animationEnabled = false
            skinbar.x = parent.width
        }

        onCloseClicked:{
            Qt.quit();
        }

        onDoubleClicked:{
            titlebar.maxClicked();
        }

        onSkinHovered:{
            skinbar.animationEnabled = true
            if(skinbar.x == parent.width){
                skinbar.opacity = 1
                skinbar.x = parent.width - skinbar.width
            }else{
                skinbar.x = parent.width
                skinbar.opacity = 0
            }
        }
    }

    HorizontalSeparator{
        id: horizontalseparator
        height: 0
        color: "transparent"
        anchors.top: titlebar.bottom
    }

    SkinBar{
        id: skinbar
        parentWidth: parent.width
        width: titlebar.height * 12
        height: titlebar.height
        anchors.top: titlebar.bottom
        startcolor: "green"
        middlecolor: "yellow"
        stopcolor: "white"
        animationEnabled: false
        opacity:0
        z: 100
    }

    CenterWindow{
        id: centerwindow
        width: parent.width
        anchors.left: parent.left
        anchors.top: horizontalseparator.bottom
        anchors.right: parent.right
        anchors.bottom: statusbar.top
        // color: "transparent"
        gradient: Gradient {
            GradientStop { position: 0.0; color: skinbar.startcolor }
            GradientStop { position: 0.5; color: skinbar.middlecolor }
            GradientStop { position: 1.0; color: skinbar.stopcolor }
        }

        SideBar{
            id: leftsidebar
            // width: 200
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.left: parent.left
            color: "#154784"
            opacity: 1
            NumberAnimation on width { to: 200; duration: 1000}
        }

        SideBar{
            id: rightsidebar
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.left: leftsidebar.right
            anchors.right: parent.right
            color: "#154784"

            function rightshow(){
                if(rightsidebar.state == "primary_x"){
                    rightsidebar.state = "right_x"
                }else{
                    rightsidebar.state = "primary_x"
                }
            }

            state: "primary_x"

            states: [
                State {
                    name: "primary_x"
                    AnchorChanges { target: rightsidebar; anchors.left: leftsidebar.right }
                },
                State {
                    name: "right_x"
                    AnchorChanges { target: rightsidebar; anchors.left: parent.right }
                }
            ]

            transitions: [
                Transition {
                    AnchorAnimation { duration: 1000 }
                }
            ]
        }

        MouseArea {
            id: centerwindowmouseArea
            anchors.fill: parent
            hoverEnabled: true
            // propagateComposedEvents: true
            onPositionChanged: {
                if(mouse.x < 200){
                    leftsidebar.opacity = 1;
                }else{
                    leftsidebar.opacity = 0;
                }
            }
        }
    }

    StatusBar{
        id:statusbar
        height: 40
        mainwindowwidth: parent.width
        mainwindowheight: parent.height
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        color: "green"
        // onSizegripChanged:{
        //     var sizeIncrease = (x - statusbar.enterX > 0) && (y - statusbar.enterY > 0)
        //     var sizeDecrease = (x - statusbar.enterX < 0) && (y - statusbar.enterY < 0)
        //     if(sizeIncrease || sizeDecrease){
        //         mainwindow.width =  mainwindow.width + x - statusbar.enterX;
        //         mainwindow.height = mainwindow.height + y - statusbar.enterY;
        //     }
        // }
    }

    focus: true
    Keys.onPressed: {
        if (event.key == Qt.Key_F11){
           mainwindow.isfullscreen = !mainwindow.isfullscreen;
           mainwindow.fullscreen();
        }
        if (event.key == Qt.Key_F10){
           mainwindow.isfullscreen = !mainwindow.isfullscreen;
           mainwindow.maxClicked();
        }
        if (event.key == Qt.Key_F12){
            rightsidebar.toggleshow()
        }
        if (event.key == Qt.Key_Up){
            rightsidebar.toggleshow()
        }
        if (event.key == Qt.Key_Down){
            rightsidebar.toggleshow()
        }
        if (event.key == Qt.Key_Left){
            rightsidebar.toggleshow()
        }
        if (event.key == Qt.Key_Right){
            rightsidebar.rightshow()
        }
    }
    Keys.onDigit0Pressed:{
        console.log("2221");
        rightsidebar.toggleshow();
    }

    Keys.onEscapePressed:{
        Qt.quit();
    }

}
