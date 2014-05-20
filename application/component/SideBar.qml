import QtQuick 2.0

Rectangle {
    id: sidebar
    
    function toggleshow() {
        if(rightsidebar.opacity == 0){
            rightsidebar.opacity = 1;
        }else{
            rightsidebar.opacity = 0;
        }
    }

    opacity: 0

    onOpacityChanged:{
        if(sidebar.opacity == 0){
            sidebar.enabled = false;
        }
    }

    Behavior on opacity {
        NumberAnimation { duration: 1000 }
    }


}
