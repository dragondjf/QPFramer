import QtQuick 2.0
import QtQuick.Dialogs 1.0
import QtMultimedia 5.0

Rectangle {
    id: main
    width: 380
    height: 587

    property string title: main_title.text
    property string playing: ""
    property string ms_title: ""
    property string played: "00:00"
    property string playall: "/00:00"
    property int play_index: musiclist.curIndex
    property int play_way: 2
    property bool ctrlset: false

    property ListModel model_test: ListModel{}

    signal addNewMusic(var index,var one)
    signal delMusic(var index)

    /*play_way meaning
      -1: once
      0 : single loop
      1 : list play
      2 : list loop
      3 : randomly play
      */

    function play_music(index){
        ctrlset = true;
        if(model_test.get(index)["isMusic"] != true)
            return;
        musiclist.curIndex = index;
        playMusic.stop();
        playMusic.source = model_test.get(index)["source"];
        playall = '/'+model_test.get(index)["time"];
        ms_title = model_test.get(index)["title"];
        playMusic.play();
        playMusic.seek(0);
        console.log(playMusic.source+'|'+musiclist.curIndex+'|'+index+'|'+play_index);
        ctrlset = !ctrlset;
    }

    Image {
        id: main_bkg
        x: 0
        y: 0
        fillMode: Image.TileHorizontally
        source: "res/img/main_bkg.png"


        Text {
            id: main_title
            x:10;y:10
            color: "#ffffff"
            font.pointSize: 9
            font.pixelSize: 12
            text: qsTr("Qt播放器")
        }
        Text {
            id: music_title
            anchors.top: main_title.bottom
            anchors.left: main_bkg.left
            anchors.topMargin: 10
            anchors.leftMargin: 10
            height: 10
            text: ms_title

            color: "#ffffff"
        }
        SliderBar {
            id: sliderbar
            x: 8
            y: 55
            anchors.top: music_title.bottom
            anchors.topMargin: -226
            width: main_bkg.width - 20
            anchors.verticalCenterOffset: -231
            anchors.horizontalCenterOffset: 0
            maximumValue: playMusic.duration
            grooveColor: "#D3D3D3"
            value: playMusic.position


            onValueChanged: {
                if(sliderbar.pressed == true){
                    if(playMusic.playbackState == MediaPlayer.StoppedState)
                        playMusic.play();
                    playMusic.seek(value);
                }
            }
        }
        Row{
            id: time_dsply
            anchors.top: sliderbar.bottom
            anchors.topMargin: 5
            anchors.right: main_bkg.right
            anchors.rightMargin: 10
            Text {
                id: played_time
                text: main.played
                color: "#FFFFFF"
            }
            Text {
                id: play_time
                text: playall
                color: "#FFFFFF"
            }
        }
        Ctrler {
            id: control_btn
            x: 0
            y: 87
            width: 380
            anchors.top: time_dsply.bottom
            anchors.left: main_bkg.left
            anchors.right: main_bkg.right
            height: 50
            anchors.leftMargin: 0
            onPlay: {
                if(playMusic.playbackState == MediaPlayer.PlayingState){
                    playMusic.pause();
                }else if(playMusic.playbackState == MediaPlayer.PausedState){
                    playMusic.play();
                }else{
                    play_music(play_index);
                    musiclist.start();
                    console.log(play_index);
                }
            }
            onPrev: {
                if(play_index == 0){
                    play_music(model_test.count - 1);
                }else{
                    play_music(play_index - 1);
                }
            }
            onNext: {
                console.log(play_index+'|'+model_test.count)
                if(play_index == model_test.count - 1)
                    play_music(0);
                else
                    play_music(play_index+1);
            }
        }
        Rectangle {
            id:opacity_bkg
            height: 400
            anchors.top: control_btn.bottom
            anchors.left: main_bkg.left
            anchors.right: main_bkg.right
            anchors.topMargin: 10
            opacity: 0.4
            anchors.bottom: btb.top
        }
        MusicList {
            id: musiclist
            anchors.fill: opacity_bkg

            color: "#CDF2E1"
            model: model_test

            onPlay: {
//                play_index = index;
//                playMusic.source = model_test.get(index)["source"];
//                playall = '/'+model_test.get(index)["time"];
//                ms_title = model_test.get(index)["title"];
//                playMusic.play();
//                console.log(playMusic.source+'|'+playall);
                play_music(index);
            }
            onDel: {
                if(playMusic.playbackState == MediaPlayer.PlayingState)
                    playMusic.stop();
                model_test.remove(index);
                delMusic(index);
            }
        }
        BotBtnsGrp {
            id: btb
            z:1
            width: 200
            anchors.left: main_bkg.left
            anchors.bottom: main_bkg.bottom
            anchors.right: main_bkg.right

            onAddClick: {
                fileDialog.open();
            }

            onSchClick: {
                scharea_mask.visible = !scharea_mask.visible;
            }

        }
        Rectangle {
            id: scharea_mask
            z:1
            color: "#E3EFD1"
            visible: false
            height: search_area.height + 10
            anchors.bottom: btb.top
            anchors.left:main_bkg.left
            anchors.right: main_bkg.right
            Text {
                id: cls_btn
                text: qsTr("×")
                anchors.right: parent.right
                anchors.verticalCenter: parent.verticalCenter
                anchors.rightMargin: 5

                MouseArea {
                    anchors.fill: parent
                    onClicked: scharea_mask.visible = false
                }
            }
        }

        Rectangle {
            id: search_area
            z: 1
            height: sch_ico.height
            visible: scharea_mask.visible
            anchors.fill: scharea_mask
            anchors.margins: 5
            anchors.rightMargin: 20
            color: "white"
            Image {
                id: sch_ico
                source: "res/img/Search_ico.png"
                anchors.verticalCenter: search_area.verticalCenter
            }
            TextInput {
                id: search_text
                anchors.left: sch_ico.right
                anchors.verticalCenter: search_area.verticalCenter
                anchors.right: search_area.right
                text: ""
            }
        }
        SysBtnGrp {
            id: sysbtngrp
            x: 318
            y: 0

            onMin: window.showMinimized()
            onClose: window.close()
        }
        MouseArea {
            anchors.top: parent.top
            anchors.left: parent.left
            height: main_title.y + main_title.height + 2
            width: sysbtngrp.x - 1
            property variant previousPosition
            onPressed: {
                previousPosition = Qt.point(mouseX, mouseY)
            }
            onPositionChanged : {
                if (pressedButtons == Qt.LeftButton) {
                    var dx = mouseX - previousPosition.x
                    var dy = mouseY - previousPosition.y
                    window.x += dx;
                    window.y += dy;
                    //window.pos = Qt.point(window.pos.x + dx, window.pos.y + dy)
                }
            }
        }
    }
    FileDialog {
        id: fileDialog
        visible: false
        modality: Qt.WindowModal
        title: fileDialog.SelectFolder ? "Choose a folder" :
            (fileDialog.SelectMultiple ? "Choose some files" : "Choose a file")
        selectExisting: true
        selectMultiple: false
        selectFolder: false
        nameFilters: [ "Music files (*.mp3)" ]
        selectedNameFilter: "All files (*)"
        onAccepted: {
            for(var i = 0; i < fileUrls.length; i++){
                var s = fileUrls[i].toString().split('/');
                var title = decodeURIComponent(s[s.length-1].split('.')[0]);
                model_test.append({
                                      "title": title,
                                      "time" : "loading",
                                      "source": fileUrls[i],
                                      "isMusic": true
                                  });
                music.source = fileUrls[i];
                music.model_index = model_test.count - 1
                music.seek(111);
                music.play();
                addNewMusic(music.model_index,model_test.get(music.model_index));
            }
        }
        onRejected: { console.log("Rejected") }

    }
    MediaPlayer {
        id: music
        property int model_index: 0
        onPositionChanged: {
            var d = new Date(music.position);
            played = d.getMinutes()+':'+d.getSeconds();
            delete d;
        }
        onDurationChanged: {
            var d = new Date(music.duration);
            try{
                model_test.set(model_index,{
                                   "title": model_test.get(model_index)["title"],
                                   "time":d.getMinutes()+':'+d.getSeconds(),
                                   "source": model_test.get(model_index)["source"],
                                   "isMusic": true
                               });
                addNewMusic(music.model_index,model_test.get(music.model_index));
            }catch(err){
                console.log('Some Error:'+err);
            }


            model_index = -1;
            delete d;
            stop();
        }
    }
    MediaPlayer {
        id: playMusic
        source: playing
        volume: control_btn.vol
        onPositionChanged: {
            var d = new Date(playMusic.position);
            played = playMusic.position != playMusic.duration? d.getMinutes()+':'+d.getSeconds():"00:00";
            delete d;
            musiclist.mplayed = played+playall;
            playall.charCodeAt()
        }
        onStopped: {
            if(ctrlset)
                return;
            switch(play_way){
            case 0://single loop
                play_music(play_index);
                break;
            case 1://list play
                console.log(play_index + '|' + model_test.count);
                if(play_index != model_test.count - 1)
                    play_music(play_index + 1);
                else
                    musiclist.stop();
                break;
            case 2://list loop
                if(play_index == model_test.count - 1){
                    play_music(0);
                    break;
                }
                play_music(play_index + 1);
                break;
            case 3://randomly play
                do{
                    var i = Math.random();
                    var play_i = Math.floor(i*10 % (model_test.count));
                }while(play_i == play_index);
                play_music(play_i);
                break;
            default://once
            }
        }
    }
}
