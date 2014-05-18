import QtQuick 2.0
import QtQuick.Window 2.1
import QtQuick.Controls 1.1
import QtQuick.Layouts 1.0
import "component"

Rectangle{
    id: mainwindow

    property bool isfullscreen: false

    signal minClicked()
    signal maxClicked()
    signal closeClicked()

    width: Screen.desktopAvailableWidth * 0.8
    height:Screen.desktopAvailableHeight * 0.8
    gradient: Gradient {
        GradientStop {id: start; position: 0.0; color: skinbar.startcolor }
        GradientStop {id: middle; position: 0.5; color: skinbar.middlecolor }
        GradientStop {id: stop; position: 1.0; color: skinbar.stopcolor }
    }

    function showWindow(){
        if(mainwindow.isfullscreen == true){
            mainwindow.isfullscreen = false;
        }
        else{
            mainwindow.isfullscreen = true;
        }
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
            mainwindow.showWindow();
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
                
                skinbar.x = parent.width - skinbar.width
            }else{
                skinbar.x = parent.width
            }
        }
    }

    HorizontalSeparator{
        id: horizontalseparator
        height: 0
        color: "lightgreen"
        anchors.top: titlebar.bottom
    }

    SkinBar{
        id: skinbar
        parentWidth: parent.width
        width: titlebar.height * 12
        height: titlebar.height
        anchors.top: horizontalseparator.bottom
        startcolor: "green"
        middlecolor: "yellow"
        stopcolor: "white"
        animationEnabled: false
    }
    focus: true
    Keys.onPressed: {
        if (event.key == Qt.Key_F11){
            mainwindow.maxClicked()
        }
    }
    Keys.onEscapePressed:{
        Qt.quit();
    }

}
