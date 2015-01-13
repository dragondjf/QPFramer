import QtQuick 2.0

Rectangle {
    id: music_list
    width: 380
    height: 380
    clip: true
    property int curIndex: 0
    property string mplayed: "00:00/00:00"

    signal play(variant index)
    signal del(var index)


    onCurIndexChanged: {
        console.log(music_lv.currentIndex+""+curIndex);
        music_lv.currentItem.state = "normal";
        music_lv.currentIndex = curIndex;
        music_lv.currentItem.state = "playing";
    }
    function start(){
        music_lv.currentIndex = curIndex;
        music_lv.currentItem.state = "playing";
    }

    function stop(){
        music_lv.currentItem.state = "normal";
    }

    property variant model: ListModel{}

    Component {
        id: ml_delegate
        Rectangle {
            id: view_dg
            height: 30
            width: music_list.width
            state: "normal"
            SysBtn {
                id: ico
                z:1
                width: 20
                height: 20
                picNormal: "res/img/music_icon.png"
                picHovered: ico.picNormal
                picPressed: "res/img/Play_pressed_small.png"
                anchors.left: view_dg.left
                anchors.leftMargin: 10
                anchors.verticalCenter: parent.verticalCenter
                onHovered: {
                    if(view_dg.state != "playing")
                        view_dg.state = "hovered"
                }
                onClicked: {
                    play(index);
                    curIndex = index;
                    view_dg.state = "playing";
                }
            }
            Column{
                anchors.left: ico.right
                anchors.leftMargin: 10
                anchors.right: right_ctl.left
                anchors.verticalCenter: parent.verticalCenter
                spacing: 10
                Text {
                    id: music_title
                    text: title
                    color: '#000000'
                    elide: Text.ElideRight
                }
                Text {
                    id: music_played
                    text: mplayed
                    visible: false
                    color: music_title.color
                }
            }
            Row {
                id: right_ctl
                z: 1
                anchors.right: view_dg.right
                anchors.verticalCenter: parent.verticalCenter
                anchors.rightMargin: 20 + scrollbar.width
                SysBtn {
                    id: del_ico
                    width: 20
                    height: 20
                    picNormal: "res/img/music_del.png"
                    picHovered: del_ico.picNormal
                    picPressed: "res/img/music_del.png"
                    anchors.verticalCenter: parent.verticalCenter
                    onHovered: {
                        if(view_dg.state != "playing")
                            view_dg.state = "hovered"
                    }
                    onClicked: {
                        if(view_dg.state == "playing"){
                            play(index + 1);
                            curIndex = index + 1;
                            del(index);
                        }else{
                            del(index);
                        }
                    }
                }
                Text {
                    id: music_time
                    text: time
                    anchors.verticalCenter: parent.verticalCenter
                }
            }



            MouseArea {
                id : parMouseA
                hoverEnabled: true
                anchors.fill: parent
                onEntered: {
                    if(view_dg.state != "playing")
                        view_dg.state = "hovered"
                }
                onExited: {
                    if(view_dg.state != "playing")
                        view_dg.state = "normal"
                }
                onDoubleClicked: {
                    play(index);
                    curIndex = index;
                    view_dg.state = "playing";
                }
            }
            states: [
                State {
                    name: "hovered"
                    PropertyChanges {
                        target: del_ico
                        visible: true
                    }
                    PropertyChanges {
                        target: music_time
                        visible: false
                    }
                    PropertyChanges {
                        target: view_dg
                        color: "#CFE0F0" //#C1CEDC
                    }
                    PropertyChanges {
                        target: ico
                        picNormal: "res/img/Play_small.png"
                    }
                },
                State {
                    name: "normal"
                    PropertyChanges {
                        target: del_ico
                        visible: false
                    }
                    PropertyChanges {
                        target: music_time
                        visible: true
                    }
                    PropertyChanges {
                        target: view_dg
                        color: "transparent"
                    }
                },
                State {
                    name: "playing"
                    PropertyChanges {
                        target: ico
                        picNormal: "res/img/unknown.png"
                        width: 54
                        height: 54
                        anchors.verticalCenter: view_dg.verticalCenter
                    }
                    PropertyChanges {
                        target: view_dg
                        height : 54
                    }
                    PropertyChanges {
                        target: music_played
                        visible : true
                    }
                    PropertyChanges {
                        target: music_time
                        visible: false
                    }
                    PropertyChanges {
                        target: view_dg
                        color: "#AAB2B8"
                    }
                    PropertyChanges {
                        target:music_title
                        color: "#ffffff"
                    }
                }
            ]
            transitions: Transition {
                    PropertyAnimation {
                        property: "height";
                        easing.type: Easing.InOutQuad
                        duration: 500
                    }
                    PropertyAnimation {
                        target: ico
                        property: "opacity"
                        from: 0
                        to: 1

                    }
                }
        }
    }

    ListView {
        id: music_lv
        anchors.fill: parent
        model: music_list.model
        delegate: ml_delegate
        focus: true
    }
    Rectangle{
        id: scrollbar
        anchors.right: music_lv.right
        y: music_lv.visibleArea.yPosition * music_lv.height
        width: 10
        height: music_lv.visibleArea.heightRatio * music_lv.height
        color: "#d3d3d3"
        onHeightChanged: {
            if(height == music_lv.height){
                width = 0
            }else
                width = 10
        }
    }
}
