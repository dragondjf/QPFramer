import QtQuick 2.0

Item {
    id: root
    width: 800
    height: 600
    Splash{
        id: splash
        anchors.fill: parent
        Text{
            anchors.centerIn: splash
            text: 'Welcome, this is Splash!'
            font.family: "微软雅黑"
            font.pointSize: 20
            color: "white"
        }

        onFinished:{
            mainLaoder.source="AppPage.qml"
        }
    }

    Loader{
        anchors.fill: parent
        focus: true
        id: mainLaoder
    }
}
