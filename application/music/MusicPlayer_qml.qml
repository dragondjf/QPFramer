import QtQuick 2.0
import QtQuick.Window 2.1
import QtQuick.Controls 1.0
import QtQuick.LocalStorage 2.0

import "Storage.js" as Storage

Window {
    id: window

    color: "gray"
    title: main.title
    modality: Qt.ApplicationModal
    flags: Qt.FramelessWindowHint|Qt.Window
    width: main.width + 2
    height: main.height + 2

    MainWindow {
        id: main
        z:1
        anchors.centerIn: parent
        model_test: model
        onAddNewMusic: {
            Storage.setMusic(index,one.title,one.time,one.source);
        }
        onDelMusic: {
            console.log(index);
            console.log(Storage.del(index));
        }
    }
//    RectangularGlow {
//        id: effect
//        anchors.fill: main
//        glowRadius: 10
//        spread: 0
//        color: "gray"
//        cornerRadius: 10
//    }
    ListModel {
        id: model
    }
    function loadList(){
        Storage.initialize();
        //Storage.clear(); //clear all
        var allCount = Storage.count();
        for(var i = 0;i < allCount;++i){
            var one = Storage.get(i);
            model.append({
                             "title": one.title,
                             "time" : one.time,
                             "source": one.source,
                             "isMusic": true
                         });
        }
    }

    Component.onCompleted: loadList()

}
