import QtQuick 2.0
import QtQuick.Window 2.1
import QtQuick.Controls 1.1
import "js/app.js" as App

Rectangle{
    id: mainwindow

    property bool isfullscreen: false

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

    function showFullScreen(){
        mainwindow.x = 0;
        mainwindow.y = 0;
        mainwindow.width = Screen.desktopAvailableWidth;
        mainwindow.height = Screen.desktopAvailableHeight;
    }

    function showNormal(){
        mainwindow.width = Screen.desktopAvailableWidth * 0.8;
        mainwindow.height = Screen.desktopAvailableHeight * 0.8;
    }

    x: 0
    y: 0
    width: Screen.desktopAvailableWidth * 0.8
    height:Screen.desktopAvailableHeight * 0.8
    gradient: Gradient {
        GradientStop { position: 0.0; color: "red" }
        GradientStop { position: 0.33; color: "yellow" }
        GradientStop { position: 1.0; color: "green" }
    }
    focus: true
    Keys.onPressed: {
        if (event.key == Qt.Key_F1){
            mainwindow.showFullScreen();
        }
    }
    Keys.onEscapePressed:{
        Qt.quit();
    }
}
