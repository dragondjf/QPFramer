import QtQuick 2.1
import QtQuick.Controls 1.0
import QtQuick.Window 2.1

ApplicationWindow {
    width: 480
    height: 640
    property alias stackView: stackView
    property alias componentPage: componentPage

    StackView {
        id: stackView
        anchors.fill: parent
        initialItem: componentPage
    }

    Component {
        id: componentPage
        Rectangle {
            color: "yellow"
            // ButtonMenu {
            //     index: parent.Stack.index
            // }
        }
    }
}