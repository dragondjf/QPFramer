import QtQuick 2.0
import QtQuick.Window 2.1
import QtQuick.Controls 1.1
import "component"


ApplicationWindow {
    id: mainwindow

    property bool isfullscreen: false
    property int dragpoistionX
    property int dragpoistionY

    function showWindow(){
        if(mainwindow.isfullscreen == true)
            {
                mainwindow.showNormal();
                mainwindow.isfullscreen = false;
            }
        else{
            mainwindow.showFullScreen();
            mainwindow.isfullscreen = true;         
            }
    }

    width: 800
    height: 600
    color: 'green'
    flags: Qt.Window| Qt.FramelessWindowHint
    title: 'QFramer'
    Rectangle{
        anchors.fill: parent
        gradient: Gradient {
            GradientStop { position: 0.0; color: "red" }
            GradientStop { position: 0.33; color: "yellow" }
            GradientStop { position: 1.0; color: "green" }
        }

        TitleBar{
            id: titlebar
            title: '564'
            height: 30
            isfullscreen: mainwindow.isfullscreen

            minIcon: "../images/icons/dark/appbar.minus.png"
            minHoverIcon: "../images/icons/light/appbar.minus.png"
            maxIcon: "../images/icons/dark/appbar.fullscreen.box.png"
            maxHoverIcon: "../images/icons/light/appbar.fullscreen.box.png"
            normalIcon: "../images/icons/dark/appbar.app.png"
            normalHoverIcon: "../images/icons/light/appbar.app.png"
            closeIcon: "../images/icons/dark/appbar.close.png"
            closeHoverIcon: "../images/icons/light/appbar.close.png"

            onMinClicked:{
                mainwindow.showMinimized()
            }

            onMaxClicked:{
                mainwindow.showWindow();
            }

            onCloseClicked:{
                Qt.quit();
            }

            onDoubleClicked:{
                console.log('222')
                mainwindow.showWindow();
            }

            // MouseArea{
            //     anchors.fill: parent
            //     propagateComposedEvents: true
            //     onPressed:{
            //         // root.dragpoistionY = mouse.y
            //         mainwindow.dragpoistionX =  mapToItem(parent, mouse.x).x - mainwindow.x
            //         mainwindow.dragpoistionY = mapToItem(parent, mouse.y).y - mainwindow.y
            //         // mouse.accepted = true
            //     }
            //     onReleased:{
            //         mainwindow.dragpoistionX = mouse.x
            //         mainwindow.dragpoistionY = mouse.y
            //     }
            //     onPositionChanged:{
            //         mainwindow.x = mapToItem(parent, mouse.x).x - mainwindow.dragpoistionX
            //         mainwindow.y = mapToItem(parent, mouse.y).y - mainwindow.dragpoistionY
            //         // mouse.accepted = true

            //     }
            // }
        }

        HorizontalSeparator{
            id: horizontalseparator
            height: 2
            color: "lightgreen"
            anchors.top: titlebar.bottom
        }




        focus: true
        Keys.onPressed: {
            if (event.key == Qt.Key_F1){
                mainwindow.showWindow();
            }
        }
        Keys.onEscapePressed:{
            mainwindow.close();
        }

        
    }
}
