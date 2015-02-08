import QtQuick 2.0

Rectangle {
    id: root
    anchors.fill: parent
    anchors.margins: 10
    color: "#0085CF"
    focus: true

    Repeater {
        id: book
        model: 100
        Page{
            x: root.width / 2 + 10
            width: root.width / 2 - 20
            height: root.height
            color: "white"
            zindex: 100 - index 
            Text{
                anchors.centerIn: parent
                text: 'Welcome, this is Page %1 !'.arg(100 - index)
                font.family: "微软雅黑"
                font.pointSize: 20
                color: "green"
            }
        }
    }

    Keys.onPressed: {
        console.log(event.key)
        if (event.key == Qt.Key_1) {
            for(var i=0; i< 10; i++){
                var page = book.itemAt(book.count - i)
                if(page){
                    page.clicked()
                }
            }
            event.accepted = true;
        }
    }

}
