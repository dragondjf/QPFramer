import QtQuick 2.0
import QtWebKit 3.0

WebView {
    id: webView
    width: 700
    height: 800
    url:"http://google.com"

    
    objectName: "myWebView"

    onLoadingChanged: {
        console.log("onLoadingChanged: status=" + loadRequest.status);
        if (loadRequest.status == WebView.LoadStartedStatus) 
            console.log("Loading started...");
        if (loadRequest.status == WebView.LoadFailedStatus) {
           console.log("Load failed! Error code: " + loadRequest.errorCode);
           if (loadRequest.errorCode === NetworkReply.OperationCanceledError)
               console.log("Load cancelled by user");
        } 
        if (loadRequest.status == WebView.LoadSucceededStatus) 
            console.log("Page loaded!");
    }

}